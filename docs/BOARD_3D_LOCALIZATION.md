# Chess Board 3D Localization

The biggest perception problem is converting camera observations into robot/world coordinates.

The target flow is:

camera image
-> marker or board detection
-> board pose in camera frame
-> board pose in robot frame
-> square centers in 3D
-> pick/place waypoints

## Recommended first approach

Use ArUco markers on the chess board.

Place markers at known board locations, for example:

- a1 corner
- h1 corner
- a8 corner
- h8 corner

This allows the camera to estimate:

- board origin
- file direction
- rank direction
- square size
- board rotation

## Why not raw chessboard detection first?

Raw chessboard detection is possible, but for robot manipulation ArUco markers are easier to debug and more reliable at the start.

## Important frames

Camera frame:
Coordinates relative to the camera.

Robot frame:
Coordinates relative to the robot base or chosen world frame.

Board frame:
Coordinates relative to the board, where a1 is the origin.

The board calibration converts board squares like e2/e4 into robot-frame 3D points.
