#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from planning.kinematics import make_top_down_pose
from planning.trajectory import interpolate_pose

start = make_top_down_pose(0.40, 0.00, 0.90)
goal  = make_top_down_pose(0.60,-0.20, 0.80)

traj = interpolate_pose(start, goal)

print(f"{len(traj)} waypoints")

for p in traj:
    print(p.as_dict())
