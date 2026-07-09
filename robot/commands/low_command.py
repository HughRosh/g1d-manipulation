#!/usr/bin/env python3

from dataclasses import dataclass, field
import numpy as np

from robot.model.joint_indices import G1D_NUM_MOTOR
from robot.model.gains import KP, KD


@dataclass
class LowCommand:
    q_target: np.ndarray = field(default_factory=lambda: np.zeros(G1D_NUM_MOTOR))
    dq_target: np.ndarray = field(default_factory=lambda: np.zeros(G1D_NUM_MOTOR))
    kp: np.ndarray = field(default_factory=lambda: np.array(KP, dtype=float))
    kd: np.ndarray = field(default_factory=lambda: np.array(KD, dtype=float))
    tau_ff: np.ndarray = field(default_factory=lambda: np.zeros(G1D_NUM_MOTOR))

    def copy(self) -> "LowCommand":
        return LowCommand(
            q_target=self.q_target.copy(),
            dq_target=self.dq_target.copy(),
            kp=self.kp.copy(),
            kd=self.kd.copy(),
            tau_ff=self.tau_ff.copy(),
        )
