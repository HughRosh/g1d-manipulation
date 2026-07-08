import mujoco
import mujoco.viewer
from pathlib import Path

# For now this loads the robot URDF directly.
# Next step will be adding table/board through MuJoCo scene composition.
MODEL_PATH = Path("simulation/urdf/g1_d_with_dex1_1_hybrid.urdf")

def main():
    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)

    print(f"Loaded combined simulation base model: {MODEL_PATH}")
    print("Next step: add table and chessboard to this scene.")

    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            mujoco.mj_step(model, data)
            viewer.sync()

if __name__ == "__main__":
    main()
