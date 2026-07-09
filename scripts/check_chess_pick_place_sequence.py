#!/usr/bin/env python3

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from perception.localization.board_calibration import default_manual_board_calibration
from apps.chess.move import ChessMove
from apps.chess.task_builder import build_pick_place_task
from apps.chess.pick_place_sequence import chess_pick_place_to_sequence

calibration = default_manual_board_calibration()
board = calibration.to_geometry()

move = ChessMove.from_uci("e2e4")
task = build_pick_place_task(move, board)
sequence = chess_pick_place_to_sequence(task)

print("Move:", move)
print("Waypoint count:", len(sequence))

for waypoint in sequence.waypoints:
    print(
        waypoint.name,
        waypoint.position,
        "gripper_closed=",
        waypoint.gripper_closed,
    )
