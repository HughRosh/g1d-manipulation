from dataclasses import dataclass
from typing import List, Optional, Tuple

import cv2
import numpy as np
from ultralytics import YOLO


@dataclass
class PickDetection:
    label: str
    conf: float
    xyxy: Tuple[float, float, float, float]
    center_px: Tuple[float, float]


class YoloPickDetector:
    def __init__(self, model_path: str, confidence: float = 0.35):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame: np.ndarray) -> List[PickDetection]:
        result = self.model.predict(frame, conf=self.confidence, verbose=False)[0]
        names = result.names
        detections: List[PickDetection] = []

        for box in result.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = names[cls_id]
            x1, y1, x2, y2 = [float(v) for v in box.xyxy[0]]
            cx = (x1 + x2) / 2.0
            cy = (y1 + y2) / 2.0

            detections.append(
                PickDetection(
                    label=label,
                    conf=conf,
                    xyxy=(x1, y1, x2, y2),
                    center_px=(cx, cy),
                )
            )

        return detections

    @staticmethod
    def choose_best(detections: List[PickDetection]) -> Optional[PickDetection]:
        if not detections:
            return None
        return max(detections, key=lambda d: d.conf)

    @staticmethod
    def draw(frame: np.ndarray, detections: List[PickDetection], selected: Optional[PickDetection] = None):
        debug = frame.copy()

        for d in detections:
            x1, y1, x2, y2 = [int(v) for v in d.xyxy]
            cx, cy = [int(v) for v in d.center_px]

            is_selected = selected is not None and d == selected
            thickness = 4 if is_selected else 2

            cv2.rectangle(debug, (x1, y1), (x2, y2), (0, 255, 0), thickness)
            cv2.circle(debug, (cx, cy), 6, (0, 0, 255), -1)

            cv2.putText(
                debug,
                f"{d.label} {d.conf:.2f}",
                (x1, max(25, y1 - 8)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

        return debug
