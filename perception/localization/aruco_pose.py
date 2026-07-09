#!/usr/bin/env python3

from dataclasses import dataclass
import cv2
import numpy as np

from apps.chess.board_geometry import Point3D, Vector3D
from perception.detection.aruco_detector import DetectedMarker


@dataclass(frozen=True)
class CameraCalibration:
    camera_matrix: np.ndarray
    dist_coeffs: np.ndarray


@dataclass(frozen=True)
class MarkerPose:
    marker_id: int
    rvec: np.ndarray
    tvec: np.ndarray

    @property
    def position_camera_frame(self) -> Point3D:
        t = self.tvec.reshape(-1)
        return Point3D(
            x=float(t[0]),
            y=float(t[1]),
            z=float(t[2]),
        )


def default_no_distortion_calibration(
    image_width: int,
    image_height: int,
    focal_length_px: float | None = None,
) -> CameraCalibration:
    if focal_length_px is None:
        focal_length_px = float(max(image_width, image_height))

    camera_matrix = np.array(
        [
            [focal_length_px, 0.0, image_width / 2.0],
            [0.0, focal_length_px, image_height / 2.0],
            [0.0, 0.0, 1.0],
        ],
        dtype=np.float64,
    )

    dist_coeffs = np.zeros((5, 1), dtype=np.float64)

    return CameraCalibration(
        camera_matrix=camera_matrix,
        dist_coeffs=dist_coeffs,
    )


def estimate_marker_pose(
    marker: DetectedMarker,
    marker_size_m: float,
    calibration: CameraCalibration,
) -> MarkerPose:
    half = marker_size_m / 2.0

    object_points = np.array(
        [
            [-half, half, 0.0],
            [half, half, 0.0],
            [half, -half, 0.0],
            [-half, -half, 0.0],
        ],
        dtype=np.float64,
    )

    image_points = marker.corners.reshape(4, 2).astype(np.float64)

    success, rvec, tvec = cv2.solvePnP(
        object_points,
        image_points,
        calibration.camera_matrix,
        calibration.dist_coeffs,
        flags=cv2.SOLVEPNP_IPPE_SQUARE,
    )

    if not success:
        raise RuntimeError(f"solvePnP failed for marker {marker.marker_id}")

    return MarkerPose(
        marker_id=marker.marker_id,
        rvec=rvec,
        tvec=tvec,
    )
