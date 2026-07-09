#!/usr/bin/env python3

from pathlib import Path
import cv2

output_dir = Path("assets/aruco_markers")
output_dir.mkdir(parents=True, exist_ok=True)

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

marker_ids = {
    10: "a1_corner",
    11: "h1_corner",
    12: "a8_corner",
    13: "h8_corner",
}

for marker_id, name in marker_ids.items():
    image = cv2.aruco.generateImageMarker(
        dictionary,
        id=marker_id,
        sidePixels=800,
    )

    output_path = output_dir / f"marker_{marker_id}_{name}.png"
    cv2.imwrite(str(output_path), image)
    print("Saved", output_path)
