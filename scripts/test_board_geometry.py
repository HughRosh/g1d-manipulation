#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.utils import load_config
from chessbot.board import ChessBoardGeometry

scene = load_config("configs/scene.yaml")["scene"]

board = ChessBoardGeometry(scene)

print()

for sq in [
    "a1",
    "d4",
    "e2",
    "e4",
    "h8"
]:
    print(f"{sq:>3} -> {board.square_center(sq)}")
