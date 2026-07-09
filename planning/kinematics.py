#!/usr/bin/env python3

"""
Kinematics utilities.

This module defines the Cartesian pose representation used
throughout the project.

All end-effector targets are represented as:

    Position (x, y, z)
    Quaternion (x, y, z, w)

No Euler angles are stored internally.

The planner should never command joints directly.
"""

from dataclasses import dataclass
import math


@dataclass
class TargetPose:

    position_xyz: list
    orientation_xyzw: list

    def as_dict(self):
        return {
            "position_xyz": self.position_xyz,
            "orientation_xyzw": self.orientation_xyzw,
        }


def quaternion_from_yaw(yaw):

    half = yaw * 0.5

    return [
        0.0,
        0.0,
        math.sin(half),
        math.cos(half),
    ]


def make_top_down_pose(x, y, z, yaw=0.0):
    """
    Create a pose whose tool Z-axis is normal to the table.

    For now this assumes a top-down grasp with only yaw rotation.
    """

    q = quaternion_from_yaw(yaw)

    return TargetPose(
        position_xyz=[float(x), float(y), float(z)],
        orientation_xyzw=q,
    )


def placeholder_ik(target_pose):
    """
    Placeholder inverse kinematics.

    Future versions will convert the target pose into
    the 14 arm joint values used by the controller.
    """

    return [0.0] * 14
