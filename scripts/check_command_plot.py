#!/usr/bin/env python3

from pathlib import Path
import sys
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from manipulation.execution.trajectory_executor import TrajectoryExecutor
from manipulation.planning.arm_targets import make_full_body_target_from_arm_targets
from manipulation.planning.joint_trajectory import linear_joint_trajectory
from robot.commands.sinks import RecordingCommandSink
from robot.logging.plot_command_log import plot_command_log
from robot.model.joint_indices import (
    LEFT_SHOULDER_PITCH,
    LEFT_ELBOW,
    RIGHT_SHOULDER_PITCH,
    RIGHT_ELBOW,
    JOINT_INDEX_TO_NAME,
)

q_start = np.zeros(29)

q_goal = make_full_body_target_from_arm_targets(
    q_start,
    left_arm_target=[0.3, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0],
    right_arm_target=[-0.3, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0],
)

trajectory = linear_joint_trajectory(
    q_start=q_start,
    q_goal=q_goal,
    duration=1.0,
    dt=0.05,
)

sink = RecordingCommandSink()

executor = TrajectoryExecutor(
    command_sink=sink,
    realtime=False,
)

executor.execute(trajectory)

output_path = Path("logs/check_command_plot.png")

plot_command_log(
    sink=sink,
    output_path=output_path,
    joint_indices=[
        LEFT_SHOULDER_PITCH,
        LEFT_ELBOW,
        RIGHT_SHOULDER_PITCH,
        RIGHT_ELBOW,
    ],
    joint_names=JOINT_INDEX_TO_NAME,
)

print("Saved:", output_path)
