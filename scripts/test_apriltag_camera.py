#!/usr/bin/env python3

from pathlib import Path
import sys
import cv2

sys.path.append(str(Path(__file__).resolve().parents[1]))

from vision.camera import Camera
from perception.apriltag_detector import AprilTagDetector


def main():
    cam = Camera(index=0)
    detector = AprilTagDetector()

    frame = cam.read()
    cam.release()

    tags = detector.detect(frame)

    print("Detected tags:")
    print(tags)

    for tag in tags:
        corners = tag["corners"]
        for x, y in corners:
            cv2.circle(frame, (int(x), int(y)), 6, (0, 255, 0), -1)

    cv2.imwrite("apriltag_detection_debug.jpg", frame)
    print("Saved apriltag_detection_debug.jpg")


if __name__ == "__main__":
    main()
