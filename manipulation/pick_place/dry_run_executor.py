from dataclasses import dataclass
from typing import Tuple


@dataclass
class PickPlaceCommand:
    pick_xyz: Tuple[float, float, float]
    place_xyz: Tuple[float, float, float]
    approach_height_m: float


class DryRunPickPlaceExecutor:
    def execute(self, cmd: PickPlaceCommand):
        px, py, pz = cmd.pick_xyz
        qx, qy, qz = cmd.place_xyz
        ah = cmd.approach_height_m

        print()
        print("DRY RUN PICK AND PLACE")
        print("======================")
        print(f"1. Move home")
        print(f"2. Move above pick:  ({px:.3f}, {py:.3f}, {pz + ah:.3f})")
        print(f"3. Descend to pick:  ({px:.3f}, {py:.3f}, {pz:.3f})")
        print(f"4. Close gripper")
        print(f"5. Lift object:      ({px:.3f}, {py:.3f}, {pz + ah:.3f})")
        print(f"6. Move above place: ({qx:.3f}, {qy:.3f}, {qz + ah:.3f})")
        print(f"7. Descend to place: ({qx:.3f}, {qy:.3f}, {qz:.3f})")
        print(f"8. Open gripper")
        print(f"9. Lift and return home")
        print()
