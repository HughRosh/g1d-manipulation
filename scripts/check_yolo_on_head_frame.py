#!/usr/bin/env python3

from pathlib import Path
import sys
import cv2

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from perception.detection.yolo_detector import YOLODetector

image_path = Path("head_frame.jpg")

if not image_path.exists():
    raise FileNotFoundError(
        "Missing head_frame.jpg. Copy the robot camera frame into the repo root first."
    )

image = cv2.imread(str(image_path))

detector = YOLODetector()
result = detector.detect(image)

print("Detections:", result.count)

for detection in result.detections:
    print(
        detection.class_name,
        f"conf={detection.confidence:.2f}",
        "center=",
        detection.center_px,
        "box=",
        detection.xyxy,
    )
