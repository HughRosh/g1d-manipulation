#!/usr/bin/env python3

from dataclasses import dataclass
import math

from apps.chess.board_geometry import FILES, RANKS, ChessBoardGeometry
from perception.detection.yolo_detector import YOLODetection
from apps.chess.perception.piece_observation import PieceObservation


@dataclass(frozen=True)
class ProjectedSquare:
    square: str
    center_px: tuple[float, float]


def nearest_projected_square(
    detection: YOLODetection,
    projected_squares: list[ProjectedSquare],
) -> ProjectedSquare:
    cx, cy = detection.center_px

    best_square = None
    best_dist = float("inf")

    for square in projected_squares:
        sx, sy = square.center_px
        dist = math.hypot(cx - sx, cy - sy)

        if dist < best_dist:
            best_dist = dist
            best_square = square

    if best_square is None:
        raise ValueError("No projected squares available")

    return best_square


def assign_detection_to_square(
    detection: YOLODetection,
    projected_squares: list[ProjectedSquare],
    board: ChessBoardGeometry,
) -> PieceObservation:
    square = nearest_projected_square(detection, projected_squares)

    return PieceObservation(
        class_name=detection.class_name,
        confidence=detection.confidence,
        square=square.square,
        image_center_px=detection.center_px,
        robot_position=board.pick_point(square.square),
    )


def all_square_names() -> list[str]:
    return [file + rank for rank in RANKS for file in FILES]
