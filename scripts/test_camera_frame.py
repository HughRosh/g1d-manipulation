#!/usr/bin/env python3

from pathlib import Path
import sys
import cv2

sys.path.append(str(Path(__file__).resolve().parents[1]))

from vision.camera import Camera


def main():
    cam = Camera(index=0)
    frame = cam.read()
    cam.release()

    out = "camera_test_frame.jpg"
    cv2.imwrite(out, frame)

    print(f"Saved {out}")


if __name__ == "__main__":
    main()
