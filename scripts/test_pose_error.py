#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pinocchio as pin
from robot.kinematics.ik import pose_error

a = pin.SE3.Identity()
b = pin.SE3.Identity()

print("Pose error:")
print(pose_error(a, b))
