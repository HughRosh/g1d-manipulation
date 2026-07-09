#!/usr/bin/env python3

from pathlib import Path
import pinocchio as pin


class G1DKinematics:
    def __init__(self):
        urdf = Path("simulation/urdf/g1_d_with_dex1_1_hybrid.urdf")

        self.model = pin.buildModelFromUrdf(str(urdf))
        self.data = self.model.createData()

        print()
        print("Loaded URDF")
        print("Number of joints:", self.model.njoints)
        print("Number of frames:", self.model.nframes)
