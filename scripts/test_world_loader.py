#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from world.load_scene import load_world

world = load_world()

print()

for name in world.list_objects():
    print(name)
