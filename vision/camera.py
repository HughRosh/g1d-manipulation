#!/usr/bin/env python3

import cv2


class Camera:
    def __init__(self, index=0):
        self.index = index
        self.cap = cv2.VideoCapture(index)

        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open camera index {index}")

    def read(self):
        ok, frame = self.cap.read()
        if not ok:
            raise RuntimeError("Failed to read camera frame")
        return frame

    def release(self):
        self.cap.release()
