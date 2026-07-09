# YOLO Chess Piece Color Training

First training target:

- white_piece
- black_piece

This is easier and more useful at the start than full piece classification.

The chess engine already tracks the actual piece type from game state. The camera mainly needs to confirm:

- which squares are occupied
- whether the detected piece is white or black
- whether a pick/place succeeded

## Dataset layout

datasets/chess_piece_color/
  data.yaml
  images/train/
  images/val/
  labels/train/
  labels/val/

## YOLO label format

Each label file has one row per detected object:

class_id x_center y_center width height

All coordinates are normalized from 0 to 1.

Class IDs:

0 = white_piece
1 = black_piece

## Training command

python -m ultralytics train model=yolo11n.pt data=datasets/chess_piece_color/data.yaml epochs=50 imgsz=640

## Recommended first dataset

Capture head-camera images from the G1-D with:

- board in different positions
- board rotated slightly
- different lighting
- pieces on many different squares
- partial occlusions from the robot arm
- both white and black pieces

Start with 100-300 labeled images.
