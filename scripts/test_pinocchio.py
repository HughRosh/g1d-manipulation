#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from robot.kinematics.pinocchio_solver import G1DKinematics

G1DKinematics()
