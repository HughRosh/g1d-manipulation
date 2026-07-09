#!/usr/bin/env python3

"""
Robot State

Stores the robot's current estimated state.
"""

from dataclasses import dataclass, field
import numpy as np


@dataclass
class RobotState:

    arm_q: np.ndarray = field(default_factory=lambda: np.zeros(14))
    gripper_open: bool = True

    tool_position: np.ndarray = field(default_factory=lambda: np.zeros(3))
    tool_quaternion: np.ndarray = field(
        default_factory=lambda: np.array([0.,0.,0.,1.])
    )
