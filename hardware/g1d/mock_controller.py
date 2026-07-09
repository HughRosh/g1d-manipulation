#!/usr/bin/env python3

import time
import numpy as np


class MockG1DController:
    def __init__(self):
        self.arm_q = np.zeros(14)
        self.gripper_state = "open"
        print("Mock G1-D controller initialized")

    def current_arm(self):
        return self.arm_q.copy()

    def move_arm(self, q, seconds=3.0):
        self.arm_q = np.array(q, dtype=float)
        print(f"[MOCK] move_arm q={self.arm_q.tolist()} seconds={seconds}")
        time.sleep(0.1)

    def move_joint(self, joint_index, delta, seconds=3.0):
        q = self.current_arm()
        q[joint_index] += delta
        self.move_arm(q, seconds=seconds)

    def open_gripper(self):
        self.gripper_state = "open"
        print("[MOCK] open_gripper")

    def close_gripper(self):
        self.gripper_state = "closed"
        print("[MOCK] close_gripper")

    def home(self):
        self.arm_q[:] = 0.0
        print("[MOCK] home")
