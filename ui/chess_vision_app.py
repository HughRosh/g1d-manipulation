#!/usr/bin/env python3

from pathlib import Path
import shutil
import time

import cv2
import streamlit as st
from PIL import Image

from perception.detection.yolo_detector import YOLODetector


REPO_ROOT = Path(__file__).resolve().parents[1]
HEAD_FRAME_PATH = REPO_ROOT / "head_frame.jpg"
RAW_DATASET_DIR = REPO_ROOT / "datasets" / "chess_piece_color" / "raw"


st.set_page_config(
    page_title="G1-D Chess Vision",
    layout="wide",
)

st.title("G1-D Chess Vision UI")

st.write("Use this UI to inspect head camera frames, run YOLO, and save training images.")

RAW_DATASET_DIR.mkdir(parents=True, exist_ok=True)

col_left, col_right = st.columns(2)

with col_left:
    st.header("Camera Frame")

    if HEAD_FRAME_PATH.exists():
        image = Image.open(HEAD_FRAME_PATH)
        st.image(image, caption=str(HEAD_FRAME_PATH), use_container_width=True)
    else:
        st.warning("Missing head_frame.jpg. Copy a frame from the robot first.")

    if st.button("Save current frame to raw dataset"):
        if not HEAD_FRAME_PATH.exists():
            st.error("No head_frame.jpg found.")
        else:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_path = RAW_DATASET_DIR / f"head_{timestamp}.jpg"
            shutil.copyfile(HEAD_FRAME_PATH, output_path)
            st.success(f"Saved {output_path}")

with col_right:
    st.header("YOLO Detection")

    model_path = st.text_input("YOLO model path", value="yolo11n.pt")
    confidence = st.slider("Confidence", 0.0, 1.0, 0.25, 0.05)

    if st.button("Run YOLO"):
        if not HEAD_FRAME_PATH.exists():
            st.error("No head_frame.jpg found.")
        else:
            image_bgr = cv2.imread(str(HEAD_FRAME_PATH))

            detector = YOLODetector(
                model_path=model_path,
                confidence=confidence,
            )

            result = detector.detect(image_bgr)

            image_draw = image_bgr.copy()

            for detection in result.detections:
                x1, y1, x2, y2 = detection.xyxy

                cv2.rectangle(
                    image_draw,
                    (int(x1), int(y1)),
                    (int(x2), int(y2)),
                    (0, 255, 0),
                    2,
                )

                label = f"{detection.class_name} {detection.confidence:.2f}"

                cv2.putText(
                    image_draw,
                    label,
                    (int(x1), max(0, int(y1) - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )

            image_rgb = cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB)
            st.image(image_rgb, caption="YOLO detections", use_container_width=True)

            st.write(f"Detections: {result.count}")

            for detection in result.detections:
                st.write(
                    {
                        "class": detection.class_name,
                        "confidence": round(detection.confidence, 3),
                        "center_px": detection.center_px,
                        "box": detection.xyxy,
                    }
                )

st.header("Dataset")

raw_images = sorted(RAW_DATASET_DIR.glob("*.jpg"))

st.write(f"Raw training images: {len(raw_images)}")

if raw_images:
    latest = raw_images[-1]
    st.image(Image.open(latest), caption=f"Latest raw image: {latest.name}", use_container_width=True)
