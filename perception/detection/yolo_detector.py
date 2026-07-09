#!/usr/bin/env python3

from dataclasses import dataclass
import numpy as np
from ultralytics import YOLO


@dataclass(frozen=True)
class YOLODetection:
    class_id: int
    class_name: str
    confidence: float
    xyxy: tuple[float, float, float, float]

    @property
    def center_px(self) -> tuple[float, float]:
        x1, y1, x2, y2 = self.xyxy
        return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)


@dataclass(frozen=True)
class YOLODetectionResult:
    detections: list[YOLODetection]

    @property
    def count(self) -> int:
        return len(self.detections)


class YOLODetector:
    def __init__(self, model_path: str = "yolo11n.pt", confidence: float = 0.25):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, image: np.ndarray) -> YOLODetectionResult:
        results = self.model.predict(
            source=image,
            conf=self.confidence,
            verbose=False,
        )

        detections: list[YOLODetection] = []

        for result in results:
            names = result.names

            if result.boxes is None:
                continue

            for box in result.boxes:
                class_id = int(box.cls.item())
                confidence = float(box.conf.item())
                xyxy = tuple(float(v) for v in box.xyxy.cpu().numpy().reshape(-1))

                detections.append(
                    YOLODetection(
                        class_id=class_id,
                        class_name=names[class_id],
                        confidence=confidence,
                        xyxy=xyxy,
                    )
                )

        return YOLODetectionResult(detections=detections)
