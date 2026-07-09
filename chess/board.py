#!/usr/bin/env python3

FILES = "abcdefgh"
RANKS = "12345678"


class ChessBoardGeometry:

    def __init__(self, origin_x, origin_y, square):

        self.origin_x = origin_x
        self.origin_y = origin_y
        self.square = square

    def square_center(self, square_name):

        f = FILES.index(square_name[0])
        r = RANKS.index(square_name[1])

        x = self.origin_x + (f + 0.5) * self.square
        y = self.origin_y + (r + 0.5) * self.square

        return x, y
