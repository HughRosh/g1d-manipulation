#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from world.world_model import *

world = WorldModel()

world.add(
    WorldObject(
        "cup",
        None,
        (0.07,0.07,0.12)
    )
)

world.add(
    WorldObject(
        "board",
        None,
        (0.40,0.40,0.01)
    )
)

print(world.list_objects())
