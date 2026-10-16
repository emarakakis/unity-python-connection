
import numpy as np
import pyrealsense2 as rs

from camera_filters import CameraFilters
from config import CameraConfig


class Camera:
    def __init__(self, config: CameraConfig | None = None):
        self.config = config or CameraConfig()
        self.filters = CameraFilters()

        self.pipeline = rs.pipeline()
        self.rs_config = rs.config()

        self.rs_config.enable_stream(
            rs.stream.depth,
            self.config.PIXELS_COLS,
            self.config.PIXELS_ROWS,
            rs.format.z16,
            self.config.FPS
        )

        self.depth_scale = None
        self.started = False

    def start(self):
        profile = self.pipeline.start(self.rs_config)
        self.started = True

        depth_sensor = profile.get_device().first_depth_sensor()
        self.depth_scale = depth_sensor.get_depth_scale()

        print(f"Depth scale: {self.depth_scale}")

    def get_depths(self) -> np.ndarray | None:
        if not self.started:
            raise RuntimeError("Camera has not been started")

        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()

        if not depth_frame:
            return None

        # Reduce depth frame resolution
        filtered = self.filters.decimation.process(depth_frame)

        # Convert depth values to disparity
        filtered = self.filters.depth_to_disparity.process(filtered)

        # Apply spatial smoothing if needed
        # filtered = self.filters.spatial.process(filtered)

        # Apply temporal smoothing using previous frames
        filtered = self.filters.temporal.process(filtered)

        # Convert disparity values back to depth
        filtered = self.filters.disparity_to_depth.process(filtered)

        # Fill missing depth pixels
        filtered = self.filters.hole_filling.process(filtered)

        # Convert depth frame to NumPy array
        raw_depth = np.asanyarray(filtered.get_data())

        # Convert raw depth units to meters
        depths = raw_depth.astype(np.float32)
        depths *= np.float32(self.depth_scale)

        # Extract Region of Interest
        depths = depths[
            self.config.ROI_Y_MIN:self.config.ROI_Y_MAX,
            self.config.ROI_X_MIN:self.config.ROI_X_MAX
        ]

        return depths

    def stop(self):
        if self.started:
            self.pipeline.stop()
            self.started = False
