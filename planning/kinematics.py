#!/usr/bin/env python3

"""
Kinematics module.

This is the future home of:
- forward kinematics
- inverse kinematics
- top-down gripper constraints
- Cartesian pose planning

For now this file defines the target-pose format used by the planner.
"""


class TargetPose:
    def __init__(self, x, y, z, approach="top_down"):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.approach = approach

    def as_dict(self):
        return {
            "position": [self.x, self.y, self.z],
            "approach": self.approach,
        }


def make_top_down_pose(x, y, z):
    return TargetPose(x, y, z, approach="top_down")


def placeholder_ik(target_pose):
    """
    Placeholder IK.

    Returns a 14-joint arm command for the dual-arm controller.
    This will later be replaced with a real IK solver.
    """
    q = [0.0] * 14
    return q
