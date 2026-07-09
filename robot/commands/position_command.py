#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass(frozen=True)
class JointPositionCommand:
    joint_index: int
    q_target: float
    dq_target: float = 0.0
    tau_ff: float = 0.0
