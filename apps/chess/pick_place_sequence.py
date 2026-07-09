#!/usr/bin/env python3

from manipulation.planning.task_sequence import (
    ManipulationTaskSequence,
    ManipulationWaypoint,
)
from apps.chess.task_builder import PickPlaceTask


def chess_pick_place_to_sequence(task: PickPlaceTask) -> ManipulationTaskSequence:
    return ManipulationTaskSequence(
        waypoints=[
            ManipulationWaypoint(
                name=f"approach_{task.source_square}",
                position=task.source_approach,
                gripper_closed=False,
            ),
            ManipulationWaypoint(
                name=f"pick_{task.source_square}",
                position=task.source_pick,
                gripper_closed=False,
            ),
            ManipulationWaypoint(
                name=f"grasp_{task.source_square}",
                position=task.source_pick,
                gripper_closed=True,
            ),
            ManipulationWaypoint(
                name=f"lift_{task.source_square}",
                position=task.source_approach,
                gripper_closed=True,
            ),
            ManipulationWaypoint(
                name=f"approach_{task.target_square}",
                position=task.target_approach,
                gripper_closed=True,
            ),
            ManipulationWaypoint(
                name=f"place_{task.target_square}",
                position=task.target_place,
                gripper_closed=True,
            ),
            ManipulationWaypoint(
                name=f"release_{task.target_square}",
                position=task.target_place,
                gripper_closed=False,
            ),
            ManipulationWaypoint(
                name=f"retract_{task.target_square}",
                position=task.target_approach,
                gripper_closed=False,
            ),
        ]
    )
