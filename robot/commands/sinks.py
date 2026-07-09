#!/usr/bin/env python3

from dataclasses import dataclass, field
import numpy as np

from robot.commands.low_command import LowCommand


@dataclass
class RecordedCommand:
    q_target: np.ndarray
    dq_target: np.ndarray
    kp: np.ndarray
    kd: np.ndarray
    tau_ff: np.ndarray


@dataclass
class RecordingCommandSink:
    commands: list[RecordedCommand] = field(default_factory=list)

    def send(self, command: LowCommand) -> None:
        self.commands.append(
            RecordedCommand(
                q_target=command.q_target.copy(),
                dq_target=command.dq_target.copy(),
                kp=command.kp.copy(),
                kd=command.kd.copy(),
                tau_ff=command.tau_ff.copy(),
            )
        )

    def clear(self) -> None:
        self.commands.clear()

    @property
    def count(self) -> int:
        return len(self.commands)

    def stacked_q_targets(self) -> np.ndarray:
        if not self.commands:
            return np.empty((0, 0))

        return np.stack([cmd.q_target for cmd in self.commands], axis=0)
