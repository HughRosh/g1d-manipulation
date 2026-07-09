#!/usr/bin/env python3

from pathlib import Path
import csv

from robot.commands.sinks import RecordingCommandSink


def save_command_log_csv(
    sink: RecordingCommandSink,
    output_path: str | Path,
) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if sink.count == 0:
        raise ValueError("No commands recorded")

    q_log = sink.stacked_q_targets()

    with output_path.open("w", newline="") as f:
        writer = csv.writer(f)

        header = ["step"] + [f"q_{i}" for i in range(q_log.shape[1])]
        writer.writerow(header)

        for step_index, q in enumerate(q_log):
            writer.writerow([step_index] + list(q))
