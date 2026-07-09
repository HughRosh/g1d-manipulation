#!/usr/bin/env python3

"""
Coordinate frame definitions.

All positions are expressed in meters.

Frames:

world
 └── robot_base
      └── table
           └── chess_board
                └── square
                     └── tool
"""

from dataclasses import dataclass


@dataclass
class Frame:

    name: str

    parent: str | None

    translation_xyz: list

    rotation_xyzw: list


WORLD = Frame(
    "world",
    None,
    [0.0,0.0,0.0],
    [0.0,0.0,0.0,1.0]
)

ROBOT_BASE = Frame(
    "robot_base",
    "world",
    [0.0,0.0,0.0],
    [0.0,0.0,0.0,1.0]
)

TABLE = Frame(
    "table",
    "robot_base",
    [0.78,0.0,0.75],
    [0.0,0.0,0.0,1.0]
)

BOARD = Frame(
    "board",
    "table",
    [-0.18,0.0,0.04],
    [0.0,0.0,0.0,1.0]
)
