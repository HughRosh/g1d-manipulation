#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Protocol
import time

from manipulation.planning.joint_trajectory import JointTrajectory
from manipulation.safety.trajectory_safety import require_safe_trajectory
from robot.commands.builders import command_from_current_position
from robot.commands.low_command import LowCommand


class CommandSink(Protocol):
    def send(self, command: LowCommand) -> None:
        ...


@dataclass
class PrintCommandSink:
    every_n_steps: int = 10

    def send(self, command: LowCommand) -> None:
        print(
            "send command | "
            f"q[15]={command.q_target[15]: .3f} "
            f"q[22]={command.q_target[22]: .3f}"
        )


@dataclass
class TrajectoryExecutor:
    command_sink: CommandSink
    realtime: bool = False
    safety_enabled: bool = True
    max_step_delta: float = 0.08

    def execute(self, trajectory: JointTrajectory) -> None:
        if self.safety_enabled:
            require_safe_trajectory(
                trajectory=trajectory,
                max_step_delta=self.max_step_delta,
            )

        for q in trajectory.positions:
            command = command_from_current_position(q)
            self.command_sink.send(command)

            if self.realtime:
                time.sleep(trajectory.dt)
