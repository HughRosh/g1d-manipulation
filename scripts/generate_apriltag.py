#!/usr/bin/env python3

import cv2

dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_APRILTAG_36h11
)

tag_id = 0
size_px = 600

img = cv2.aruco.generateImageMarker(
    dictionary,
    tag_id,
    size_px,
)

out = "apriltag_36h11_id0.png"
cv2.imwrite(out, img)

print(f"Saved {out}")
