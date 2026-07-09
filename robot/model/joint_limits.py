#!/usr/bin/env python3

from dataclasses import dataclass
from math import pi

from robot.model.joint_indices import JOINT_INDEX_TO_NAME


@dataclass(frozen=True)
class JointLimit:
    lower: float
    upper: float
    velocity: float | None = None
    effort: float | None = None


DEFAULT_SAFE_LIMIT = JointLimit(lower=-pi, upper=pi)

JOINT_LIMITS = {
    index: DEFAULT_SAFE_LIMIT for index in JOINT_INDEX_TO_NAME
}


def get_joint_limit(index: int) -> JointLimit:
    if index not in JOINT_LIMITS:
        raise KeyError(f"No G1-D joint limit registered for motor index {index}")
    return JOINT_LIMITS[index]


def clamp_joint(index: int, q: float) -> float:
    limit = get_joint_limit(index)
    return max(limit.lower, min(limit.upper, q))
