#!/usr/bin/env python3

from src.utils import load_config
from world.world_model import *


def load_world():

    scene = load_config("configs/scene.yaml")["scene"]

    world = WorldModel()

    table = scene["table"]
    board = scene["board"]
    cup = scene["cup"]

    world.add(
        WorldObject(
            "table",
            table,
            (
                table["size_x_m"],
                table["size_y_m"],
                table["thickness_m"],
            ),
        )
    )

    world.add(
        WorldObject(
            "board",
            board,
            (
                board["size_m"],
                board["size_m"],
                board["thickness_m"],
            ),
        )
    )

    world.add(
        WorldObject(
            "cup",
            cup,
            (
                cup["radius_m"]*2,
                cup["radius_m"]*2,
                cup["height_m"],
            ),
        )
    )

    return world
