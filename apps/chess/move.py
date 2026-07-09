#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass(frozen=True)
class ChessMove:
    source: str
    target: str

    @classmethod
    def from_uci(cls, uci: str) -> "ChessMove":
        if len(uci) < 4:
            raise ValueError(f"Invalid UCI move: {uci}")

        return cls(
            source=uci[0:2],
            target=uci[2:4],
        )
