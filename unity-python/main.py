
import socket
import time
import json
import struct

import numpy as np

from camera import Camera
from config import NetworkConfig, CameraConfig, SandmapConfig


network = NetworkConfig()
camera_config = CameraConfig()
sandmap = SandmapConfig()

camera = Camera(camera_config)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = None

try:
    server.bind((network.HOST, network.PORT))
    server.listen()

    print("Waiting for Unity...")

    conn, addr = server.accept()
    print("Unity connected:", addr)

    # ------------------------------------------
    # Start RealSense
    # ------------------------------------------

    camera.start()

    # ------------------------------------------
    # Send Setup Information
    # ------------------------------------------

    setup = {
        "type": "setup",
        "GRID_ROWS": camera_config.ROI_ROWS,
        "GRID_COLS": camera_config.ROI_COLS,
        "HEIGHT_MULTIPLIER": sandmap.HEIGHT_MULTIPLIER
    }

    setup_bytes = json.dumps(setup).encode("utf-8")

    conn.sendall(struct.pack("<I", len(setup_bytes)))
    conn.sendall(setup_bytes)

    print("Setup sent:", setup)

    # ------------------------------------------
    # Main Loop
    # ------------------------------------------

    while True:
        frame_start = time.perf_counter()
        depths = camera.get_depths()

        if depths is None:
            continue

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

finally:
    camera.stop()

    if conn is not None:
        conn.close()

    server.close()