import socket
import time
import numpy as np
import pyrealsense2 as rs
import json
import struct

HOST = "127.0.0.1"
PORT = 5000

#   Distance of camera to the floor
FLOOR_DISTANCE = 1.66

#   Distance of camera to the base of the SandCastle. Where sand is at 0
BASE_DISTANCE = 1#1.13

#   Average sand height if all sand in Sandcastle is flat
AVERAGE_SAND_HEIGHT = 0.095
AVERAGE_SAND_HEIGHT_TOTAL = BASE_DISTANCE + AVERAGE_SAND_HEIGHT

#   Peripheral Glass height
MAX_SAND_HEIGHT = 1#0.25

#   Multiply height for better visualization
HEIGHT_MULTIPLIER = 2.5

#   SET ROI DIMENSIONS

ROI_X_MIN = 70
ROI_Y_MIN = 20

ROI_X_MAX = 530
ROI_Y_MAX = 320

ROI_ROWS = ROI_Y_MAX - ROI_Y_MIN
ROI_COLS = ROI_X_MAX - ROI_X_MIN
#   Max and min values of the sand
MIN_DEPTH = BASE_DISTANCE - MAX_SAND_HEIGHT
MAX_DEPTH = BASE_DISTANCE

#   Physical Box Dimensions
PHYSICAL_BOX_DEPTH = 0.25
PHYSICAL_BOX_WIDTH = 1.097
PHYSICAL_BOX_LENGTH = 0.78
PHYSICAL_BOX_VOLUME = PHYSICAL_BOX_DEPTH * PHYSICAL_BOX_WIDTH * PHYSICAL_BOX_LENGTH * 1000

#   Dimensions to be used for the realsense depth.
CAMERA_PIXELS_ROWS = 720
CAMERA_PIXELS_COLS = 1280

DECIMATION_FACTOR = 2

UNITY_GRID_ROWS = CAMERA_PIXELS_ROWS // DECIMATION_FACTOR
UNITY_GRID_COLS = CAMERA_PIXELS_COLS // DECIMATION_FACTOR

# --------------------------------------------------
# TCP server
# --------------------------------------------------

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
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
    CAMERA_PIXELS_COLS,
    CAMERA_PIXELS_ROWS,
    rs.format.z16,
    30
)

profile = pipeline.start(config)

depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()

print(f"Depth scale: {depth_scale}")

# --------------------------------------------------
# RealSense filters
# --------------------------------------------------

decimation = rs.decimation_filter()

#   Changes dimension of the depth output. 2 bcz unity processes half the dimension
decimation.set_option(
    rs.option.filter_magnitude,
    2
)


depth_to_disparity = rs.disparity_transform(True)
disparity_to_depth = rs.disparity_transform(False)


spatial = rs.spatial_filter()

#   How many times the smoothing of the temporal filter will pass
spatial.set_option(
    rs.option.filter_magnitude,
    2
)

#   How strong the smoothing will be. 0.25 to 1 range, 0.25 strong smooth 1 no
spatial.set_option(
    rs.option.filter_smooth_alpha,
    0.5
)

#   Threshold of the difference for smoothing. Bigger threshold smooths bigger differences
spatial.set_option(
    rs.option.filter_smooth_delta,
    20
)


temporal = rs.temporal_filter()

#   How important are the previous values. filtered ≈ alpha * current + (1-alpha) * previous
#   Smaller a keeps previous values more
temporal.set_option(
    rs.option.filter_smooth_alpha,
    0.5
)

"""
    Threshold if we use or not temporal filtering or not depending on the
    difference of the new value and the last value (on this pixel): 
    
    diff = |cur_val - prev_val|
    diff < delta
    
    If this is true then use alpha and etc.
    
    This can be used with depth or with disparity of the camera. Disparity has
    big changes when we are near the camera and smaller changes when we are further
    away of the camera. So we will use temporal when we are further away from the
    camera and not when we are near.
    
    current distance Z
    focal length fx
    stereo baseline B
    
    
    D = 32 * f * B /Z
"""
temporal.set_option(
    rs.option.filter_smooth_delta,
    20
)

"""
    0	Disabled — δεν χρησιμοποιεί παλιότερη τιμή
    1	Valid in 8/8 previous frames
    2	Valid in 2/3 previous frames
    3	Valid in 2/4 previous frames
    4	Valid in 2/8 previous frames
    5	Valid in 1/2 previous frames
    6	Valid in 1/5 previous frames
    7	Valid in 1/8 previous frames
    8	Persist indefinitely
"""
temporal.set_option(
    rs.option.holes_fill,
    4
)


#   Fills holes in the depth due to noise
hole_filling = rs.hole_filling_filter(1)


# --------------------------------------------------
# Main loop
# --------------------------------------------------

#   Send Setup information
setup = {
    "type": "setup",
    "GRID_ROWS": ROI_ROWS,
    "GRID_COLS": ROI_COLS,
    "HEIGHT_MULTIPLIER": HEIGHT_MULTIPLIER
}

setup_bytes = json.dumps(setup).encode("utf-8")

# Send JSON size first
conn.sendall(
    struct.pack("<I", len(setup_bytes))
)

# Send JSON
conn.sendall(setup_bytes)

print("Setup sent:", setup)

try:
    while True:
        frame_start = time.perf_counter()

        frames = pipeline.wait_for_frames()

        depth_frame = frames.get_depth_frame()

        if not depth_frame:
            continue

        # ------------------------------------------
        # Filter pipeline
        # ------------------------------------------

        # 1280x720 -> 640x360
        filtered = decimation.process(depth_frame)

        #   Use disparity values for the processing
        filtered = depth_to_disparity.process(filtered)

        #   Smoothing the Surface.
        # filtered = spatial.process(filtered)

        #   Change the value based on past heights
        filtered = temporal.process(filtered)
        filtered = disparity_to_depth.process(filtered)

        #   Fill the holes. Should never not have it enabled as lot of holes!
        filtered = hole_filling.process(filtered)


        # ------------------------------------------
        # Convert depth frame to NumPy
        # ------------------------------------------

        raw_depth = np.asanyarray(
            filtered.get_data()
        )

        
        #   Raw Depths are unsigned int (0-65535). Need to multiply with depth_scale for meters
        depths = raw_depth.astype(np.float32)
        depths *= np.float32(depth_scale)
        
        depths = depths[
            ROI_Y_MIN:ROI_Y_MAX,
            ROI_X_MIN:ROI_X_MAX
        ]
        

        valid_mask = (
            (depths >= MIN_DEPTH) &
            (depths <= MAX_DEPTH)
        )

        heights = np.zeros_like(
            depths,
            dtype=np.float32
        )

        heights[valid_mask] = (
            (MAX_DEPTH - depths[valid_mask]) * HEIGHT_MULTIPLIER
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

finally:
    pipeline.stop()
    conn.close()
    server.close()