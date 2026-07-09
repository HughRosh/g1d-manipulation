#!/usr/bin/env python3

from dataclasses import dataclass


FILES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANKS = ["1", "2", "3", "4", "5", "6", "7", "8"]


@dataclass(frozen=True)
class Point3D:
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class ChessBoardGeometry:
    origin_a1: Point3D
    square_size: float
    approach_height: float = 0.10
    pick_height: float = 0.02

    def square_center(self, square: str) -> Point3D:
        if len(square) != 2:
            raise ValueError(f"Invalid square name: {square}")

        file_char = square[0].lower()
        rank_char = square[1]

        if file_char not in FILES:
            raise ValueError(f"Invalid file: {file_char}")

        if rank_char not in RANKS:
            raise ValueError(f"Invalid rank: {rank_char}")

        file_index = FILES.index(file_char)
        rank_index = RANKS.index(rank_char)

        return Point3D(
            x=self.origin_a1.x + file_index * self.square_size,
            y=self.origin_a1.y + rank_index * self.square_size,
            z=self.origin_a1.z,
        )

    def approach_point(self, square: str) -> Point3D:
        center = self.square_center(square)
        return Point3D(
            x=center.x,
            y=center.y,
            z=center.z + self.approach_height,
        )

    def pick_point(self, square: str) -> Point3D:
        center = self.square_center(square)
        return Point3D(
            x=center.x,
            y=center.y,
            z=center.z + self.pick_height,
        )
