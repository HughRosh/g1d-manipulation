#!/usr/bin/env python3

from robot.model.joint_indices import G1D_NUM_MOTOR

KP = [
    0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0,
    60, 0, 40,
    40, 40, 40, 40, 40, 40, 40,
    40, 40, 40, 40, 40, 40, 40,
]

KD = [
    0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0,
    1, 0, 1,
    1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1,
]

assert len(KP) == G1D_NUM_MOTOR
assert len(KD) == G1D_NUM_MOTOR
