#!/usr/bin/env python3

import argparse
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from hardware.g1d.factory import make_g1d_controller
from src.utils import load_config


RIGHT_SHOULDER_PITCH = 7


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", default="mock", choices=["mock", "real"])
    parser.add_argument("--interface", default="eth0")
    args = parser.parse_args()

    scene = load_config("configs/scene.yaml")["scene"]
    cup = scene["cup"]
    table = scene["table"]

    print("Cup demo using backend:", args.backend)
    print("Cup:", cup)
    print("Table height:", table["height_m"])

    robot = make_g1d_controller(
        backend=args.backend,
        interface=args.interface,
    )

    print("Demo motion: small arm move + gripper cycle")
    robot.move_joint(RIGHT_SHOULDER_PITCH, 0.10, seconds=1.0)

    robot.open_gripper()
    time.sleep(0.5)
    robot.close_gripper()
    time.sleep(0.5)
    robot.open_gripper()

    robot.move_joint(RIGHT_SHOULDER_PITCH, -0.10, seconds=1.0)

    print("Cup backend demo complete")


if __name__ == "__main__":
    main()
