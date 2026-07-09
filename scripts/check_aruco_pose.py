#!/usr/bin/env python3

from pathlib import Path
import sys
import cv2
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from perception.detection.aruco_detector import ArucoDetector
from perception.localization.aruco_pose import (
    default_no_distortion_calibration,
    estimate_marker_pose,
)

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

marker = aruco.generateImageMarker(
    dictionary,
    id=7,
    sidePixels=300,
)

image = np.ones((600, 800), dtype=np.uint8) * 255
image[150:450, 250:550] = marker

detector = ArucoDetector()
result = detector.detect(image)

print("Detected IDs:", result.ids())

calibration = default_no_distortion_calibration(
    image_width=800,
    image_height=600,
)

pose = estimate_marker_pose(
    marker=result.markers[0],
    marker_size_m=0.05,
    calibration=calibration,
)

print("Marker ID:", pose.marker_id)
print("Marker position in camera frame:", pose.position_camera_frame)
print("rvec:", pose.rvec.reshape(-1))
print("tvec:", pose.tvec.reshape(-1))
