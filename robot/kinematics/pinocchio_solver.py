#!/usr/bin/env python3

from pathlib import Path
import numpy as np
import pinocchio as pin


class G1DKinematics:
    def __init__(self, end_effector_frame="right_dex1_base_link"):
        urdf = Path("simulation/urdf/g1_d_with_dex1_1_hybrid.urdf")

        self.model = pin.buildModelFromUrdf(str(urdf))
        self.data = self.model.createData()

        self.ee_frame_name = end_effector_frame
        self.ee_frame_id = self.model.getFrameId(self.ee_frame_name)

        print()
        print("Loaded URDF")
        print("Number of joints:", self.model.njoints)
        print("Number of frames:", self.model.nframes)
        print("End effector frame:", self.ee_frame_name)
        print("End effector frame id:", self.ee_frame_id)

    def neutral_q(self):
        return pin.neutral(self.model)

    def forward_kinematics(self, q=None):
        if q is None:
            q = self.neutral_q()

        pin.forwardKinematics(self.model, self.data, q)
        pin.updateFramePlacements(self.model, self.data)

        placement = self.data.oMf[self.ee_frame_id]

        return {
            "position_xyz": placement.translation.tolist(),
            "rotation_matrix": placement.rotation.tolist(),
        }
