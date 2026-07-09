#!/usr/bin/env python3

"""
Pose error utilities for SE(3) inverse kinematics.
"""

import pinocchio as pin


def pose_error(current, target):
    """
    Compute a 6D error vector between two SE(3) poses.

    Returns:
        [dx, dy, dz, rx, ry, rz]
    """
    err = pin.log6(current.inverse() * target)
    return err.vector
