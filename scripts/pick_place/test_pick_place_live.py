import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import cv2
import yaml

from perception.pick_place.yolo_pick_detector import YoloPickDetector
from manipulation.pick_place.image_to_robot import ImageToRobotMapper
from manipulation.pick_place.dry_run_executor import DryRunPickPlaceExecutor, PickPlaceCommand


def main():
    with open("configs/pick_place.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    detector = YoloPickDetector(
        model_path=cfg["vision"]["model_path"],
        confidence=float(cfg["vision"]["confidence"]),
    )

    cam = cv2.VideoCapture(int(cfg["vision"]["camera_index"]))

    if not cam.isOpened():
        raise RuntimeError("Could not open camera")

    ret, frame = cam.read()
    if not ret:
        raise RuntimeError("Could not read first frame")

    h, w = frame.shape[:2]

    cal = cfg["calibration"]
    mapper = ImageToRobotMapper(
        image_x_min_px=0,
        image_x_max_px=w,
        image_y_min_px=0,
        image_y_max_px=h,
        robot_x_min_m=float(cal["robot_x_min_m"]),
        robot_x_max_m=float(cal["robot_x_max_m"]),
        robot_y_min_m=float(cal["robot_y_min_m"]),
        robot_y_max_m=float(cal["robot_y_max_m"]),
    )

    executor = DryRunPickPlaceExecutor()

    print("Press p to print dry-run pick-place command")
    print("Press q to quit")

    latest_pick_xyz = None

    while True:
        ok, frame = cam.read()
        if not ok:
            print("Failed to read frame")
            break

        detections = detector.detect(frame)
        selected = detector.choose_best(detections)
        debug = detector.draw(frame, detections, selected)

        if selected is not None:
            rx, ry = mapper.map_px_to_robot(selected.center_px)
            rz = float(cfg["pick"]["pick_height_m"])
            latest_pick_xyz = (rx, ry, rz)

            cx, cy = [int(v) for v in selected.center_px]

            cv2.putText(
                debug,
                f"SELECTED: {selected.label}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
            )

            cv2.putText(
                debug,
                f"PICK XYZ: {rx:.3f}, {ry:.3f}, {rz:.3f}",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
            )

            cv2.circle(debug, (cx, cy), 12, (0, 0, 255), 3)

        cv2.imshow("YOLO Pick Place Dry Run", debug)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        if key == ord("p"):
            if latest_pick_xyz is None:
                print("No object selected")
            else:
                cmd = PickPlaceCommand(
                    pick_xyz=latest_pick_xyz,
                    place_xyz=tuple(float(x) for x in cfg["robot"]["place_xyz"]),
                    approach_height_m=float(cfg["pick"]["approach_height_m"]),
                )
                executor.execute(cmd)

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
