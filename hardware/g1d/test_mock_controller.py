#!/usr/bin/env python3

from mock_controller import MockG1DController
import time

RIGHT_SHOULDER_PITCH = 7


def main():
    robot = MockG1DController()

    robot.move_joint(RIGHT_SHOULDER_PITCH, 0.10, seconds=3.0)
    robot.move_joint(RIGHT_SHOULDER_PITCH, -0.10, seconds=3.0)

    robot.open_gripper()
    time.sleep(0.5)
    robot.close_gripper()
    time.sleep(0.5)
    robot.open_gripper()

    robot.home()

    print("Mock controller test complete")


if __name__ == "__main__":
    main()
