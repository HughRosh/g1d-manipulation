#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import time
import numpy as np
import mujoco
import mujoco.viewer

from src.utils import load_config
from scripts.create_chess_piece_scene import square_xy


MODEL_PATH = "simulation/mujoco/chess_piece_scene.xml"


def main():
    scene = load_config("configs/scene.yaml")["scene"]

    model = mujoco.MjModel.from_xml_path(MODEL_PATH)
    data = mujoco.MjData(model)

    joint_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "moving_piece_free")
    qadr = model.jnt_qposadr[joint_id]

    table = scene["table"]
    board = scene["board"]

    piece_z = table["height_m"] + board["thickness_m"] + 0.055 / 2.0

    start_x, start_y = square_xy("e2", scene)
    end_x, end_y = square_xy("e4", scene)

    print("Animating piece e2 -> e4")

    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            for alpha in np.linspace(0, 1, 160):
                x = (1 - alpha) * start_x + alpha * end_x
                y = (1 - alpha) * start_y + alpha * end_y

                lift = 0.08 * np.sin(np.pi * alpha)
                z = piece_z + lift

                data.qpos[qadr:qadr+7] = [x, y, z, 1, 0, 0, 0]

                mujoco.mj_forward(model, data)
                viewer.sync()
                time.sleep(0.015)

            while viewer.is_running():
                viewer.sync()
                time.sleep(0.03)


if __name__ == "__main__":
    main()
