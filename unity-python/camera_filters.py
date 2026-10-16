
from dataclasses import dataclass, field
import pyrealsense2 as rs


@dataclass
class CameraFilters:

    # --------------------------------------------------
    # Decimation Filter
    # --------------------------------------------------

    # Changes the dimensions of the depth output.
    # Magnitude = 2 because Unity processes half the original dimensions.
    decimation: rs.decimation_filter = field(
        default_factory=lambda: rs.decimation_filter(2)
    )

    # --------------------------------------------------
    # Disparity Transform
    # --------------------------------------------------

    # Converts depth to disparity and back.
    # Disparity is inversely proportional to distance:
    #
    # D = 32 * f * B / Z
    #
    # Z = distance from the camera
    # f = focal length
    # B = stereo baseline
    #
    # Disparity changes more rapidly for objects near the camera
    # and more slowly for objects farther away.
    depth_to_disparity: rs.disparity_transform = field(
        default_factory=lambda: rs.disparity_transform(True)
    )

    disparity_to_depth: rs.disparity_transform = field(
        default_factory=lambda: rs.disparity_transform(False)
    )

    # --------------------------------------------------
    # Spatial Filter
    # --------------------------------------------------

    # Magnitude:
    # Number of smoothing iterations performed by the spatial filter.

    # Smooth Alpha:
    # Controls smoothing strength.
    # Range: 0.25 to 1.0
    # 0.25 = stronger smoothing
    # 1.0 = no smoothing

    # Smooth Delta:
    # Threshold of the depth difference used for smoothing.
    # A larger threshold allows smoothing across larger differences.

    spatial: rs.spatial_filter = field(
        default_factory=lambda: rs.spatial_filter(
            smooth_alpha=0.5,
            smooth_delta=20,
            magnitude=2,
            hole_fill=0
        )
    )

    # --------------------------------------------------
    # Temporal Filter
    # --------------------------------------------------

    # Smooth Alpha:
    # Controls the importance of the current frame relative
    # to previous frames.
    #
    # filtered ≈ alpha * current + (1 - alpha) * previous
    #
    # Smaller alpha values preserve more historical information.

    # Smooth Delta:
    # Threshold used to decide whether temporal smoothing
    # should be applied based on the difference between
    # the current and previous pixel values.
    #
    # diff = abs(current - previous)
    # diff < delta
    #
    # If the condition is satisfied, temporal smoothing
    # can be applied.
    #
    # This filter can operate on depth or disparity data.

    # Persistence Control:
    # 0 = Disabled
    # 1 = Valid in 8/8 previous frames
    # 2 = Valid in 2/3 previous frames
    # 3 = Valid in 2/4 previous frames
    # 4 = Valid in 2/8 previous frames
    # 5 = Valid in 1/2 previous frames
    # 6 = Valid in 1/5 previous frames
    # 7 = Valid in 1/8 previous frames
    # 8 = Persist indefinitely

    temporal: rs.temporal_filter = field(
        default_factory=lambda: rs.temporal_filter(
            smooth_alpha=0.5,
            smooth_delta=20,
            persistence_control=4
        )
    )

    # --------------------------------------------------
    # Hole Filling Filter
    # --------------------------------------------------

    # Fills missing depth pixels caused by sensor noise.
    #
    # Mode:
    # 0 = Fill from left
    # 1 = Farthest from around
    # 2 = Nearest from around

    hole_filling: rs.hole_filling_filter = field(
        default_factory=lambda: rs.hole_filling_filter(1)
    )
