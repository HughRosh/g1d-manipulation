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
from robot.logging.command_log import save_command_log_csv

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

output_path = Path("logs/check_command_log.csv")
save_command_log_csv(sink, output_path)

print("Saved:", output_path)
print("Commands:", sink.count)
