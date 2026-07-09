#!/usr/bin/env python3

from dataclasses import dataclass
from abc import ABC, abstractmethod

from perception.localization.board_calibration import BoardCalibration
from apps.chess.board_geometry import Point3D, Vector3D


@dataclass(frozen=True)
class CameraIntrinsics:
    fx: float
    fy: float
    cx: float
    cy: float


@dataclass(frozen=True)
class CameraExtrinsics:
    camera_position_in_robot: Point3D
    camera_x_axis_in_robot: Vector3D
    camera_y_axis_in_robot: Vector3D
    camera_z_axis_in_robot: Vector3D


@dataclass(frozen=True)
class BoardPoseEstimate:
    calibration: BoardCalibration
    confidence: float
    method: str


class BoardPoseEstimator(ABC):
    @abstractmethod
    def estimate(self, image) -> BoardPoseEstimate:
        raise NotImplementedError


class ManualBoardPoseEstimator(BoardPoseEstimator):
    def estimate(self, image=None) -> BoardPoseEstimate:
        calibration = BoardCalibration(
            origin_a1=Point3D(x=0.30, y=-0.20, z=0.00),
            file_direction=Vector3D(x=1.0, y=0.0, z=0.0),
            rank_direction=Vector3D(x=0.0, y=1.0, z=0.0),
            square_size=0.05,
        )

        return BoardPoseEstimate(
            calibration=calibration,
            confidence=1.0,
            method="manual",
        )
