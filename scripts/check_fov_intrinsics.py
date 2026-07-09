#!/usr/bin/env python3

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from perception.camera.fov_intrinsics import rough_g1d_head_camera_model

model = rough_g1d_head_camera_model()
camera_matrix = model.camera_matrix()

print("Camera model:", model)
print("Camera matrix:")
print(camera_matrix)
print("Distortion:")
print(model.distortion_coeffs())
