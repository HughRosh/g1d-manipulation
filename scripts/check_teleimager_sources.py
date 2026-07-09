#!/usr/bin/env python3

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from perception.camera.teleimager_sources import ALL_G1D_STREAMS

for stream in ALL_G1D_STREAMS:
    print(stream.name)
    print("  type:", stream.camera_type)
    print("  url:", stream.webrtc_url)
    print("  role:", stream.role)
