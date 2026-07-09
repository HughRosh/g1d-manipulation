#!/usr/bin/env python3

"""
Chessboard geometry.

Converts chess squares (e2, e4, etc.) into robot-frame coordinates.
"""

FILES = "abcdefgh"
RANKS = "12345678"


class ChessBoardGeometry:

    def __init__(self, scene):

        board = scene["board"]

        self.center_x = board["x_m"]
        self.center_y = board["y_m"]
        self.board_size = board["size_m"]

        self.square_size = self.board_size / 8.0

    def square_center(self, square):

        file_index = FILES.index(square[0])
        rank_index = RANKS.index(square[1])

        x = self.center_x + (file_index - 3.5) * self.square_size
        y = self.center_y + (rank_index - 3.5) * self.square_size

        return x, y
