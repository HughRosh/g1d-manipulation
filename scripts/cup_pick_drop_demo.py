import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from utils import load_config
from robot_controller import execute_motion


def make_cup_pick_drop_motion(config):
    cup_x, cup_y, _ = config["cup"]["position_xyz_m"]
    drop_x, drop_y, _ = config["drop_zone"]["position_xyz_m"]

    approach_z = config["cup"]["approach_z_m"]
    grasp_z = config["cup"]["grasp_z_m"]
    release_z = config["drop_zone"]["release_z_m"]

    return [
        {"action": "move", "target": [cup_x, cup_y, approach_z]},
        {"action": "gripper", "state": "open"},
        {"action": "move", "target": [cup_x, cup_y, grasp_z]},
        {"action": "gripper", "state": "close"},
        {"action": "move", "target": [cup_x, cup_y, approach_z]},
        {"action": "move", "target": [drop_x, drop_y, release_z]},
        {"action": "gripper", "state": "open"},
        {"action": "move", "target": [drop_x, drop_y, approach_z]},
    ]


def main():
    config = load_config("configs/cup_demo.yaml")
    motion = make_cup_pick_drop_motion(config)

    print("Cup pick/drop demo")
    for step in motion:
        print(step)

    execute_motion(motion, dry_run=True)


if __name__ == "__main__":
    main()
