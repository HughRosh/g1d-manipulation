import time
from pathlib import Path

import mujoco
import mujoco.viewer

MODEL_PATH = Path("simulation/urdf/g1d_chess_static_scene.urdf")

def main():
    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)

    print(f"Loaded static scene: {MODEL_PATH}")
    print("Robot + table + chessboard + cup. Close viewer to exit.")

    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            viewer.sync()
            time.sleep(0.01)

if __name__ == "__main__":
    main()
