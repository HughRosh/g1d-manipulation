#!/usr/bin/env python3

from dataclasses import dataclass
import numpy as np

from apps.chess.board_geometry import Point3D, Vector3D
from perception.localization.board_calibration import BoardCalibration


@dataclass(frozen=True)
class BoardCornerMarkerMap:
    a1_marker_id: int
    h1_marker_id: int
    a8_marker_id: int
    h8_marker_id: int


@dataclass(frozen=True)
class MarkerPosition:
    marker_id: int
    position: Point3D


def point_to_array(point: Point3D) -> np.ndarray:
    return np.array([point.x, point.y, point.z], dtype=float)


def array_to_point(array: np.ndarray) -> Point3D:
    return Point3D(
        x=float(array[0]),
        y=float(array[1]),
        z=float(array[2]),
    )


def array_to_vector(array: np.ndarray) -> Vector3D:
    return Vector3D(
        x=float(array[0]),
        y=float(array[1]),
        z=float(array[2]),
    )


def calibration_from_corner_markers(
    marker_positions: list[MarkerPosition],
    marker_map: BoardCornerMarkerMap,
    square_size: float | None = None,
    approach_height: float = 0.10,
    pick_height: float = 0.02,
) -> BoardCalibration:
    by_id = {marker.marker_id: marker.position for marker in marker_positions}

    required = [
        marker_map.a1_marker_id,
        marker_map.h1_marker_id,
        marker_map.a8_marker_id,
        marker_map.h8_marker_id,
    ]

    missing = [marker_id for marker_id in required if marker_id not in by_id]

    if missing:
        raise ValueError(f"Missing required board corner marker IDs: {missing}")

    a1 = point_to_array(by_id[marker_map.a1_marker_id])
    h1 = point_to_array(by_id[marker_map.h1_marker_id])
    a8 = point_to_array(by_id[marker_map.a8_marker_id])
    h8 = point_to_array(by_id[marker_map.h8_marker_id])

    file_vector = h1 - a1
    rank_vector = a8 - a1

    measured_file_size = float(np.linalg.norm(file_vector) / 7.0)
    measured_rank_size = float(np.linalg.norm(rank_vector) / 7.0)

    if square_size is None:
        square_size = (measured_file_size + measured_rank_size) / 2.0

    origin_a1 = a1

    return BoardCalibration(
        origin_a1=array_to_point(origin_a1),
        file_direction=array_to_vector(file_vector),
        rank_direction=array_to_vector(rank_vector),
        square_size=square_size,
        approach_height=approach_height,
        pick_height=pick_height,
    )
