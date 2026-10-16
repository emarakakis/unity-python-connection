
from dataclasses import dataclass
from typing import ClassVar
import pyrealsense2 as rs


@dataclass(frozen=True)
class NetworkConfig:
    HOST: str = "127.0.0.1"
    PORT: int = 5000


@dataclass(frozen=True)
class CameraConfig:
    PIXELS_ROWS: int = 720
    PIXELS_COLS: int = 1280
    FPS: int = 30
    
    FORMAT: rs.format = rs.format.z16

    DECIMATION_FACTOR: int = 2

    ROI_X_MIN: int = 70
    ROI_Y_MIN: int = 20
    ROI_X_MAX: int = 530
    ROI_Y_MAX: int = 320

    @property
    def ROI_ROWS(self) -> int:
        return self.ROI_Y_MAX - self.ROI_Y_MIN

    @property
    def ROI_COLS(self) -> int:
        return self.ROI_X_MAX - self.ROI_X_MIN

    @property
    def GRID_ROWS(self) -> int:
        return self.PIXELS_ROWS // self.DECIMATION_FACTOR

    @property
    def GRID_COLS(self) -> int:
        return self.PIXELS_COLS // self.DECIMATION_FACTOR


@dataclass(frozen=True)
class SandmapConfig:

    # Distance from the camera to the floor
    FLOOR_DISTANCE: float = 1.66

    # Distance from the camera to the base of the sandbox
    BASE_DISTANCE: float = 1.0

    # Average sand height when the sand is flat
    AVERAGE_SAND_HEIGHT: float = 0.095

    # Maximum sand height
    MAX_SAND_HEIGHT: float = 1.0

    # Height amplification for visualization
    HEIGHT_MULTIPLIER: float = 2.5

    # Physical sandbox dimensions in meters
    PHYSICAL_BOX_DEPTH: float = 0.25
    PHYSICAL_BOX_WIDTH: float = 1.097
    PHYSICAL_BOX_LENGTH: float = 0.78

    @property
    def AVERAGE_SAND_HEIGHT_TOTAL(self) -> float:
        return self.BASE_DISTANCE + self.AVERAGE_SAND_HEIGHT

    @property
    def MIN_DEPTH(self) -> float:
        return self.BASE_DISTANCE - self.MAX_SAND_HEIGHT

    @property
    def MAX_DEPTH(self) -> float:
        return self.BASE_DISTANCE

    @property
    def PHYSICAL_BOX_VOLUME(self) -> float:
        return (
            self.PHYSICAL_BOX_DEPTH
            * self.PHYSICAL_BOX_WIDTH
            * self.PHYSICAL_BOX_LENGTH
            * 1000
        )
