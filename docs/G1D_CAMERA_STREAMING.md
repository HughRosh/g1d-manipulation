# G1-D Camera Streaming

The G1-D camera service captures video streams from multiple cameras and publishes them over the network.

## Supported Camera Sources

- UVC cameras
- OpenCV cameras
- Intel RealSense cameras

## Streaming Modes

- ZeroMQ PUB-SUB
- WebRTC
- Future: local shared-memory frame access

## Configuration

The image service supports:

- physical path camera identification
- serial number camera identification
- video device path identification
- configurable resolution
- configurable frame rate
- ZeroMQ REQ-REP image configuration commands
- triple ring buffer frame processing

## ZMQ Client Usage

Connect the robot and computer with Ethernet.

Set the computer static IP to:

```text
192.168.123.22
EOS
