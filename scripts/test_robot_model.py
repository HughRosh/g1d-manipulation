import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from robot.model import RobotModel
from src.utils import load_config


def main():
    config = load_config("configs/robot.yaml")
    robot = RobotModel(config["robot"]["urdf"])

    print(f"Robot name: {robot.robot_name()}")

    print("\nRight arm joints:")
    for joint in robot.right_arm_joints():
        print(joint)

    print("\nDex1/gripper joints:")
    for joint in robot.dex1_joints():
        print(joint)


if __name__ == "__main__":
    main()
