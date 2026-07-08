#!/usr/bin/env python3
import time
from multiprocessing import Value

from test_g1_dex1_internal import G1_29_Arm_Internal_Dex1_Controller
from unitree_sdk2py.core.channel import ChannelFactoryInitialize

def main():
    ChannelFactoryInitialize(0, "eth0")

    left = Value("d", 7.0, lock=True)
    right = Value("d", 7.0, lock=True)

    G1_29_Arm_Internal_Dex1_Controller(left, right)

    print("Opening grippers")
    left.value = 7.0
    right.value = 7.0
    time.sleep(2)

    print("Closing grippers")
    left.value = 5.37
    right.value = 5.37
    time.sleep(2)

    print("Opening grippers again")
    left.value = 7.0
    right.value = 7.0
    time.sleep(2)

    print("Done")

if __name__ == "__main__":
    main()
