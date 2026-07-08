#!/usr/bin/env python3
import sys
import time
import numpy as np
from multiprocessing import Value

sys.path.append("/home/unitree")

from test_g1_dex1_internal import G1_29_Arm_Internal_Dex1_Controller
from unitree_sdk2py.core.channel import ChannelFactoryInitialize

def main():
    ChannelFactoryInitialize(0, "eth0")

    left = Value("d", 0.0, lock=True)
    right = Value("d", 0.0, lock=True)

    ctrl = G1_29_Arm_Internal_Dex1_Controller(left, right)

    q0 = ctrl.get_current_dual_arm_q()
    print("Current arm q:", q0)

    q1 = q0.copy()
    q1[7] += 0.10

    print("Moving right shoulder pitch +0.10 rad")
    for _ in range(300):
        ctrl.ctrl_dual_arm(q1, np.zeros(14))
        time.sleep(0.01)

    print("Returning to start")
    for _ in range(300):
        ctrl.ctrl_dual_arm(q0, np.zeros(14))
        time.sleep(0.01)

    print("Done")

if __name__ == "__main__":
    main()
