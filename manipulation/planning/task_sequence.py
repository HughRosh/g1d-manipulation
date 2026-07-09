#!/usr/bin/env python3

from dataclasses import dataclass

from apps.chess.board_geometry import Point3D


@dataclass(frozen=True)
class ManipulationWaypoint:
    name: str
    position: Point3D
    gripper_closed: bool


@dataclass(frozen=True)
class ManipulationTaskSequence:
    waypoints: list[ManipulationWaypoint]

    def __len__(self) -> int:
        return len(self.waypoints)

    def names(self) -> list[str]:
        return [waypoint.name for waypoint in self.waypoints]
