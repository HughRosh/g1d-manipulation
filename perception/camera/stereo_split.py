#!/usr/bin/env python3

import numpy as np


def split_side_by_side_stereo(frame: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if frame is None:
        raise ValueError("frame is None")

    height, width = frame.shape[:2]

    if width % 2 != 0:
        raise ValueError(f"Expected even stereo width, got {width}")

    mid = width // 2
    left = frame[:, :mid].copy()
    right = frame[:, mid:].copy()

    return left, right
