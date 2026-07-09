#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from robot.kinematics.pinocchio_solver import G1DKinematics

kin = G1DKinematics()

pose = kin.forward_kinematics()

print()
print("Right Dex1.1 base FK:")
print(pose)
