import argparse
import cv2

from g1d_chess.vision.board_roi_detector import BoardROIDetector


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--out", default="board_roi_debug.jpg")
    parser.add_argument("--x-min", type=float, default=0.12)
    parser.add_argument("--x-max", type=float, default=0.78)
    parser.add_argument("--y-min", type=float, default=0.61)
    parser.add_argument("--y-max", type=float, default=0.95)
    args = parser.parse_args()

    image = cv2.imread(args.image)
    if image is None:
        raise FileNotFoundError(args.image)

    detector = BoardROIDetector(args.x_min, args.x_max, args.y_min, args.y_max)
    debug = detector.debug_draw(image)
    cv2.imwrite(args.out, debug)

    print(f"Saved {args.out}")
    print(detector.square_centers_image(image))


if __name__ == "__main__":
    main()
