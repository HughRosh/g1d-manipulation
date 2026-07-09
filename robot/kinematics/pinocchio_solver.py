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

        self.right_arm_joint_names = [
            "right_shoulder_pitch_joint",
            "right_shoulder_roll_joint",
            "right_shoulder_yaw_joint",
            "right_elbow_joint",
            "right_wrist_roll_joint",
            "right_wrist_pitch_joint",
            "right_wrist_yaw_joint",
        ]

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

    def solve_position_ik(self, target_xyz, q0=None, max_iters=200, tol=1e-3):
        """
        Position-only IK for the right Dex1.1 base frame.

        This solves XYZ first. Orientation/top-down will be added next.
        """

        q = self.neutral_q() if q0 is None else q0.copy()
        target = np.asarray(target_xyz, dtype=float)

        damping = 1e-4
        step_scale = 0.5

        for i in range(max_iters):
            pin.forwardKinematics(self.model, self.data, q)
            pin.updateFramePlacements(self.model, self.data)

            current = self.data.oMf[self.ee_frame_id].translation
            error = target - current

            if np.linalg.norm(error) < tol:
                return q, True, i, np.linalg.norm(error)

            J6 = pin.computeFrameJacobian(
                self.model,
                self.data,
                q,
                self.ee_frame_id,
                pin.ReferenceFrame.LOCAL_WORLD_ALIGNED,
            )

            J = J6[:3, :]

            dq = J.T @ np.linalg.solve(
                J @ J.T + damping * np.eye(3),
                error,
            )

            q = pin.integrate(self.model, q, step_scale * dq)

        return q, False, max_iters, np.linalg.norm(error)
