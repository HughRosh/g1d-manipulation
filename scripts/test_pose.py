#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from planning.kinematics import make_top_down_pose


pose = make_top_down_pose(
    x=0.45,
    y=-0.20,
    z=0.83,
    yaw=0.0,
)

print(pose.as_dict())
