#!/usr/bin/env python3

import cv2


class AprilTagDetector:
    def __init__(self):
        if not hasattr(cv2, "aruco"):
            raise RuntimeError(
                "cv2.aruco not available. Install opencv-contrib-python."
            )

        self.dictionary = cv2.aruco.getPredefinedDictionary(
            cv2.aruco.DICT_APRILTAG_36h11
        )

        self.parameters = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(
            self.dictionary,
            self.parameters,
        )

    def detect(self, frame):
        corners, ids, rejected = self.detector.detectMarkers(frame)

        results = []

        if ids is None:
            return results

        for tag_id, tag_corners in zip(ids.flatten(), corners):
            results.append(
                {
                    "id": int(tag_id),
                    "corners": tag_corners.reshape(-1, 2).tolist(),
                }
            )

        return results
