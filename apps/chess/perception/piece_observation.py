#!/usr/bin/env python3

from dataclasses import dataclass

from apps.chess.board_geometry import Point3D


@dataclass(frozen=True)
class PieceObservation:
    class_name: str
    confidence: float
    square: str
    image_center_px: tuple[float, float]
    robot_position: Point3D
