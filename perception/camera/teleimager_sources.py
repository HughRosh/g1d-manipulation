#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass(frozen=True)
class TeleimagerStream:
    name: str
    webrtc_url: str
    port: int
    camera_type: str
    role: str


HEAD_BINOCULAR = TeleimagerStream(
    name="head_binocular",
    webrtc_url="https://192.168.123.164:60001",
    port=60001,
    camera_type="binocular",
    role="primary_board_localization",
)

LEFT_WRIST = TeleimagerStream(
    name="left_wrist",
    webrtc_url="https://192.168.123.164:60002",
    port=60002,
    camera_type="monocular",
    role="left_hand_close_up_verification",
)

RIGHT_WRIST = TeleimagerStream(
    name="right_wrist",
    webrtc_url="https://192.168.123.164:60003",
    port=60003,
    camera_type="monocular",
    role="right_hand_close_up_verification",
)

ALL_G1D_STREAMS = [
    HEAD_BINOCULAR,
    LEFT_WRIST,
    RIGHT_WRIST,
]
