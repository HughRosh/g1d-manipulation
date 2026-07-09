#!/usr/bin/env python3

from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class FOVCameraModel:
    width_px: int
    height_px: int
    horizontal_fov_deg: float
    vertical_fov_deg: float

    def camera_matrix(self) -> np.ndarray:
        fx = (self.width_px / 2.0) / math.tan(math.radians(self.horizontal_fov_deg) / 2.0)
        fy = (self.height_px / 2.0) / math.tan(math.radians(self.vertical_fov_deg) / 2.0)

        cx = self.width_px / 2.0
        cy = self.height_px / 2.0

        return np.array(
            [
                [fx, 0.0, cx],
                [0.0, fy, cy],
                [0.0, 0.0, 1.0],
            ],
            dtype=np.float64,
        )

    def distortion_coeffs(self) -> np.ndarray:
        return np.zeros((5, 1), dtype=np.float64)


def rough_g1d_head_camera_model() -> FOVCameraModel:
    return FOVCameraModel(
        width_px=1280,
        height_px=720,
        horizontal_fov_deg=55.2,
        vertical_fov_deg=42.4,
    )
