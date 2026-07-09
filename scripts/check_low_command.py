#!/usr/bin/env python3

from pathlib import Path
import sys
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from robot.commands.builders import command_from_current_position, apply_position_command
from robot.commands.position_command import JointPositionCommand
from robot.model.joint_indices import LEFT_SHOULDER_PITCH

current_q = np.zeros(29)

cmd = command_from_current_position(current_q)
cmd = apply_position_command(
    cmd,
    JointPositionCommand(
        joint_index=LEFT_SHOULDER_PITCH,
        q_target=0.5,
    ),
)

print("Command size:", len(cmd.q_target))
print("Left shoulder pitch target:", cmd.q_target[LEFT_SHOULDER_PITCH])
print("Left shoulder pitch kp:", cmd.kp[LEFT_SHOULDER_PITCH])
print("Left shoulder pitch kd:", cmd.kd[LEFT_SHOULDER_PITCH])
