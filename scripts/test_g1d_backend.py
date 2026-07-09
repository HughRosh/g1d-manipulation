#!/usr/bin/env python3

import argparse
import time
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from hardware.g1d.factory import make_g1d_controller

RIGHT_SHOULDER_PITCH = 7


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", default="mock", choices=["mock", "real"])
    parser.add_argument("--interface", default="eth0")
    args = parser.parse_args()

    robot = make_g1d_controller(
        backend=args.backend,
        interface=args.interface,
    )

    robot.move_joint(RIGHT_SHOULDER_PITCH, 0.10, seconds=1.0)
    robot.move_joint(RIGHT_SHOULDER_PITCH, -0.10, seconds=1.0)

    robot.open_gripper()
    time.sleep(0.5)
    robot.close_gripper()
    time.sleep(0.5)
    robot.open_gripper()

    print("Backend test complete")


if __name__ == "__main__":
    main()
