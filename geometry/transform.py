#!/usr/bin/env python3

from dataclasses import dataclass
import numpy as np


@dataclass
class Transform:
    translation: np.ndarray
    quaternion: np.ndarray

    @staticmethod
    def identity():
        return Transform(
            np.zeros(3),
            np.array([0.0, 0.0, 0.0, 1.0]),
        )

    def as_matrix(self):
        T = np.eye(4)
        T[:3, 3] = self.translation
        return T
