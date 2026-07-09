#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Protocol
import time
import numpy as np

from manipulation.planning.joint_trajectory import JointTrajectory
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

    def execute(self, trajectory: JointTrajectory) -> None:
        for step_index, q in enumerate(trajectory.positions):
            command = command_from_current_position(q)
            self.command_sink.send(command)

            if self.realtime:
                time.sleep(trajectory.dt)
