
import socket
import time
import json
import struct

import numpy as np
import pyrealsense2 as rs

from camera_filters import CameraFilters
from config import NetworkConfig, CameraConfig, SandmapConfig


# --------------------------------------------------
# Configuration
# --------------------------------------------------

network = NetworkConfig()
camera = CameraConfig()
sandmap = SandmapConfig()


# --------------------------------------------------
# TCP Server
# --------------------------------------------------

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((network.HOST, network.PORT))
server.listen()

print("Waiting for Unity...")

conn, addr = server.accept()

print("Unity connected:", addr)


# --------------------------------------------------
# RealSense
# --------------------------------------------------

pipeline = rs.pipeline()
config = rs.config()

config.enable_stream(
    rs.stream.depth,
    camera.PIXELS_COLS,
    camera.PIXELS_ROWS,
    rs.format.z16,
    camera.FPS
)

try:
    profile = pipeline.start(config)

    depth_sensor = profile.get_device().first_depth_sensor()
    depth_scale = depth_sensor.get_depth_scale()

    print(f"Depth scale: {depth_scale}")

    filters = CameraFilters()

    # --------------------------------------------------
    # Send Setup Information
    # --------------------------------------------------

    setup = {
        "type": "setup",
        "GRID_ROWS": camera.ROI_ROWS,
        "GRID_COLS": camera.ROI_COLS,
        "HEIGHT_MULTIPLIER": sandmap.HEIGHT_MULTIPLIER
    }

    setup_bytes = json.dumps(setup).encode("utf-8")

    # Send JSON size first
    conn.sendall(
        struct.pack("<I", len(setup_bytes))
    )

    # Send JSON
    conn.sendall(setup_bytes)

    print("Setup sent:", setup)

    # --------------------------------------------------
    # Main Loop
    # --------------------------------------------------

    while True:
        frame_start = time.perf_counter()

        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()

        if not depth_frame:
            continue

        # ------------------------------------------
        # Filter Pipeline
        # ------------------------------------------

        # Reduce resolution from 1280x720 to 640x360
        filtered = filters.decimation.process(depth_frame)

        # Convert depth values to disparity
        filtered = filters.depth_to_disparity.process(filtered)

        # Smooth the depth surface
        # filtered = filters.spatial.process(filtered)

        # Apply temporal smoothing using previous frames
        filtered = filters.temporal.process(filtered)

        # Convert disparity back to depth
        filtered = filters.disparity_to_depth.process(filtered)

        # Fill missing depth pixels
        filtered = filters.hole_filling.process(filtered)

        # ------------------------------------------
        # Convert Depth Frame to NumPy
        # ------------------------------------------

        raw_depth = np.asanyarray(
            filtered.get_data()
        )

        # Convert raw depth values to meters
        depths = raw_depth.astype(np.float32)
        depths *= np.float32(depth_scale)

        # Extract Region of Interest
        depths = depths[
            camera.ROI_Y_MIN:camera.ROI_Y_MAX,
            camera.ROI_X_MIN:camera.ROI_X_MAX
        ]

        # ------------------------------------------
        # Calculate Heights
        # ------------------------------------------

        valid_mask = (
            (depths > 0) &
            (depths >= sandmap.MIN_DEPTH) &
            (depths <= sandmap.MAX_DEPTH)
        )

        heights = np.zeros_like(
            depths,
            dtype=np.float32
        )

        heights[valid_mask] = (
            (sandmap.MAX_DEPTH - depths[valid_mask])
            * sandmap.HEIGHT_MULTIPLIER
        )

        # ------------------------------------------
        # Send to Unity
        # ------------------------------------------

        conversion_start = time.perf_counter()

        data = heights.tobytes(order="C")

        conversion_end = time.perf_counter()

        send_start = time.perf_counter()

        conn.sendall(data)

        send_end = time.perf_counter()
        total_end = time.perf_counter()

        print(
            f"Shape: {heights.shape} | "
            f"Size: {len(data) / 1024 / 1024:.2f} MiB | "
            f"ToBytes: {(conversion_end - conversion_start) * 1000:.2f} ms | "
            f"Send: {(send_end - send_start) * 1000:.2f} ms | "
            f"Total: {(total_end - frame_start) * 1000:.2f} ms"
        )

except KeyboardInterrupt:
    print("Stopping server...")

pipeline_started = False

try:
    profile = pipeline.start(config)
    pipeline_started = True

    # Rest of your code

finally:
    if pipeline_started:
        pipeline.stop()

    conn.close()
    server.close()
