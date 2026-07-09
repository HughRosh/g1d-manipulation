# G1-D Teleimager Camera Interface

The G1-D streams camera video through Teleimager.

## Camera streams

- Head binocular camera: `https://192.168.123.164:60001`
- Left wrist monocular camera: `https://192.168.123.164:60002`
- Right wrist monocular camera: `https://192.168.123.164:60003`

## Recommended chess usage

Use the head binocular camera for primary board localization.

Use the wrist cameras for:

- close-up correction
- checking gripper alignment
- verifying piece pickup
- verifying piece placement

## ZMQ usage

Connect robot and computer over Ethernet.

Set the computer static IP to:

`192.168.123.22`

On the G1-D PC2, the default conda environment is:

`tv`

The `tv` environment already has Teleimager components installed.

Run the Teleimager image client from the Teleimager repository:

`python src/teleimager/image_client.py`

## WebRTC usage

Open one of these in a browser:

`https://192.168.123.164:60001`

`https://192.168.123.164:60002`

`https://192.168.123.164:60003`

Then click the start button at the top of the page.

## Chess localization plan

First version:

head camera image
-> ArUco marker detection
-> solvePnP board pose estimate
-> camera frame to robot frame transform
-> board square centers in robot frame

Later version:

head binocular camera
-> stereo depth / disparity
-> board pose refinement
-> wrist camera final correction
