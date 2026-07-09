#!/usr/bin/env python3

from dataclasses import dataclass

from apps.chess.board_geometry import ChessBoardGeometry, Point3D
from apps.chess.move import ChessMove


@dataclass(frozen=True)
class PickPlaceTask:
    source_square: str
    target_square: str
    source_approach: Point3D
    source_pick: Point3D
    target_approach: Point3D
    target_place: Point3D


def build_pick_place_task(
    move: ChessMove,
    board: ChessBoardGeometry,
) -> PickPlaceTask:
    return PickPlaceTask(
        source_square=move.source,
        target_square=move.target,
        source_approach=board.approach_point(move.source),
        source_pick=board.pick_point(move.source),
        target_approach=board.approach_point(move.target),
        target_place=board.pick_point(move.target),
    )
