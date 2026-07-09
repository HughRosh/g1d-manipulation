#!/usr/bin/env python3

from dataclasses import dataclass
import numpy as np

from manipulation.planning.joint_trajectory import JointTrajectory
from robot.model.joint_indices import G1D_NUM_MOTOR, INVALID_FOR_G1D, JOINT_INDEX_TO_NAME
from robot.model.joint_limits import get_joint_limit


@dataclass(frozen=True)
class SafetyReport:
    ok: bool
    messages: list[str]


def check_trajectory_safety(
    trajectory: JointTrajectory,
    max_step_delta: float = 0.08,
    allow_invalid_motor_motion: bool = False,
) -> SafetyReport:
    messages: list[str] = []

    if trajectory.dof != G1D_NUM_MOTOR:
        messages.append(
            f"Expected trajectory DOF {G1D_NUM_MOTOR}, got {trajectory.dof}"
        )

    if trajectory.steps < 2:
        messages.append("Trajectory must have at least 2 steps")

    if not np.all(np.isfinite(trajectory.positions)):
        messages.append("Trajectory contains NaN or infinite values")

    for index in JOINT_INDEX_TO_NAME:
        limit = get_joint_limit(index)
        q = trajectory.positions[:, index]

        if np.any(q < limit.lower):
            messages.append(
                f"Joint {index} {JOINT_INDEX_TO_NAME[index]} goes below lower limit {limit.lower}"
            )

        if np.any(q > limit.upper):
            messages.append(
                f"Joint {index} {JOINT_INDEX_TO_NAME[index]} goes above upper limit {limit.upper}"
            )

    if not allow_invalid_motor_motion:
        for index in INVALID_FOR_G1D:
            q = trajectory.positions[:, index]
            if np.max(np.abs(q - q[0])) > 1e-6:
                messages.append(
                    f"Invalid G1-D motor slot {index} changes during trajectory"
                )

    if trajectory.steps >= 2:
        step_delta = np.abs(np.diff(trajectory.positions, axis=0))
        max_delta = float(np.max(step_delta))

        if max_delta > max_step_delta:
            messages.append(
                f"Max per-step joint change {max_delta:.4f} exceeds limit {max_step_delta:.4f}"
            )

    return SafetyReport(
        ok=len(messages) == 0,
        messages=messages,
    )


def require_safe_trajectory(
    trajectory: JointTrajectory,
    max_step_delta: float = 0.08,
    allow_invalid_motor_motion: bool = False,
) -> None:
    report = check_trajectory_safety(
        trajectory=trajectory,
        max_step_delta=max_step_delta,
        allow_invalid_motor_motion=allow_invalid_motor_motion,
    )

    if not report.ok:
        joined = "\n".join(report.messages)
        raise ValueError(f"Unsafe trajectory:\n{joined}")
