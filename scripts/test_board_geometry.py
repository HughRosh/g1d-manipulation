#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from chessbot.board import ChessBoardGeometry

board = ChessBoardGeometry(
    origin_x=0.40,
    origin_y=-0.20,
    square=0.05,
)

for sq in ["a1","e2","e4","h8"]:
    print(sq, board.square_center(sq))
