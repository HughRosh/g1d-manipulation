import mujoco
import mujoco.viewer
from pathlib import Path

MODEL_PATH = Path("simulation/mujoco/table_scene.xml")

def main():
    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)

    print(f"Loaded table scene: {MODEL_PATH}")

    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            mujoco.mj_step(model, data)
            viewer.sync()

if __name__ == "__main__":
    main()
