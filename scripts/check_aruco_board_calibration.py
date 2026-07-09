#!/usr/bin/env python3

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from apps.chess.move import ChessMove
from apps.chess.task_builder import build_pick_place_task
from apps.chess.board_geometry import Point3D
from perception.localization.aruco_board_calibration import (
    BoardCornerMarkerMap,
    MarkerPosition,
    calibration_from_corner_markers,
)

marker_map = BoardCornerMarkerMap(
    a1_marker_id=10,
    h1_marker_id=11,
    a8_marker_id=12,
    h8_marker_id=13,
)

markers = [
    MarkerPosition(10, Point3D(0.30, -0.20, 0.00)),
    MarkerPosition(11, Point3D(0.65, -0.20, 0.00)),
    MarkerPosition(12, Point3D(0.30, 0.15, 0.00)),
    MarkerPosition(13, Point3D(0.65, 0.15, 0.00)),
]

calibration = calibration_from_corner_markers(
    marker_positions=markers,
    marker_map=marker_map,
)

board = calibration.to_geometry()
move = ChessMove.from_uci("e2e4")
task = build_pick_place_task(move, board)

print("Calibration:", calibration)
print("Measured square size:", calibration.square_size)
print("Source pick:", task.source_pick)
print("Target place:", task.target_place)
