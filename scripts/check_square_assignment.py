#!/usr/bin/env python3

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from apps.chess.board_geometry import create_axis_aligned_board, Point3D
from apps.chess.perception.square_assignment import ProjectedSquare, assign_detection_to_square
from perception.detection.yolo_detector import YOLODetection

board = create_axis_aligned_board(
    origin_a1=Point3D(x=0.30, y=-0.20, z=0.00),
    square_size=0.05,
)

projected_squares = [
    ProjectedSquare("e2", (420.0, 310.0)),
    ProjectedSquare("e4", (420.0, 230.0)),
    ProjectedSquare("d4", (380.0, 230.0)),
]

detection = YOLODetection(
    class_id=0,
    class_name="white_pawn",
    confidence=0.91,
    xyxy=(400.0, 210.0, 440.0, 250.0),
)

observation = assign_detection_to_square(
    detection=detection,
    projected_squares=projected_squares,
    board=board,
)

print("Detected:", observation.class_name)
print("Assigned square:", observation.square)
print("Image center:", observation.image_center_px)
print("Robot pick position:", observation.robot_position)
