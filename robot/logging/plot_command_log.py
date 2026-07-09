#!/usr/bin/env python3

from pathlib import Path
import matplotlib.pyplot as plt

from robot.commands.sinks import RecordingCommandSink


def plot_command_log(
    sink: RecordingCommandSink,
    output_path: str | Path,
    joint_indices: list[int],
    joint_names: dict[int, str] | None = None,
) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if sink.count == 0:
        raise ValueError("No commands recorded")

    q_log = sink.stacked_q_targets()
    steps = range(q_log.shape[0])

    plt.figure()

    for index in joint_indices:
        label = joint_names[index] if joint_names and index in joint_names else f"q_{index}"
        plt.plot(steps, q_log[:, index], label=label)

    plt.xlabel("Step")
    plt.ylabel("Joint position target [rad]")
    plt.title("Commanded Joint Trajectory")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
