#!/usr/bin/env python3

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from perception.localization.board_pose_estimator import ManualBoardPoseEstimator
from apps.chess.move import ChessMove
from apps.chess.task_builder import build_pick_place_task

estimator = ManualBoardPoseEstimator()
estimate = estimator.estimate()

board = estimate.calibration.to_geometry()
move = ChessMove.from_uci("e2e4")
task = build_pick_place_task(move, board)

print("Pose method:", estimate.method)
print("Confidence:", estimate.confidence)
print("Calibration:", estimate.calibration)
print("Source pick:", task.source_pick)
print("Target place:", task.target_place)
