#!/usr/bin/env python3

from pathlib import Path
import shutil
import time
import sys
import subprocess

import cv2
import streamlit as st
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from perception.camera.stereo_split import split_side_by_side_stereo
from perception.detection.yolo_detector import YOLODetector
from perception.detection.aruco_detector import ArucoDetector, draw_aruco_detections


HEAD_FRAME_PATH = REPO_ROOT / "head_frame.jpg"
RAW_DATASET_DIR = REPO_ROOT / "datasets" / "chess_piece_color" / "raw"
ARUCO_DIR = REPO_ROOT / "assets" / "aruco_markers"


st.set_page_config(
    page_title="G1-D Chess Vision",
    layout="wide",
)

st.title("G1-D Chess Vision UI")
st.write("Stereo camera viewer, YOLO test, ArUco marker detection, and dataset capture.")

RAW_DATASET_DIR.mkdir(parents=True, exist_ok=True)

st.sidebar.header("Robot")
robot_ip = st.sidebar.text_input("Robot IP", value="192.168.123.164")
robot_frame_path = st.sidebar.text_input("Robot frame path", value="/home/unitree/head_frame.jpg")

if st.sidebar.button("Capture latest saved frame from robot"):
    cmd = [
        "scp",
        f"unitree@{robot_ip}:{robot_frame_path}",
        str(HEAD_FRAME_PATH),
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        st.sidebar.success("Copied frame from robot")
    else:
        st.sidebar.error("Failed to copy frame")
        st.sidebar.code(result.stderr)

st.sidebar.header("Camera")
camera_view = st.sidebar.radio(
    "Image source",
    ["full_stereo", "left_head", "right_head"],
    index=2,
)

frame_bgr = None
display_bgr = None

if HEAD_FRAME_PATH.exists():
    frame_bgr = cv2.imread(str(HEAD_FRAME_PATH))

    if frame_bgr is not None:
        if camera_view == "full_stereo":
            display_bgr = frame_bgr
        else:
            left_bgr, right_bgr = split_side_by_side_stereo(frame_bgr)
            display_bgr = left_bgr if camera_view == "left_head" else right_bgr

col_left, col_right = st.columns(2)

with col_left:
    st.header("Camera Frame")

    if display_bgr is None:
        st.warning("Missing or unreadable head_frame.jpg")
    else:
        display_rgb = cv2.cvtColor(display_bgr, cv2.COLOR_BGR2RGB)
        st.image(display_rgb, caption=f"{camera_view}: {HEAD_FRAME_PATH}", use_container_width=True)

        st.write("Image shape:", display_bgr.shape)

    if st.button("Save selected view to raw dataset"):
        if display_bgr is None:
            st.error("No frame available")
        else:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_path = RAW_DATASET_DIR / f"{camera_view}_{timestamp}.jpg"
            cv2.imwrite(str(output_path), display_bgr)
            st.success(f"Saved {output_path}")

    st.header("ArUco Board Markers")
    marker_files = sorted(ARUCO_DIR.glob("*.png"))

    if marker_files:
        st.write("Print these and place them on the chessboard corners:")
        st.write("10 = a1 corner")
        st.write("11 = h1 corner")
        st.write("12 = a8 corner")
        st.write("13 = h8 corner")

        preview_cols = st.columns(4)
        for idx, marker_file in enumerate(marker_files):
            with preview_cols[idx % 4]:
                st.image(Image.open(marker_file), caption=marker_file.name, use_container_width=True)
    else:
        st.warning("No ArUco marker images found. Run scripts/make_aruco_board_markers.py")

with col_right:
    st.header("ArUco Detection")

    aruco_dictionary = st.text_input("ArUco dictionary", value="DICT_4X4_50")

    if st.button("Run ArUco"):
        if display_bgr is None:
            st.error("No frame available")
        else:
            detector = ArucoDetector(dictionary_name=aruco_dictionary)
            result = detector.detect(display_bgr)
            annotated = draw_aruco_detections(display_bgr, result)
            annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

            st.image(annotated_rgb, caption="ArUco detections", use_container_width=True)
            st.write("Detected marker count:", result.count)
            st.write("Detected IDs:", result.ids())

    st.header("YOLO Detection")

    model_path = st.text_input("YOLO model path", value="yolo11n.pt")
    confidence = st.slider("Confidence", 0.0, 1.0, 0.25, 0.05)

    if st.button("Run YOLO"):
        if display_bgr is None:
            st.error("No frame available")
        else:
            detector = YOLODetector(
                model_path=model_path,
                confidence=confidence,
            )

            result = detector.detect(display_bgr)
            image_draw = display_bgr.copy()

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

            st.write("Detections:", result.count)

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
