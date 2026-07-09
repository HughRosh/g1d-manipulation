#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from planning.kinematics import make_top_down_pose, placeholder_ik


def main():
    pose = make_top_down_pose(0.50, -0.25, 0.90)
    print("Target pose:")
    print(pose.as_dict())

    q = placeholder_ik(pose)
    print("Placeholder IK output:")
    print(q)


if __name__ == "__main__":
    main()
