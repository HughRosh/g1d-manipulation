#!/usr/bin/env python3

"""
Trajectory generation.

Interpolates between Cartesian target poses.
"""

import numpy as np
from planning.kinematics import TargetPose


def interpolate_pose(start, goal, steps=20):

    p0 = np.asarray(start.position_xyz)
    p1 = np.asarray(goal.position_xyz)

    poses = []

    for i in range(steps + 1):

        alpha = i / steps

        p = (1 - alpha) * p0 + alpha * p1

        poses.append(
            TargetPose(
                position_xyz=p.tolist(),
                orientation_xyzw=goal.orientation_xyzw,
            )
        )

    return poses
