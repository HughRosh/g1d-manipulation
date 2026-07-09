#!/usr/bin/env python3

from controller import G1DController
import time


RIGHT_SHOULDER_PITCH = 7


def main():
    robot = G1DController(interface="eth0")

    print("Small right arm test")
    robot.move_joint(RIGHT_SHOULDER_PITCH, 0.10, seconds=3.0)
    robot.move_joint(RIGHT_SHOULDER_PITCH, -0.10, seconds=3.0)

    print("Gripper test")
    robot.open_gripper()
    time.sleep(2)
    robot.close_gripper()
    time.sleep(2)
    robot.open_gripper()
    time.sleep(2)

    print("Done")


if __name__ == "__main__":
    main()
