"""
        Librealsense Python Bindings
        ==============================
        Library for accessing RealSense cameras
    
"""
from __future__ import annotations
import datetime
import pybind11_stubgen.typing_ext
import typing
__all__: list[str] = ['BufData', 'D400', 'D500', 'DEPTH', 'L500', 'SR300', 'STAEControl', 'STAFactor', 'STCensusRadius', 'STColorControl', 'STColorCorrection', 'STDepthControlGroup', 'STDepthTableControl', 'STHdad', 'STRauColorThresholdsControl', 'STRauSupportVectorControl', 'STRsm', 'STSloColorThresholdsControl', 'STSloPenaltyControl', 'T200', 'TRACKING', 'align', 'any', 'any_intel', 'auto_calibrated_device', 'calib_location', 'calib_target_type', 'calibration_change_device', 'calibration_status', 'calibration_type', 'camera_info', 'color_sensor', 'colorizer', 'combined_motion', 'composite_frame', 'config', 'context', 'd500_intercam_sync_mode', 'debug_protocol', 'debug_stream_sensor', 'decimation_filter', 'depth_frame', 'depth_sensor', 'depth_stereo_sensor', 'device', 'device_calibration', 'device_hub', 'device_list', 'disparity_frame', 'disparity_transform', 'distortion', 'embedded_decimation_filter', 'embedded_filter', 'embedded_filter_type', 'embedded_temporal_filter', 'enable_metadata', 'enable_rolling_log_file', 'eth_config_device', 'event_information', 'extension', 'extrinsics', 'filter', 'filter_interface', 'firmware_log_message', 'firmware_log_parsed_message', 'firmware_logger', 'fisheye_sensor', 'format', 'frame', 'frame_metadata_value', 'frame_queue', 'frame_source', 'gpu_frame', 'hdr_merge', 'hole_filling_filter', 'intrinsics', 'ip_address', 'l500_visual_preset', 'labeled_points', 'link_priority', 'log', 'log_message', 'log_severity', 'log_to_callback', 'log_to_console', 'log_to_file', 'm420_converter', 'matchers', 'max_usable_range_sensor', 'motion_device_intrinsic', 'motion_frame', 'motion_sensor', 'motion_stream', 'motion_stream_profile', 'non_intel', 'notification', 'notification_category', 'nv12_converter', 'object_detection', 'object_detection_frame', 'option', 'option_from_string', 'option_range', 'option_type', 'option_value', 'options', 'options_list', 'perception_frame', 'perception_sensor', 'perception_stream', 'perception_stream_profile', 'pipeline', 'pipeline_profile', 'pipeline_wrapper', 'playback', 'playback_status', 'pointcloud', 'points', 'pose', 'pose_frame', 'pose_sensor', 'pose_stream', 'pose_stream_profile', 'processing_block', 'product_line', 'quaternion', 'recorder', 'region_of_interest', 'reset_logger', 'roi_sensor', 'rotation_filter', 'rs2_deproject_pixel_to_point', 'rs2_fov', 'rs2_project_color_pixel_to_depth_pixel', 'rs2_project_point_to_pixel', 'rs2_transform_point_to_point', 'rs400_advanced_mode', 'rs400_visual_preset', 'safety_mode', 'safety_sensor', 'save_single_frameset', 'save_to_ply', 'sensor', 'sequence_id_filter', 'serializable_device', 'software_device', 'software_motion_frame', 'software_notification', 'software_pose_frame', 'software_sensor', 'software_video_frame', 'spatial_filter', 'stream', 'stream_profile', 'supports_eth_config', 'sw_only', 'syncer', 'temporal_filter', 'terminal_parser', 'texture_coordinate', 'threshold_filter', 'timestamp_domain', 'units_transform', 'updatable', 'update_device', 'uyvy_converter', 'vector', 'vertex', 'video_frame', 'video_stream', 'video_stream_profile', 'wheel_odometer', 'yuy2_converter', 'yuy_decoder']
class notification_category:
    """
    Category of the librealsense notification.
    
    Members:
    
      frames_timeout
    
      frame_corrupted
    
      hardware_error
    
      hardware_event
    
      unknown_error
    
      firmware_update_recommended
    
      pose_relocalization
    """
    __members__: typing.ClassVar[dict[str, notification_category]]
    firmware_update_recommended: typing.ClassVar[notification_category]
    frame_corrupted: typing.ClassVar[notification_category]
    frames_timeout: typing.ClassVar[notification_category]
    hardware_error: typing.ClassVar[notification_category]
    hardware_event: typing.ClassVar[notification_category]
    pose_relocalization: typing.ClassVar[notification_category]
    unknown_error: typing.ClassVar[notification_category]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class distortion:
    """
    Distortion model: defines how pixel coordinates should be mapped to sensor coordinates.
    
    Members:
    
      none
    
      modified_brown_conrady
    
      inverse_brown_conrady
    
      ftheta
    
      brown_conrady
    
      kannala_brandt4
    """
    __members__: typing.ClassVar[dict[str, distortion]]
    brown_conrady: typing.ClassVar[distortion]
    ftheta: typing.ClassVar[distortion]
    inverse_brown_conrady: typing.ClassVar[distortion]
    kannala_brandt4: typing.ClassVar[distortion]
    modified_brown_conrady: typing.ClassVar[distortion]
    none: typing.ClassVar[distortion]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class log_severity:
    """
    Severity of the librealsense logger.
    
    Members:
    
      debug
    
      info
    
      warn
    
      error
    
      fatal
    
      none
    """
    __members__: typing.ClassVar[dict[str, log_severity]]
    debug: typing.ClassVar[log_severity]
    error: typing.ClassVar[log_severity]
    fatal: typing.ClassVar[log_severity]
    info: typing.ClassVar[log_severity]
    none: typing.ClassVar[log_severity]
    warn: typing.ClassVar[log_severity]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class extension:
    """
    Specifies advanced interfaces (capabilities) objects may implement.
    
    Members:
    
      unknown
    
      debug
    
      info
    
      motion
    
      options
    
      video
    
      roi
    
      depth_sensor
    
      video_frame
    
      motion_frame
    
      composite_frame
    
      points
    
      depth_frame
    
      advanced_mode
    
      record
    
      video_profile
    
      playback
    
      depth_stereo_sensor
    
      disparity_frame
    
      motion_profile
    
      pose_frame
    
      pose_profile
    
      tm2
    
      software_device
    
      software_sensor
    
      decimation_filter
    
      threshold_filter
    
      disparity_filter
    
      spatial_filter
    
      temporal_filter
    
      hole_filling_filter
    
      zero_order_filter
    
      recommended_filters
    
      pose
    
      pose_sensor
    
      wheel_odometer
    
      global_timer
    
      updatable
    
      update_device
    
      l500_depth_sensor
    
      tm2_sensor
    
      auto_calibrated_device
    
      color_sensor
    
      motion_sensor
    
      fisheye_sensor
    
      depth_huffman_decoder
    
      serializable
    
      fw_logger
    
      auto_calibration_filter
    
      device_calibration
    
      calibrated_sensor
    
      hdr_merge
    
      sequence_id_filter
    
      max_usable_range_sensor
    
      debug_stream_sensor
    
      calibration_change_device
    
      rotation_filter
    
      safety_sensor
    
      depth_mapping_sensor
    
      labeled_points
    
      eth_config
    
      supported_embedded_filters
    
      decimation_embedded_filter
    
      temporal_embedded_filter
    
      close_range_embedded_filter
    
      perception_frame
    
      object_detection_frame
    
      perception_sensor
    
      perception_profile
    
      gpu_frame
    """
    __members__: typing.ClassVar[dict[str, extension]]
    advanced_mode: typing.ClassVar[extension]
    auto_calibrated_device: typing.ClassVar[extension]
    auto_calibration_filter: typing.ClassVar[extension]
    calibrated_sensor: typing.ClassVar[extension]
    calibration_change_device: typing.ClassVar[extension]
    close_range_embedded_filter: typing.ClassVar[extension]
    color_sensor: typing.ClassVar[extension]
    composite_frame: typing.ClassVar[extension]
    debug: typing.ClassVar[extension]
    debug_stream_sensor: typing.ClassVar[extension]
    decimation_embedded_filter: typing.ClassVar[extension]
    decimation_filter: typing.ClassVar[extension]
    depth_frame: typing.ClassVar[extension]
    depth_huffman_decoder: typing.ClassVar[extension]
    depth_mapping_sensor: typing.ClassVar[extension]
    depth_sensor: typing.ClassVar[extension]
    depth_stereo_sensor: typing.ClassVar[extension]
    device_calibration: typing.ClassVar[extension]
    disparity_filter: typing.ClassVar[extension]
    disparity_frame: typing.ClassVar[extension]
    eth_config: typing.ClassVar[extension]
    fisheye_sensor: typing.ClassVar[extension]
    fw_logger: typing.ClassVar[extension]
    global_timer: typing.ClassVar[extension]
    gpu_frame: typing.ClassVar[extension]
    hdr_merge: typing.ClassVar[extension]
    hole_filling_filter: typing.ClassVar[extension]
    info: typing.ClassVar[extension]
    l500_depth_sensor: typing.ClassVar[extension]
    labeled_points: typing.ClassVar[extension]
    max_usable_range_sensor: typing.ClassVar[extension]
    motion: typing.ClassVar[extension]
    motion_frame: typing.ClassVar[extension]
    motion_profile: typing.ClassVar[extension]
    motion_sensor: typing.ClassVar[extension]
    object_detection_frame: typing.ClassVar[extension]
    options: typing.ClassVar[extension]
    perception_frame: typing.ClassVar[extension]
    perception_profile: typing.ClassVar[extension]
    perception_sensor: typing.ClassVar[extension]
    playback: typing.ClassVar[extension]
    points: typing.ClassVar[extension]
    pose: typing.ClassVar[extension]
    pose_frame: typing.ClassVar[extension]
    pose_profile: typing.ClassVar[extension]
    pose_sensor: typing.ClassVar[extension]
    recommended_filters: typing.ClassVar[extension]
    record: typing.ClassVar[extension]
    roi: typing.ClassVar[extension]
    rotation_filter: typing.ClassVar[extension]
    safety_sensor: typing.ClassVar[extension]
    sequence_id_filter: typing.ClassVar[extension]
    serializable: typing.ClassVar[extension]
    software_device: typing.ClassVar[extension]
    software_sensor: typing.ClassVar[extension]
    spatial_filter: typing.ClassVar[extension]
    supported_embedded_filters: typing.ClassVar[extension]
    temporal_embedded_filter: typing.ClassVar[extension]
    temporal_filter: typing.ClassVar[extension]
    threshold_filter: typing.ClassVar[extension]
    tm2: typing.ClassVar[extension]
    tm2_sensor: typing.ClassVar[extension]
    unknown: typing.ClassVar[extension]
    updatable: typing.ClassVar[extension]
    update_device: typing.ClassVar[extension]
    video: typing.ClassVar[extension]
    video_frame: typing.ClassVar[extension]
    video_profile: typing.ClassVar[extension]
    wheel_odometer: typing.ClassVar[extension]
    zero_order_filter: typing.ClassVar[extension]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class matchers:
    """
    Specifies types of different matchers.
    
    Members:
    
      di
    
      di_c
    
      dlr_c
    
      dlr
    
      dic
    
      dic_c
    
      default
    """
    __members__: typing.ClassVar[dict[str, matchers]]
    default: typing.ClassVar[matchers]
    di: typing.ClassVar[matchers]
    di_c: typing.ClassVar[matchers]
    dic: typing.ClassVar[matchers]
    dic_c: typing.ClassVar[matchers]
    dlr: typing.ClassVar[matchers]
    dlr_c: typing.ClassVar[matchers]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class camera_info:
    """
    This information is mainly available for camera debug and troubleshooting and should not be used in applications.
    
    Members:
    
      name
    
      serial_number
    
      firmware_version
    
      recommended_firmware_version
    
      physical_port
    
      debug_op_code
    
      advanced_mode
    
      product_id
    
      camera_locked
    
      usb_type_descriptor
    
      product_line
    
      asic_serial_number
    
      firmware_update_id
    
      ip_address
    
      dfu_device_path
    
      connection_type
    
      smcu_fw_version
    
      imu_type
    
      mipi_driver_version
    """
    __members__: typing.ClassVar[dict[str, camera_info]]
    advanced_mode: typing.ClassVar[camera_info]
    asic_serial_number: typing.ClassVar[camera_info]
    camera_locked: typing.ClassVar[camera_info]
    connection_type: typing.ClassVar[camera_info]
    debug_op_code: typing.ClassVar[camera_info]
    dfu_device_path: typing.ClassVar[camera_info]
    firmware_update_id: typing.ClassVar[camera_info]
    firmware_version: typing.ClassVar[camera_info]
    imu_type: typing.ClassVar[camera_info]
    ip_address: typing.ClassVar[camera_info]
    mipi_driver_version: typing.ClassVar[camera_info]
    name: typing.ClassVar[camera_info]
    physical_port: typing.ClassVar[camera_info]
    product_id: typing.ClassVar[camera_info]
    product_line: typing.ClassVar[camera_info]
    recommended_firmware_version: typing.ClassVar[camera_info]
    serial_number: typing.ClassVar[camera_info]
    smcu_fw_version: typing.ClassVar[camera_info]
    usb_type_descriptor: typing.ClassVar[camera_info]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class stream:
    """
    Streams are different types of data provided by RealSense devices.
    
    Members:
    
      any
    
      depth
    
      color
    
      infrared
    
      fisheye
    
      gyro
    
      accel
    
      gpio
    
      pose
    
      confidence
    
      motion
    
      safety
    
      occupancy
    
      labeled_point_cloud
    
      object_detection
    """
    __members__: typing.ClassVar[dict[str, stream]]
    accel: typing.ClassVar[stream]
    any: typing.ClassVar[stream]
    color: typing.ClassVar[stream]
    confidence: typing.ClassVar[stream]
    depth: typing.ClassVar[stream]
    fisheye: typing.ClassVar[stream]
    gpio: typing.ClassVar[stream]
    gyro: typing.ClassVar[stream]
    infrared: typing.ClassVar[stream]
    labeled_point_cloud: typing.ClassVar[stream]
    motion: typing.ClassVar[stream]
    object_detection: typing.ClassVar[stream]
    occupancy: typing.ClassVar[stream]
    pose: typing.ClassVar[stream]
    safety: typing.ClassVar[stream]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class format:
    """
    A stream's format identifies how binary data is encoded within a frame.
    
    Members:
    
      any
    
      z16
    
      disparity16
    
      xyz32f
    
      yuyv
    
      rgb8
    
      bgr8
    
      rgba8
    
      bgra8
    
      y8
    
      y16
    
      raw10
    
      raw16
    
      raw8
    
      uyvy
    
      motion_raw
    
      motion_xyz32f
    
      gpio_raw
    
      six_dof
    
      disparity32
    
      y10bpack
    
      distance
    
      mjpeg
    
      y8i
    
      y12i
    
      inzi
    
      invi
    
      w10
    
      z16h
    
      fg
    
      y411
    
      y16i
    
      m420
    
      combined_motion
    
      nv12
    """
    __members__: typing.ClassVar[dict[str, format]]
    any: typing.ClassVar[format]
    bgr8: typing.ClassVar[format]
    bgra8: typing.ClassVar[format]
    combined_motion: typing.ClassVar[format]
    disparity16: typing.ClassVar[format]
    disparity32: typing.ClassVar[format]
    distance: typing.ClassVar[format]
    fg: typing.ClassVar[format]
    gpio_raw: typing.ClassVar[format]
    invi: typing.ClassVar[format]
    inzi: typing.ClassVar[format]
    m420: typing.ClassVar[format]
    mjpeg: typing.ClassVar[format]
    motion_raw: typing.ClassVar[format]
    motion_xyz32f: typing.ClassVar[format]
    nv12: typing.ClassVar[format]
    raw10: typing.ClassVar[format]
    raw16: typing.ClassVar[format]
    raw8: typing.ClassVar[format]
    rgb8: typing.ClassVar[format]
    rgba8: typing.ClassVar[format]
    six_dof: typing.ClassVar[format]
    uyvy: typing.ClassVar[format]
    w10: typing.ClassVar[format]
    xyz32f: typing.ClassVar[format]
    y10bpack: typing.ClassVar[format]
    y12i: typing.ClassVar[format]
    y16: typing.ClassVar[format]
    y16i: typing.ClassVar[format]
    y411: typing.ClassVar[format]
    y8: typing.ClassVar[format]
    y8i: typing.ClassVar[format]
    yuyv: typing.ClassVar[format]
    z16: typing.ClassVar[format]
    z16h: typing.ClassVar[format]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class timestamp_domain:
    """
    Specifies the clock in relation to which the frame timestamp was measured.
    
    Members:
    
      hardware_clock
    
      system_time
    
      global_time
    """
    __members__: typing.ClassVar[dict[str, timestamp_domain]]
    global_time: typing.ClassVar[timestamp_domain]
    hardware_clock: typing.ClassVar[timestamp_domain]
    system_time: typing.ClassVar[timestamp_domain]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class frame_metadata_value:
    """
    Per-Frame-Metadata is the set of read-only properties that might be exposed for each individual frame.
    
    Members:
    
      frame_counter
    
      frame_timestamp
    
      sensor_timestamp
    
      actual_exposure
    
      gain_level
    
      auto_exposure
    
      white_balance
    
      time_of_arrival
    
      temperature
    
      backend_timestamp
    
      actual_fps
    
      frame_laser_power
    
      frame_laser_power_mode
    
      exposure_priority
    
      exposure_roi_left
    
      exposure_roi_right
    
      exposure_roi_top
    
      exposure_roi_bottom
    
      brightness
    
      contrast
    
      saturation
    
      sharpness
    
      auto_white_balance_temperature
    
      backlight_compensation
    
      hue
    
      gamma
    
      manual_white_balance
    
      power_line_frequency
    
      low_light_compensation
    
      frame_emitter_mode
    
      frame_led_power
    
      raw_frame_size
    
      gpio_input_data
    
      sequence_name
    
      sequence_id
    
      sequence_size
    
      trigger
    
      preset
    
      input_width
    
      input_height
    
      sub_preset_info
    
      calib_info
    
      crc
    
      safety_depth_frame_counter
    
      safety_level1
    
      safety_level1_origin
    
      safety_level2
    
      safety_level2_origin
    
      safety_level1_verdict
    
      safety_level2_verdict
    
      safety_operational_mode
    
      safety_vision_verdict
    
      safety_hara_events
    
      safety_preset_integrity
    
      safety_preset_id_selected
    
      safety_preset_id_used
    
      safety_sip_degradation_used
    
      safety_sip_generic_metrics_activate
    
      safety_sip_generic_metrics_state
    
      safety_sip_generic_metrics_value1
    
      safety_sip_generic_metrics_value2
    
      safety_sip_generic_metrics_threshold1
    
      safety_sip_generic_metrics_threshold2
    
      safety_zero_monitoring_enabled
    
      safety_hara_history_mode
    
      safety_soc_fusa_events
    
      safety_soc_fusa_action
    
      safety_soc_l0_counter
    
      safety_soc_l0_rate
    
      safety_soc_l1_counter
    
      safety_soc_l1_rate
    
      safety_soc_gmt_status
    
      safety_soc_hkr_critical_error_gpio
    
      safety_soc_monitor_l2_error_type
    
      safety_soc_monitor_l3_error_type
    
      safety_soc_safety_and_security
    
      safety_depth_frame_timestamp
    
      safety_smcu_processing_timestamp
    
      safety_pipeline_propagation_delay
    
      safety_smcu_debug_status_bitmask
    
      safety_smcu_debug_info_internal_state
    
      safety_smcu_debug_info_bist_status
    
      safety_non_fusa_gpio_out
    
      safety_smcu_hw_monitor_status
    
      safety_smcu_sw_monitor_status
    
      safety_non_fusa_gpio_in
    
      safety_mb_fusa_event
    
      safety_mb_fusa_action
    
      safety_mb_status
    
      safety_smcu_liveliness
    
      safety_smcu_state
    
      safety_preset_id
    
      sensor_angle_roll
    
      sensor_angle_pitch
    
      diagnostic_zone_median_height
    
      floor_detection
    
      diagnostic_zone_fill_rate
    
      depth_fill_rate
    
      depth_stdev
    
      occupancy_grid_rows
    
      occupancy_grid_columns
    
      occupancy_cell_size
    
      number_of_3d_vertices
    
      safety_preset_error_type
    
      safety_preset_error_param_1
    
      safety_preset_error_param_2
    
      danger_zone_point_0_x_cord
    
      danger_zone_point_0_y_cord
    
      danger_zone_point_1_x_cord
    
      danger_zone_point_1_y_cord
    
      danger_zone_point_2_x_cord
    
      danger_zone_point_2_y_cord
    
      danger_zone_point_3_x_cord
    
      danger_zone_point_3_y_cord
    
      warning_zone_point_0_x_cord
    
      warning_zone_point_0_y_cord
    
      warning_zone_point_1_x_cord
    
      warning_zone_point_1_y_cord
    
      warning_zone_point_2_x_cord
    
      warning_zone_point_2_y_cord
    
      warning_zone_point_3_x_cord
    
      warning_zone_point_3_y_cord
    
      diagnostic_zone_point_0_x_cord
    
      diagnostic_zone_point_0_y_cord
    
      diagnostic_zone_point_1_x_cord
    
      diagnostic_zone_point_1_y_cord
    
      diagnostic_zone_point_2_x_cord
    
      diagnostic_zone_point_2_y_cord
    
      diagnostic_zone_point_3_x_cord
    
      diagnostic_zone_point_3_y_cord
    
      embedded_filters
    """
    __members__: typing.ClassVar[dict[str, frame_metadata_value]]
    actual_exposure: typing.ClassVar[frame_metadata_value]
    actual_fps: typing.ClassVar[frame_metadata_value]
    auto_exposure: typing.ClassVar[frame_metadata_value]
    auto_white_balance_temperature: typing.ClassVar[frame_metadata_value]
    backend_timestamp: typing.ClassVar[frame_metadata_value]
    backlight_compensation: typing.ClassVar[frame_metadata_value]
    brightness: typing.ClassVar[frame_metadata_value]
    calib_info: typing.ClassVar[frame_metadata_value]
    contrast: typing.ClassVar[frame_metadata_value]
    crc: typing.ClassVar[frame_metadata_value]
    danger_zone_point_0_x_cord: typing.ClassVar[frame_metadata_value]
    danger_zone_point_0_y_cord: typing.ClassVar[frame_metadata_value]
    danger_zone_point_1_x_cord: typing.ClassVar[frame_metadata_value]
    danger_zone_point_1_y_cord: typing.ClassVar[frame_metadata_value]
    danger_zone_point_2_x_cord: typing.ClassVar[frame_metadata_value]
    danger_zone_point_2_y_cord: typing.ClassVar[frame_metadata_value]
    danger_zone_point_3_x_cord: typing.ClassVar[frame_metadata_value]
    danger_zone_point_3_y_cord: typing.ClassVar[frame_metadata_value]
    depth_fill_rate: typing.ClassVar[frame_metadata_value]
    depth_stdev: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_fill_rate: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_median_height: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_point_0_x_cord: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_point_0_y_cord: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_point_1_x_cord: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_point_1_y_cord: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_point_2_x_cord: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_point_2_y_cord: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_point_3_x_cord: typing.ClassVar[frame_metadata_value]
    diagnostic_zone_point_3_y_cord: typing.ClassVar[frame_metadata_value]
    embedded_filters: typing.ClassVar[frame_metadata_value]
    exposure_priority: typing.ClassVar[frame_metadata_value]
    exposure_roi_bottom: typing.ClassVar[frame_metadata_value]
    exposure_roi_left: typing.ClassVar[frame_metadata_value]
    exposure_roi_right: typing.ClassVar[frame_metadata_value]
    exposure_roi_top: typing.ClassVar[frame_metadata_value]
    floor_detection: typing.ClassVar[frame_metadata_value]
    frame_counter: typing.ClassVar[frame_metadata_value]
    frame_emitter_mode: typing.ClassVar[frame_metadata_value]
    frame_laser_power: typing.ClassVar[frame_metadata_value]
    frame_laser_power_mode: typing.ClassVar[frame_metadata_value]
    frame_led_power: typing.ClassVar[frame_metadata_value]
    frame_timestamp: typing.ClassVar[frame_metadata_value]
    gain_level: typing.ClassVar[frame_metadata_value]
    gamma: typing.ClassVar[frame_metadata_value]
    gpio_input_data: typing.ClassVar[frame_metadata_value]
    hue: typing.ClassVar[frame_metadata_value]
    input_height: typing.ClassVar[frame_metadata_value]
    input_width: typing.ClassVar[frame_metadata_value]
    low_light_compensation: typing.ClassVar[frame_metadata_value]
    manual_white_balance: typing.ClassVar[frame_metadata_value]
    number_of_3d_vertices: typing.ClassVar[frame_metadata_value]
    occupancy_cell_size: typing.ClassVar[frame_metadata_value]
    occupancy_grid_columns: typing.ClassVar[frame_metadata_value]
    occupancy_grid_rows: typing.ClassVar[frame_metadata_value]
    power_line_frequency: typing.ClassVar[frame_metadata_value]
    preset: typing.ClassVar[frame_metadata_value]
    raw_frame_size: typing.ClassVar[frame_metadata_value]
    safety_depth_frame_counter: typing.ClassVar[frame_metadata_value]
    safety_depth_frame_timestamp: typing.ClassVar[frame_metadata_value]
    safety_hara_events: typing.ClassVar[frame_metadata_value]
    safety_hara_history_mode: typing.ClassVar[frame_metadata_value]
    safety_level1: typing.ClassVar[frame_metadata_value]
    safety_level1_origin: typing.ClassVar[frame_metadata_value]
    safety_level1_verdict: typing.ClassVar[frame_metadata_value]
    safety_level2: typing.ClassVar[frame_metadata_value]
    safety_level2_origin: typing.ClassVar[frame_metadata_value]
    safety_level2_verdict: typing.ClassVar[frame_metadata_value]
    safety_mb_fusa_action: typing.ClassVar[frame_metadata_value]
    safety_mb_fusa_event: typing.ClassVar[frame_metadata_value]
    safety_mb_status: typing.ClassVar[frame_metadata_value]
    safety_non_fusa_gpio_in: typing.ClassVar[frame_metadata_value]
    safety_non_fusa_gpio_out: typing.ClassVar[frame_metadata_value]
    safety_operational_mode: typing.ClassVar[frame_metadata_value]
    safety_pipeline_propagation_delay: typing.ClassVar[frame_metadata_value]
    safety_preset_error_param_1: typing.ClassVar[frame_metadata_value]
    safety_preset_error_param_2: typing.ClassVar[frame_metadata_value]
    safety_preset_error_type: typing.ClassVar[frame_metadata_value]
    safety_preset_id: typing.ClassVar[frame_metadata_value]
    safety_preset_id_selected: typing.ClassVar[frame_metadata_value]
    safety_preset_id_used: typing.ClassVar[frame_metadata_value]
    safety_preset_integrity: typing.ClassVar[frame_metadata_value]
    safety_sip_degradation_used: typing.ClassVar[frame_metadata_value]
    safety_sip_generic_metrics_activate: typing.ClassVar[frame_metadata_value]
    safety_sip_generic_metrics_state: typing.ClassVar[frame_metadata_value]
    safety_sip_generic_metrics_threshold1: typing.ClassVar[frame_metadata_value]
    safety_sip_generic_metrics_threshold2: typing.ClassVar[frame_metadata_value]
    safety_sip_generic_metrics_value1: typing.ClassVar[frame_metadata_value]
    safety_sip_generic_metrics_value2: typing.ClassVar[frame_metadata_value]
    safety_smcu_debug_info_bist_status: typing.ClassVar[frame_metadata_value]
    safety_smcu_debug_info_internal_state: typing.ClassVar[frame_metadata_value]
    safety_smcu_debug_status_bitmask: typing.ClassVar[frame_metadata_value]
    safety_smcu_hw_monitor_status: typing.ClassVar[frame_metadata_value]
    safety_smcu_liveliness: typing.ClassVar[frame_metadata_value]
    safety_smcu_processing_timestamp: typing.ClassVar[frame_metadata_value]
    safety_smcu_state: typing.ClassVar[frame_metadata_value]
    safety_smcu_sw_monitor_status: typing.ClassVar[frame_metadata_value]
    safety_soc_fusa_action: typing.ClassVar[frame_metadata_value]
    safety_soc_fusa_events: typing.ClassVar[frame_metadata_value]
    safety_soc_gmt_status: typing.ClassVar[frame_metadata_value]
    safety_soc_hkr_critical_error_gpio: typing.ClassVar[frame_metadata_value]
    safety_soc_l0_counter: typing.ClassVar[frame_metadata_value]
    safety_soc_l0_rate: typing.ClassVar[frame_metadata_value]
    safety_soc_l1_counter: typing.ClassVar[frame_metadata_value]
    safety_soc_l1_rate: typing.ClassVar[frame_metadata_value]
    safety_soc_monitor_l2_error_type: typing.ClassVar[frame_metadata_value]
    safety_soc_monitor_l3_error_type: typing.ClassVar[frame_metadata_value]
    safety_soc_safety_and_security: typing.ClassVar[frame_metadata_value]
    safety_vision_verdict: typing.ClassVar[frame_metadata_value]
    safety_zero_monitoring_enabled: typing.ClassVar[frame_metadata_value]
    saturation: typing.ClassVar[frame_metadata_value]
    sensor_angle_pitch: typing.ClassVar[frame_metadata_value]
    sensor_angle_roll: typing.ClassVar[frame_metadata_value]
    sensor_timestamp: typing.ClassVar[frame_metadata_value]
    sequence_id: typing.ClassVar[frame_metadata_value]
    sequence_name: typing.ClassVar[frame_metadata_value]
    sequence_size: typing.ClassVar[frame_metadata_value]
    sharpness: typing.ClassVar[frame_metadata_value]
    sub_preset_info: typing.ClassVar[frame_metadata_value]
    temperature: typing.ClassVar[frame_metadata_value]
    time_of_arrival: typing.ClassVar[frame_metadata_value]
    trigger: typing.ClassVar[frame_metadata_value]
    warning_zone_point_0_x_cord: typing.ClassVar[frame_metadata_value]
    warning_zone_point_0_y_cord: typing.ClassVar[frame_metadata_value]
    warning_zone_point_1_x_cord: typing.ClassVar[frame_metadata_value]
    warning_zone_point_1_y_cord: typing.ClassVar[frame_metadata_value]
    warning_zone_point_2_x_cord: typing.ClassVar[frame_metadata_value]
    warning_zone_point_2_y_cord: typing.ClassVar[frame_metadata_value]
    warning_zone_point_3_x_cord: typing.ClassVar[frame_metadata_value]
    warning_zone_point_3_y_cord: typing.ClassVar[frame_metadata_value]
    white_balance: typing.ClassVar[frame_metadata_value]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class calib_target_type:
    """
    Calibration target type.
    
    Members:
    
      rect_gaussian_dot_vertices
    
      roi_rect_gaussian_dot_vertices
    
      pos_gaussian_dot_vertices
    """
    __members__: typing.ClassVar[dict[str, calib_target_type]]
    pos_gaussian_dot_vertices: typing.ClassVar[calib_target_type]
    rect_gaussian_dot_vertices: typing.ClassVar[calib_target_type]
    roi_rect_gaussian_dot_vertices: typing.ClassVar[calib_target_type]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class option:
    """
    Defines general configuration controls. These can generally be mapped to camera UVC controls, and can be set / queried at any time unless stated otherwise.
    
    Members:
    
      backlight_compensation
    
      brightness
    
      contrast
    
      exposure
    
      gain
    
      gamma
    
      hue
    
      saturation
    
      sharpness
    
      white_balance
    
      enable_auto_exposure
    
      enable_auto_white_balance
    
      visual_preset
    
      laser_power
    
      accuracy
    
      motion_range
    
      filter_option
    
      confidence_threshold
    
      emitter_enabled
    
      frames_queue_size
    
      total_frame_drops
    
      fisheye_auto_exposure_mode
    
      power_line_frequency
    
      asic_temperature
    
      error_polling_enabled
    
      projector_temperature
    
      output_trigger_enabled
    
      motion_module_temperature
    
      depth_units
    
      enable_motion_correction
    
      auto_exposure_priority
    
      color_scheme
    
      histogram_equalization_enabled
    
      min_distance
    
      max_distance
    
      texture_source
    
      filter_magnitude
    
      filter_smooth_alpha
    
      filter_smooth_delta
    
      holes_fill
    
      stereo_baseline
    
      auto_exposure_converge_step
    
      inter_cam_sync_mode
    
      stream_filter
    
      stream_format_filter
    
      stream_index_filter
    
      emitter_on_off
    
      zero_order_point_x
    
      zero_order_point_y
    
      ldd_temperature
    
      mc_temperature
    
      ma_temperature
    
      hardware_preset
    
      global_time_enabled
    
      apd_temperature
    
      enable_mapping
    
      enable_relocalization
    
      enable_pose_jumping
    
      enable_dynamic_calibration
    
      depth_offset
    
      led_power
    
      zero_order_enabled
    
      enable_map_preservation
    
      freefall_detection_enabled
    
      receiver_gain
    
      post_processing_sharpening
    
      pre_processing_sharpening
    
      noise_filtering
    
      invalidation_bypass
    
      digital_gain
    
      sensor_mode
    
      emitter_always_on
    
      thermal_compensation
    
      trigger_camera_accuracy_health
    
      reset_camera_accuracy_health
    
      host_performance
    
      hdr_enabled
    
      sequence_name
    
      sequence_size
    
      sequence_id
    
      humidity_temperature
    
      enable_max_usable_range
    
      alternate_ir
    
      noise_estimation
    
      enable_ir_reflectivity
    
      auto_exposure_limit
    
      auto_gain_limit
    
      auto_rx_sensitivity
    
      transmitter_frequency
    
      vertical_binning
    
      receiver_sensitivity
    
      auto_exposure_limit_toggle
    
      auto_gain_limit_toggle
    
      emitter_frequency
    
      auto_exposure_mode
    
      ohm_temperature
    
      soc_pvt_temperature
    
      gyro_sensitivity
    
      region_of_interest
    
      rotation
    
      safety_preset_active_index
    
      safety_mode
    
      rgb_tnr_enabled
    
      safety_mcu_temperature
    
      left_ir_temperature
    
      embedded_filter_enabled
    
      disparity_shift
    
      threshold
    
      downscale_ratio
    
      readout_shaping
    
      detection_distance
    
      sensors_config_mode
    
      unknown
    
      ambient_light
    
      lld_temperature
    """
    __members__: typing.ClassVar[dict[str, option]]
    accuracy: typing.ClassVar[option]
    alternate_ir: typing.ClassVar[option]
    ambient_light: typing.ClassVar[option]
    apd_temperature: typing.ClassVar[option]
    asic_temperature: typing.ClassVar[option]
    auto_exposure_converge_step: typing.ClassVar[option]
    auto_exposure_limit: typing.ClassVar[option]
    auto_exposure_limit_toggle: typing.ClassVar[option]
    auto_exposure_mode: typing.ClassVar[option]
    auto_exposure_priority: typing.ClassVar[option]
    auto_gain_limit: typing.ClassVar[option]
    auto_gain_limit_toggle: typing.ClassVar[option]
    auto_rx_sensitivity: typing.ClassVar[option]
    backlight_compensation: typing.ClassVar[option]
    brightness: typing.ClassVar[option]
    color_scheme: typing.ClassVar[option]
    confidence_threshold: typing.ClassVar[option]
    contrast: typing.ClassVar[option]
    depth_offset: typing.ClassVar[option]
    depth_units: typing.ClassVar[option]
    detection_distance: typing.ClassVar[option]
    digital_gain: typing.ClassVar[option]
    disparity_shift: typing.ClassVar[option]
    downscale_ratio: typing.ClassVar[option]
    embedded_filter_enabled: typing.ClassVar[option]
    emitter_always_on: typing.ClassVar[option]
    emitter_enabled: typing.ClassVar[option]
    emitter_frequency: typing.ClassVar[option]
    emitter_on_off: typing.ClassVar[option]
    enable_auto_exposure: typing.ClassVar[option]
    enable_auto_white_balance: typing.ClassVar[option]
    enable_dynamic_calibration: typing.ClassVar[option]
    enable_ir_reflectivity: typing.ClassVar[option]
    enable_map_preservation: typing.ClassVar[option]
    enable_mapping: typing.ClassVar[option]
    enable_max_usable_range: typing.ClassVar[option]
    enable_motion_correction: typing.ClassVar[option]
    enable_pose_jumping: typing.ClassVar[option]
    enable_relocalization: typing.ClassVar[option]
    error_polling_enabled: typing.ClassVar[option]
    exposure: typing.ClassVar[option]
    filter_magnitude: typing.ClassVar[option]
    filter_option: typing.ClassVar[option]
    filter_smooth_alpha: typing.ClassVar[option]
    filter_smooth_delta: typing.ClassVar[option]
    fisheye_auto_exposure_mode: typing.ClassVar[option]
    frames_queue_size: typing.ClassVar[option]
    freefall_detection_enabled: typing.ClassVar[option]
    gain: typing.ClassVar[option]
    gamma: typing.ClassVar[option]
    global_time_enabled: typing.ClassVar[option]
    gyro_sensitivity: typing.ClassVar[option]
    hardware_preset: typing.ClassVar[option]
    hdr_enabled: typing.ClassVar[option]
    histogram_equalization_enabled: typing.ClassVar[option]
    holes_fill: typing.ClassVar[option]
    host_performance: typing.ClassVar[option]
    hue: typing.ClassVar[option]
    humidity_temperature: typing.ClassVar[option]
    inter_cam_sync_mode: typing.ClassVar[option]
    invalidation_bypass: typing.ClassVar[option]
    laser_power: typing.ClassVar[option]
    ldd_temperature: typing.ClassVar[option]
    led_power: typing.ClassVar[option]
    left_ir_temperature: typing.ClassVar[option]
    lld_temperature: typing.ClassVar[option]
    ma_temperature: typing.ClassVar[option]
    max_distance: typing.ClassVar[option]
    mc_temperature: typing.ClassVar[option]
    min_distance: typing.ClassVar[option]
    motion_module_temperature: typing.ClassVar[option]
    motion_range: typing.ClassVar[option]
    noise_estimation: typing.ClassVar[option]
    noise_filtering: typing.ClassVar[option]
    ohm_temperature: typing.ClassVar[option]
    output_trigger_enabled: typing.ClassVar[option]
    post_processing_sharpening: typing.ClassVar[option]
    power_line_frequency: typing.ClassVar[option]
    pre_processing_sharpening: typing.ClassVar[option]
    projector_temperature: typing.ClassVar[option]
    readout_shaping: typing.ClassVar[option]
    receiver_gain: typing.ClassVar[option]
    receiver_sensitivity: typing.ClassVar[option]
    region_of_interest: typing.ClassVar[option]
    reset_camera_accuracy_health: typing.ClassVar[option]
    rgb_tnr_enabled: typing.ClassVar[option]
    rotation: typing.ClassVar[option]
    safety_mcu_temperature: typing.ClassVar[option]
    safety_mode: typing.ClassVar[option]
    safety_preset_active_index: typing.ClassVar[option]
    saturation: typing.ClassVar[option]
    sensor_mode: typing.ClassVar[option]
    sensors_config_mode: typing.ClassVar[option]
    sequence_id: typing.ClassVar[option]
    sequence_name: typing.ClassVar[option]
    sequence_size: typing.ClassVar[option]
    sharpness: typing.ClassVar[option]
    soc_pvt_temperature: typing.ClassVar[option]
    stereo_baseline: typing.ClassVar[option]
    stream_filter: typing.ClassVar[option]
    stream_format_filter: typing.ClassVar[option]
    stream_index_filter: typing.ClassVar[option]
    texture_source: typing.ClassVar[option]
    thermal_compensation: typing.ClassVar[option]
    threshold: typing.ClassVar[option]
    total_frame_drops: typing.ClassVar[option]
    transmitter_frequency: typing.ClassVar[option]
    trigger_camera_accuracy_health: typing.ClassVar[option]
    unknown: typing.ClassVar[option]
    vertical_binning: typing.ClassVar[option]
    visual_preset: typing.ClassVar[option]
    white_balance: typing.ClassVar[option]
    zero_order_enabled: typing.ClassVar[option]
    zero_order_point_x: typing.ClassVar[option]
    zero_order_point_y: typing.ClassVar[option]
    @staticmethod
    def __str__(*args, **kwargs):
        """
        name(self: object) -> str
        """
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class option_type:
    """
    The different types option values can take on
    
    Members:
    
      integer
    
      float
    
      string
    
      boolean
    
      rect
    """
    __members__: typing.ClassVar[dict[str, option_type]]
    boolean: typing.ClassVar[option_type]
    float: typing.ClassVar[option_type]
    integer: typing.ClassVar[option_type]
    rect: typing.ClassVar[option_type]
    string: typing.ClassVar[option_type]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class l500_visual_preset:
    """
    For L500 devices: provides optimized settings (presets) for specific types of usage.
    
    Members:
    
      custom
    
      default
    
      no_ambient_light
    
      low_ambient_light
    
      max_range
    
      short_range
    
      automatic
    """
    __members__: typing.ClassVar[dict[str, l500_visual_preset]]
    automatic: typing.ClassVar[l500_visual_preset]
    custom: typing.ClassVar[l500_visual_preset]
    default: typing.ClassVar[l500_visual_preset]
    low_ambient_light: typing.ClassVar[l500_visual_preset]
    max_range: typing.ClassVar[l500_visual_preset]
    no_ambient_light: typing.ClassVar[l500_visual_preset]
    short_range: typing.ClassVar[l500_visual_preset]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class rs400_visual_preset:
    """
    For D400 devices: provides optimized settings (presets) for specific types of usage.
    
    Members:
    
      custom
    
      default
    
      hand
    
      high_accuracy
    
      high_density
    
      medium_density
    
      remove_ir_pattern
    """
    __members__: typing.ClassVar[dict[str, rs400_visual_preset]]
    custom: typing.ClassVar[rs400_visual_preset]
    default: typing.ClassVar[rs400_visual_preset]
    hand: typing.ClassVar[rs400_visual_preset]
    high_accuracy: typing.ClassVar[rs400_visual_preset]
    high_density: typing.ClassVar[rs400_visual_preset]
    medium_density: typing.ClassVar[rs400_visual_preset]
    remove_ir_pattern: typing.ClassVar[rs400_visual_preset]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class playback_status:
    """
    Members:
    
      unknown
    
      playing
    
      paused
    
      stopped
    """
    __members__: typing.ClassVar[dict[str, playback_status]]
    paused: typing.ClassVar[playback_status]
    playing: typing.ClassVar[playback_status]
    stopped: typing.ClassVar[playback_status]
    unknown: typing.ClassVar[playback_status]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class calibration_type:
    """
    Calibration type for use in device_calibration
    
    Members:
    
      auto_depth_to_rgb
    
      manual_depth_to_rgb
    
      thermal
    """
    __members__: typing.ClassVar[dict[str, calibration_type]]
    auto_depth_to_rgb: typing.ClassVar[calibration_type]
    manual_depth_to_rgb: typing.ClassVar[calibration_type]
    thermal: typing.ClassVar[calibration_type]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class calibration_status:
    """
    Calibration callback status for use in device_calibration.trigger_device_calibration
    
    Members:
    
      bad_conditions
    
      bad_result
    
      scene_invalid
    
      failed
    
      retry
    
      triggered
    
      special_frame
    
      started
    
      not_needed
    
      successful
    """
    __members__: typing.ClassVar[dict[str, calibration_status]]
    bad_conditions: typing.ClassVar[calibration_status]
    bad_result: typing.ClassVar[calibration_status]
    failed: typing.ClassVar[calibration_status]
    not_needed: typing.ClassVar[calibration_status]
    retry: typing.ClassVar[calibration_status]
    scene_invalid: typing.ClassVar[calibration_status]
    special_frame: typing.ClassVar[calibration_status]
    started: typing.ClassVar[calibration_status]
    successful: typing.ClassVar[calibration_status]
    triggered: typing.ClassVar[calibration_status]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class d500_intercam_sync_mode:
    """
    For D500: intercamera synchronization mode
    
    Members:
    
      none
    
      rgb_master
    
      pwm_master
    
      external_master
    """
    __members__: typing.ClassVar[dict[str, d500_intercam_sync_mode]]
    external_master: typing.ClassVar[d500_intercam_sync_mode]
    none: typing.ClassVar[d500_intercam_sync_mode]
    pwm_master: typing.ClassVar[d500_intercam_sync_mode]
    rgb_master: typing.ClassVar[d500_intercam_sync_mode]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class intrinsics:
    """
    Video stream intrinsics.
    """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def coeffs(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]:
        """
        Distortion coefficients
        """
    @coeffs.setter
    def coeffs(self, arg1: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]) -> None:
        ...
    @property
    def fx(self) -> float:
        """
        Focal length of the image plane, as a multiple of pixel width
        """
    @fx.setter
    def fx(self, arg0: float) -> None:
        ...
    @property
    def fy(self) -> float:
        """
        Focal length of the image plane, as a multiple of pixel height
        """
    @fy.setter
    def fy(self, arg0: float) -> None:
        ...
    @property
    def height(self) -> int:
        """
        Height of the image in pixels
        """
    @height.setter
    def height(self, arg0: int) -> None:
        ...
    @property
    def model(self) -> distortion:
        """
        Distortion model of the image
        """
    @model.setter
    def model(self, arg0: distortion) -> None:
        ...
    @property
    def ppx(self) -> float:
        """
        Horizontal coordinate of the principal point of the image, as a pixel offset from the left edge
        """
    @ppx.setter
    def ppx(self, arg0: float) -> None:
        ...
    @property
    def ppy(self) -> float:
        """
        Vertical coordinate of the principal point of the image, as a pixel offset from the top edge
        """
    @ppy.setter
    def ppy(self, arg0: float) -> None:
        ...
    @property
    def width(self) -> int:
        """
        Width of the image in pixels
        """
    @width.setter
    def width(self, arg0: int) -> None:
        ...
class motion_device_intrinsic:
    """
    Motion device intrinsics: scale, bias, and variances.
    """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def bias_variances(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        Variance of bias for X, Y, and Z axis
        """
    @bias_variances.setter
    def bias_variances(self, arg1: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        ...
    @property
    def data(self) -> typing.Annotated[list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(4)]], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        3x4 matrix with 3x3 scale and cross axis and 3x1 biases
        """
    @data.setter
    def data(self, arg1: typing.Annotated[list[typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(4)]], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        ...
    @property
    def noise_variances(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        Variance of noise for X, Y, and Z axis
        """
    @noise_variances.setter
    def noise_variances(self, arg1: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        ...
class vector:
    """
    3D vector in Euclidean coordinate space.
    """
    x: float
    y: float
    z: float
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class quaternion:
    """
    Quaternion used to represent rotation.
    """
    w: float
    x: float
    y: float
    z: float
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class combined_motion:
    """
    IMU combined GYRO & ACCEL data
    """
    angular_velocity: vector
    linear_acceleration: vector
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class pose:
    def __init__(self) -> None:
        ...
    @property
    def acceleration(self) -> vector:
        """
        X, Y, Z values of acceleration, in meters/sec^2
        """
    @acceleration.setter
    def acceleration(self, arg0: vector) -> None:
        ...
    @property
    def angular_acceleration(self) -> vector:
        """
        X, Y, Z values of angular acceleration, in radians/sec^2
        """
    @angular_acceleration.setter
    def angular_acceleration(self, arg0: vector) -> None:
        ...
    @property
    def angular_velocity(self) -> vector:
        """
        X, Y, Z values of angular velocity, in radians/sec
        """
    @angular_velocity.setter
    def angular_velocity(self, arg0: vector) -> None:
        ...
    @property
    def mapper_confidence(self) -> int:
        """
        Pose map confidence 0x0 - Failed, 0x1 - Low, 0x2 - Medium, 0x3 - High
        """
    @mapper_confidence.setter
    def mapper_confidence(self, arg0: int) -> None:
        ...
    @property
    def rotation(self) -> quaternion:
        """
        Qi, Qj, Qk, Qr components of rotation as represented in quaternion rotation (relative to initial position)
        """
    @rotation.setter
    def rotation(self, arg0: quaternion) -> None:
        ...
    @property
    def tracker_confidence(self) -> int:
        """
        Pose confidence 0x0 - Failed, 0x1 - Low, 0x2 - Medium, 0x3 - High
        """
    @tracker_confidence.setter
    def tracker_confidence(self, arg0: int) -> None:
        ...
    @property
    def translation(self) -> vector:
        """
        X, Y, Z values of translation, in meters (relative to initial position)
        """
    @translation.setter
    def translation(self, arg0: vector) -> None:
        ...
    @property
    def velocity(self) -> vector:
        """
        X, Y, Z values of velocity, in meters/sec
        """
    @velocity.setter
    def velocity(self, arg0: vector) -> None:
        ...
class extrinsics:
    """
    Cross-stream extrinsics: encodes the topology describing how the different devices are oriented.
    """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def rotation(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(9)]:
        """
        Column - major 3x3 rotation matrix
        """
    @rotation.setter
    def rotation(self, arg1: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(9)]) -> None:
        ...
    @property
    def translation(self) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        Three-element translation vector, in meters
        """
    @translation.setter
    def translation(self, arg1: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        ...
class product_line:
    """
    Members:
    
      any
    
      any_intel
    
      non_intel
    
      sw_only
    
      D400
    
      D500
    
      SR300
    
      L500
    
      T200
    
      DEPTH
    
      TRACKING
    """
    D400: typing.ClassVar[product_line]
    D500: typing.ClassVar[product_line]
    DEPTH: typing.ClassVar[product_line]
    L500: typing.ClassVar[product_line]
    SR300: typing.ClassVar[product_line]
    T200: typing.ClassVar[product_line]
    TRACKING: typing.ClassVar[product_line]
    __members__: typing.ClassVar[dict[str, product_line]]
    any: typing.ClassVar[product_line]
    any_intel: typing.ClassVar[product_line]
    non_intel: typing.ClassVar[product_line]
    sw_only: typing.ClassVar[product_line]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class option_range:
    default: float
    max: float
    min: float
    step: float
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, min: float, max: float, step: float, default: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
class region_of_interest:
    max_x: int
    max_y: int
    min_x: int
    min_y: int
    def __init__(self) -> None:
        ...
class calib_location:
    """
    Calib Location
    
    Members:
    
      eeprom
    
      flash
    
      ram
    """
    __members__: typing.ClassVar[dict[str, calib_location]]
    eeprom: typing.ClassVar[calib_location]
    flash: typing.ClassVar[calib_location]
    ram: typing.ClassVar[calib_location]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class safety_mode:
    """
    Safety Mode
    
    Members:
    
      run
    
      standby
    
      service
    """
    __members__: typing.ClassVar[dict[str, safety_mode]]
    run: typing.ClassVar[safety_mode]
    service: typing.ClassVar[safety_mode]
    standby: typing.ClassVar[safety_mode]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class embedded_filter_type:
    """
    Embedded Filter Type
    
    Members:
    
      decimation
    
      temporal
    
      improved_close_range_depth
    """
    __members__: typing.ClassVar[dict[str, embedded_filter_type]]
    decimation: typing.ClassVar[embedded_filter_type]
    improved_close_range_depth: typing.ClassVar[embedded_filter_type]
    temporal: typing.ClassVar[embedded_filter_type]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BufData:
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
class stream_profile:
    """
    Stores details about the profile of a stream.
    """
    def __bool__(self) -> bool:
        """
        Checks if the profile is valid
        """
    def __init__(self) -> None:
        ...
    def __nonzero__(self) -> bool:
        """
        Checks if the profile is valid
        """
    def __repr__(self) -> str:
        ...
    def as_motion_stream_profile(self) -> ...:
        ...
    def as_perception_stream_profile(self) -> ...:
        ...
    def as_pose_stream_profile(self) -> ...:
        ...
    def as_stream_profile(self) -> stream_profile:
        ...
    def as_video_stream_profile(self) -> ...:
        ...
    def bytes_per_pixel(self) -> int:
        ...
    def clone(self, type: stream, index: int, format: format) -> stream_profile:
        """
        Clone the current profile and change the type, index and format to input parameters
        """
    def format(self) -> format:
        """
        The stream's format
        """
    def fps(self) -> int:
        """
        The streams framerate
        """
    def get_extrinsics_to(self, to: stream_profile) -> extrinsics:
        """
        Get the extrinsic transformation between two profiles (representing physical sensors)
        """
    def is_default(self) -> bool:
        """
        Checks if the stream profile is marked/assigned as default, meaning that the profile will be selected when the user requests stream configuration using wildcards.
        """
    def is_motion_stream_profile(self) -> bool:
        ...
    def is_perception_stream_profile(self) -> bool:
        ...
    def is_pose_stream_profile(self) -> bool:
        ...
    def is_stream_profile(self) -> bool:
        ...
    def is_video_stream_profile(self) -> bool:
        ...
    def register_extrinsics_to(self, to: stream_profile, extrinsics: extrinsics) -> None:
        """
        Assign extrinsic transformation parameters to a specific profile (sensor). The extrinsic information is generally available as part of the camera calibration, and librealsense is responsible for retrieving and assigning these parameters where appropriate. This specific function is intended for synthetic/mock-up (software) devices for which the parameters are produced and injected by the user.
        """
    def stream_index(self) -> int:
        """
        The stream's index
        """
    def stream_name(self) -> str:
        """
        The stream's human-readable name.
        """
    def stream_type(self) -> stream:
        """
        The stream's type
        """
    def unique_id(self) -> int:
        """
        Unique index assigned whent the stream was created
        """
class video_stream_profile(stream_profile):
    """
    Stream profile instance which contains additional video attributes.
    """
    def __init__(self, sp: stream_profile) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def get_intrinsics(self) -> intrinsics:
        """
        Get stream profile instrinsics attributes.
        """
    def height(self) -> int:
        ...
    def width(self) -> int:
        ...
    @property
    def intrinsics(self) -> intrinsics:
        """
        Stream profile instrinsics attributes. Identical to calling get_intrinsics.
        """
class motion_stream_profile(stream_profile):
    """
    Stream profile instance which contains IMU-specific intrinsics.
    """
    def __init__(self, sp: stream_profile) -> None:
        ...
    def get_motion_intrinsics(self) -> motion_device_intrinsic:
        """
        Returns scale and bias of a motion stream.
        """
class pose_stream_profile(stream_profile):
    """
    Stream profile instance with an explicit pose extension type.
    """
    def __init__(self, sp: stream_profile) -> None:
        ...
class perception_stream_profile(stream_profile):
    """
    Stream profile for perception streams.
    """
    def __init__(self, sp: stream_profile) -> None:
        ...
class filter_interface:
    """
    Interface for frame filtering functionality
    """
    def process(self, frame: ...) -> ...:
        ...
class frame:
    """
    Base class for multiple frame extensions
    """
    def __bool__(self) -> bool:
        """
        check if internal frame handle is valid
        """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: frame) -> None:
        ...
    def __nonzero__(self) -> bool:
        """
        check if internal frame handle is valid
        """
    def __repr__(self) -> str:
        ...
    def as_depth_frame(self) -> ...:
        ...
    def as_frame(self) -> frame:
        ...
    def as_frameset(self) -> ...:
        ...
    def as_gpu_frame(self) -> ...:
        ...
    def as_labeled_points(self) -> ...:
        ...
    def as_motion_frame(self) -> ...:
        ...
    def as_object_detection_frame(self) -> ...:
        ...
    def as_perception_frame(self) -> ...:
        ...
    def as_points(self) -> ...:
        ...
    def as_pose_frame(self) -> ...:
        ...
    def as_video_frame(self) -> ...:
        ...
    def get_data(self) -> BufData:
        """
        Retrieve data from the frame handle.
        """
    def get_data_size(self) -> int:
        """
        Retrieve data size from frame handle.
        """
    def get_frame_metadata(self, frame_metadata: frame_metadata_value) -> int:
        """
        Retrieve the current value of a single frame_metadata.
        """
    def get_frame_number(self) -> int:
        """
        Retrieve the frame number.
        """
    def get_frame_timestamp_domain(self) -> timestamp_domain:
        """
        Retrieve the timestamp domain.
        """
    def get_gpu_data_or_upload(self) -> typing.Any:
        """
        Always returns a usable CUDA device pointer on a CUDA build as a (address:int, copied:bool) tuple: zero-copy when available (copied=False), otherwise the SDK uploads to a cached device buffer (copied=True). Returns None on non-CUDA builds. Consume the address via CuPy/PyCUDA/Numba/TensorRT; keep the frame alive until the GPU work completes.
        """
    def get_profile(self) -> stream_profile:
        """
        Retrieve stream profile from frame handle.
        """
    def get_timestamp(self) -> float:
        """
        Retrieve the time at which the frame was captured
        """
    def is_depth_frame(self) -> bool:
        ...
    def is_frame(self) -> bool:
        ...
    def is_frameset(self) -> bool:
        ...
    def is_gpu_frame(self) -> bool:
        ...
    def is_labeled_points(self) -> bool:
        ...
    def is_motion_frame(self) -> bool:
        ...
    def is_object_detection_frame(self) -> bool:
        ...
    def is_perception_frame(self) -> bool:
        ...
    def is_points(self) -> bool:
        ...
    def is_pose_frame(self) -> bool:
        ...
    def is_video_frame(self) -> bool:
        ...
    def keep(self) -> None:
        """
        Keep the frame, otherwise if no refernce to the frame, the frame will be released.
        """
    def supports_frame_metadata(self, frame_metadata: frame_metadata_value) -> bool:
        """
        Determine if the device allows a specific metadata to be queried.
        """
    def swap(self, other: frame) -> None:
        """
        Swap the internal frame handle with the one in parameter
        """
    @property
    def data(self) -> BufData:
        """
        Data from the frame handle. Identical to calling get_data.
        """
    @property
    def frame_number(self) -> int:
        """
        The frame number. Identical to calling get_frame_number.
        """
    @property
    def frame_timestamp_domain(self) -> timestamp_domain:
        """
        The timestamp domain. Identical to calling get_frame_timestamp_domain.
        """
    @property
    def profile(self) -> stream_profile:
        """
        Stream profile from frame handle. Identical to calling get_profile.
        """
    @property
    def timestamp(self) -> float:
        """
        Time at which the frame was captured. Identical to calling get_timestamp.
        """
class video_frame(frame):
    """
    Extends the frame class with additional video related attributes and functions.
    """
    def __init__(self, arg0: frame) -> None:
        ...
    def extract_target_dimensions(self, arg0: calib_target_type) -> list[float]:
        """
        This will calculate the four target dimenson size(s) in millimeter on the specific target.
        """
    def get_bits_per_pixel(self) -> int:
        """
        Retrieve bits per pixel.
        """
    def get_bytes_per_pixel(self) -> int:
        """
        Retrieve bytes per pixel.
        """
    def get_height(self) -> int:
        """
        Returns image height in pixels.
        """
    def get_stride_in_bytes(self) -> int:
        """
        Retrieve frame stride, meaning the actual line width in memory in bytes (not the logical image width).
        """
    def get_width(self) -> int:
        """
        Returns image width in pixels.
        """
    @property
    def bits_per_pixel(self) -> int:
        """
        Bits per pixel. Identical to calling get_bits_per_pixel.
        """
    @property
    def bytes_per_pixel(self) -> int:
        """
        Bytes per pixel. Identical to calling get_bytes_per_pixel.
        """
    @property
    def height(self) -> int:
        """
        Image height in pixels. Identical to calling get_height.
        """
    @property
    def stride_in_bytes(self) -> int:
        """
        Frame stride, meaning the actual line width in memory in bytes (not the logical image width). Identical to calling get_stride_in_bytes.
        """
    @property
    def width(self) -> int:
        """
        Image width in pixels. Identical to calling get_width.
        """
class vertex:
    x: float
    y: float
    z: float
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
class texture_coordinate:
    u: float
    v: float
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
class object_detection:
    bottom_right_x: int
    bottom_right_y: int
    class_id: int
    depth: float
    score: int
    top_left_x: int
    top_left_y: int
    def __repr__(self) -> str:
        ...
class points(frame):
    """
    Extends the frame class with additional point cloud related attributes and functions.
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: frame) -> None:
        ...
    def export_to_ply(self, arg0: str, arg1: video_frame) -> None:
        """
        Export the point cloud to a PLY file
        """
    def get_texture_coordinates(self, dims: int = 1) -> BufData:
        """
        Retrieve the texture coordinates (uv map) for the point cloud
        """
    def get_vertices(self, dims: int = 1) -> BufData:
        """
        Retrieve the vertices of the point cloud
        """
    def size(self) -> int:
        ...
class depth_frame(video_frame):
    """
    Extends the video_frame class with additional depth related attributes and functions.
    """
    def __init__(self, arg0: frame) -> None:
        ...
    def get_distance(self, x: int, y: int) -> float:
        """
        Provide the depth in meters at the given pixel
        """
    def get_units(self) -> float:
        """
        Provide the scaling factor to use when converting from get_data() units to meters
        """
class disparity_frame(depth_frame):
    """
    Extends the depth_frame class with additional disparity related attributes and functions.
    """
    def __init__(self, arg0: frame) -> None:
        ...
    def get_baseline(self) -> float:
        """
        Retrieve the distance between the two IR sensors.
        """
class motion_frame(frame):
    """
    Extends the frame class with additional motion related attributes and functions
    """
    def __init__(self, arg0: frame) -> None:
        ...
    def get_combined_motion_data(self) -> combined_motion:
        """
        Retrieve motion data from a MOTION sensor
        """
    def get_motion_data(self) -> vector:
        """
        Retrieve motion data from a GYRO/ACCEL sensor
        """
    @property
    def motion_data(self) -> vector:
        """
        Motion data from IMU sensor. Identical to calling get_motion_data.
        """
class pose_frame(frame):
    """
    Extends the frame class with additional pose related attributes and functions.
    """
    def __init__(self, arg0: frame) -> None:
        ...
    def get_pose_data(self) -> pose:
        """
        Retrieve the pose data from T2xx position tracking sensor.
        """
    @property
    def pose_data(self) -> pose:
        """
        Pose data from T2xx position tracking sensor. Identical to calling get_pose_data.
        """
class labeled_points(frame):
    """
    Extends the frame class with additional labeled points related attributes and functions.
    """
    def __init__(self, arg0: frame) -> None:
        ...
    def get_bpp(self) -> int:
        """
        Returns labeled point cloud bpp (bits per pixel).
        """
    def get_height(self) -> int:
        """
        Returns labeled point cloud height in pixels.
        """
    def get_labels(self) -> BufData:
        """
        Retrieve the labels of the labeled point cloud
        """
    def get_vertices(self) -> BufData:
        """
        Retrieve the vertices of the labeled point cloud
        """
    def get_width(self) -> int:
        """
        Returns labeled point cloud width in pixels.
        """
    @property
    def height(self) -> int:
        """
        labeled point cloud height in pixels. Identical to calling get_height.
        """
    @property
    def width(self) -> int:
        """
        labeled point cloud width in pixels. Identical to calling get_width.
        """
class perception_frame(frame):
    """
    Extends the frame class with attributes inferred from the frame content, such as object detection results.
    """
    def __init__(self, arg0: frame) -> None:
        ...
class object_detection_frame(perception_frame):
    """
    Extends perception_frame class with additional object detection related attributes and functions.
    """
    def __init__(self, arg0: frame) -> None:
        ...
    def get_detection(self, index: int) -> object_detection:
        """
        Get a specific detection by index
        """
    def get_detection_count(self) -> int:
        """
        Get the number of detected objects in this frame
        """
class gpu_frame(frame):
    """
    Extends the frame class for a GPU-resident (zero-copy) frame on integrated-GPU CUDA builds. Reach it with frame.as(gpu_frame); the cast is null unless the frame is GPU-resident.
    """
    def __init__(self, arg0: frame) -> None:
        ...
    def get_gpu_data(self) -> typing.Any:
        """
        Retrieve the CUDA device pointer aliasing the frame data for zero-copy GPU consumption (CuPy/PyCUDA/Numba/TensorRT). Returns the device address as an int, or None if unavailable. Keep the frame alive until the GPU work completes.
        """
class composite_frame(frame):
    """
    Extends the frame class with additional frameset related attributes and functions
    """
    @typing.overload
    def __getitem__(self, arg0: int) -> frame:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list[frame]:
        ...
    def __init__(self, arg0: frame) -> None:
        ...
    def __iter__(self) -> typing.Iterator[frame]:
        ...
    def __len__(self) -> int:
        """
        Return the size of the frameset
        """
    def first(self, s: stream, f: format = ...) -> frame:
        """
        Retrieve the first frame of a specific stream type and optionally with a specific format. If no frame is found, an error will be thrown.
        """
    def first_or_default(self, s: stream, f: format = ...) -> frame:
        """
        Retrieve the first frame of a specific stream and optionally with a specific format. If no frame is found, return an empty frame instance.
        """
    def foreach(self, callable: typing.Callable[[frame], None]) -> None:
        """
        Extract internal frame handles from the frameset and invoke the action function
        """
    def get_color_frame(self, index: int = 0) -> video_frame:
        """
        Retrieve the first color frame, if no frame is found, search for the color frame from IR stream. If one still can't be found, return an empty frame instance.
        """
    def get_depth_frame(self) -> depth_frame:
        """
        Retrieve the first depth frame, if no frame is found, return an empty frame instance.
        """
    def get_fisheye_frame(self, index: int = 0) -> video_frame:
        """
        Retrieve the fisheye monochrome video frame
        """
    def get_infrared_frame(self, index: int = 0) -> video_frame:
        """
        Retrieve the first infrared frame, if no frame is found, return an empty frame instance.
        """
    def get_labeled_point_cloud_frame(self) -> labeled_points:
        """
        Retrieve the labeled point cloud frame, if no frame is found, return an empty frame instance.
        """
    def get_object_detection_frame(self, index: int = 0) -> object_detection_frame:
        """
        Retrieve the object detection frame, if no frame is found, return an empty frame instance.
        """
    def get_pose_frame(self, index: int = 0) -> pose_frame:
        """
        Retrieve the pose frame
        """
    def size(self) -> int:
        """
        Return the size of the frameset
        """
class option_value:
    id: option
    type: option_type
    value: typing.Any
    def __repr__(self) -> str:
        ...
class options_list:
    def __getitem__(self, arg0: int) -> option_value:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
class options:
    """
    Base class for options interface. Should be used via sensor or processing_block.
    """
    def get_option(self, option: option) -> float:
        """
        Read option value from the device.
        """
    def get_option_description(self, option: option) -> str:
        """
        Get option description.
        """
    def get_option_range(self, option: option) -> option_range:
        """
        Retrieve the available range of values of a supported option
        """
    def get_option_value(self, arg0: option) -> option_value:
        ...
    def get_option_value_description(self, option: option, value: float) -> str:
        """
        Get option value description (In case a specific option value holds special meaning)
        """
    def get_supported_options(self) -> list[option]:
        """
        Retrieve list of supported options
        """
    def is_option_read_only(self, option: option) -> bool:
        """
        Check if particular option is read only.
        """
    def on_options_changed(self, callback: typing.Callable[[options_list], None]) -> None:
        """
        Sets a callback to notify in case options in this container change value
        """
    def set_option(self, option: option, value: float) -> None:
        """
        Write new value to device option
        """
    def set_option_value(self, arg0: option, arg1: json) -> None:
        ...
    def supports(self, option: option) -> bool:
        """
        Check if particular option is supported by a subdevice
        """
class frame_source:
    """
    The source used to generate frames, which is usually done by the low level driver for each sensor. frame_source is one of the parameters of processing_block's callback function, which can be used to re-generate the frame and via frame_ready invoke another callback function to notify application frame is ready.
    """
    def allocate_composite_frame(self, frames: list[frame]) -> frame:
        """
        Allocate composite frame with given params
        """
    def allocate_motion_frame(self, profile: stream_profile, original: frame, frame_type: extension = ...) -> frame:
        """
        Allocate a new motion frame with given params
        """
    def allocate_points(self, profile: stream_profile, original: frame) -> frame:
        ...
    def allocate_video_frame(self, profile: stream_profile, original: frame, new_bpp: int = 0, new_width: int = 0, new_height: int = 0, new_stride: int = 0, frame_type: extension = ...) -> frame:
        """
        Allocate a new video frame with given params
        """
    def frame_ready(self, result: frame) -> None:
        """
        Invoke the callback funtion informing the frame is ready.
        """
class frame_queue:
    """
    Frame queues are the simplest cross-platform synchronization primitive provided by librealsense to help developers who are not using async APIs.
    """
    def __call__(self, f: frame) -> None:
        """
        Identical to calling enqueue.
        """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, capacity: int, keep_frames: bool = False) -> None:
        ...
    def capacity(self) -> int:
        """
        Return the capacity of the queue.
        """
    def enqueue(self, f: frame) -> None:
        """
        Enqueue a new frame into the queue.
        """
    def keep_frames(self) -> bool:
        """
        Return whether or not the queue calls keep on enqueued frames.
        """
    def poll_for_frame(self) -> frame:
        """
        Poll if a new frame is available and dequeue it if it is
        """
    def size(self) -> int:
        """
        Number of enqueued frames.
        """
    def try_wait_for_frame(self, timeout_ms: int = 5000) -> tuple[bool, frame]:
        ...
    def wait_for_frame(self, timeout_ms: int = 5000) -> frame:
        """
        Wait until a new frame becomes available in the queue and dequeue it.
        """
class processing_block(options):
    """
    Define the processing block workflow, inherit this class to generate your own processing_block.
    """
    def __init__(self, processing_function: typing.Callable[[frame, frame_source], None]) -> None:
        ...
    def get_info(self, arg0: camera_info) -> str:
        """
        Retrieve camera specific information, like versions of various internal components.
        """
    def invoke(self, f: frame) -> None:
        """
        Ask processing block to process the frame
        """
    def start(self, callback: typing.Callable[[frame], None]) -> None:
        """
        Start the processing block with callback function to inform the application the frame is processed.
        """
    def supports(self, arg0: camera_info) -> bool:
        """
        Check if a specific camera info field is supported.
        """
class filter(processing_block, filter_interface):
    """
    Define the filter workflow, inherit this class to generate your own filter.
    """
    def __bool__(self) -> bool:
        ...
    def __init__(self, filter_function: typing.Callable[[frame, frame_source], None], queue_size: int = 1) -> None:
        ...
    def __nonzero__(self) -> bool:
        ...
    def as_decimation_filter(self) -> ...:
        ...
    def as_disparity_transform(self) -> ...:
        ...
    def as_hdr_merge(self) -> ...:
        ...
    def as_hole_filling_filter(self) -> ...:
        ...
    def as_rotation_filter(self) -> ...:
        ...
    def as_sequence_id_filter(self) -> ...:
        ...
    def as_spatial_filter(self) -> ...:
        ...
    def as_temporal_filter(self) -> ...:
        ...
    def as_threshold_filter(self) -> ...:
        ...
    def is_decimation_filter(self) -> bool:
        ...
    def is_disparity_transform(self) -> bool:
        ...
    def is_hdr_merge(self) -> bool:
        ...
    def is_hole_filling_filter(self) -> bool:
        ...
    def is_rotation_filter(self) -> bool:
        ...
    def is_sequence_id_filter(self) -> bool:
        ...
    def is_spatial_filter(self) -> bool:
        ...
    def is_temporal_filter(self) -> bool:
        ...
    def is_threshold_filter(self) -> bool:
        ...
class pointcloud(filter):
    """
    Generates 3D point clouds based on a depth frame. Can also map textures from a color frame.
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, stream: stream, index: int = 0) -> None:
        ...
    def calculate(self, depth: frame) -> points:
        """
        Generate the pointcloud and texture mappings of depth map.
        """
    def map_to(self, mapped: frame) -> None:
        """
        Map the point cloud to the given color frame.
        """
class yuy_decoder(filter):
    """
    Converts frames in raw YUY format to RGB. This conversion is somewhat costly, but the SDK will automatically try to use SSE2, AVX, or CUDA instructions where available to get better performance. Othere implementations (GLSL, OpenCL, Neon, NCS) should follow.
    """
    def __init__(self) -> None:
        ...
class threshold_filter(filter):
    """
    Depth thresholding filter. By controlling min and max options on the block, one could filter out depth values that are either too large or too small, as a software post-processing step
    """
    def __init__(self, min_dist: float = 0.15000000596046448, max_dist: float = 4.0) -> None:
        ...
class units_transform(filter):
    def __init__(self) -> None:
        ...
class syncer:
    """
    Sync instance to align frames from different streams
    """
    def __init__(self, queue_size: int = 1) -> None:
        ...
    def poll_for_frame(self) -> composite_frame:
        """
        Check if a coherent set of frames is available
        """
    def poll_for_frames(self) -> composite_frame:
        """
        Check if a coherent set of frames is available
        """
    def try_wait_for_frame(self, timeout_ms: int = 5000) -> tuple[bool, composite_frame]:
        ...
    def try_wait_for_frames(self, timeout_ms: int = 5000) -> tuple[bool, composite_frame]:
        ...
    def wait_for_frame(self, timeout_ms: int = 5000) -> composite_frame:
        """
        Wait until a coherent set of frames becomes available
        """
    def wait_for_frames(self, timeout_ms: int = 5000) -> composite_frame:
        """
        Wait until a coherent set of frames becomes available
        """
class align(filter):
    """
    Performs alignment between depth image and another image.
    """
    def __init__(self, align_to: stream) -> None:
        """
        To perform alignment of a depth image to the other, set the align_to parameter with the other stream type.
        To perform alignment of a non depth image to a depth image, set the align_to parameter to RS2_STREAM_DEPTH.
        Camera calibration and frame's stream type are determined on the fly, according to the first valid frameset passed to process().
        """
    def process(self, frames: composite_frame) -> composite_frame:
        """
        Run thealignment process on the given frames to get an aligned set of frames
        """
class colorizer(filter):
    """
    Colorizer filter generates color images based on input depth frame
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, color_scheme: float) -> None:
        """
        Possible values for color_scheme:
        0 - Jet
        1 - Classic
        2 - WhiteToBlack
        3 - BlackToWhite
        4 - Bio
        5 - Cold
        6 - Warm
        7 - Quantized
        8 - Pattern
        """
    def colorize(self, depth: frame) -> video_frame:
        """
        Start to generate color image base on depth frame
        """
class decimation_filter(filter):
    """
    Performs downsampling by using the median with specific kernel size.
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, magnitude: float) -> None:
        ...
class rotation_filter(filter):
    """
    Performs rotation of frames.
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, value: list[stream]) -> None:
        ...
class temporal_filter(filter):
    """
    Temporal filter smooths the image by calculating multiple frames with alpha and delta settings. Alpha defines the weight of current frame, and delta defines thethreshold for edge classification and preserving.
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, smooth_alpha: float, smooth_delta: float, persistence_control: int) -> None:
        """
        Possible values for persistence_control:
        1 - Valid in 8/8 - Persistency activated if the pixel was valid in 8 out of the last 8 frames
        2 - Valid in 2 / last 3 - Activated if the pixel was valid in two out of the last 3 frames
        3 - Valid in 2 / last 4 - Activated if the pixel was valid in two out of the last 4 frames
        4 - Valid in 2 / 8 - Activated if the pixel was valid in two out of the last 8 frames
        5 - Valid in 1 / last 2 - Activated if the pixel was valid in one of the last two frames
        6 - Valid in 1 / last 5 - Activated if the pixel was valid in one out of the last 5 frames
        7 - Valid in 1 / last 8 - Activated if the pixel was valid in one out of the last 8 frames
        8 - Persist Indefinitely - Persistency will be imposed regardless of the stored history(most aggressive filtering)
        """
class spatial_filter(filter):
    """
    Spatial filter smooths the image by calculating frame with alpha and delta settings. Alpha defines the weight of the current pixel for smoothing, and is bounded within [25..100]%. Delta defines the depth gradient below which the smoothing will occur as number of depth levels.
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, smooth_alpha: float, smooth_delta: float, magnitude: float, hole_fill: float) -> None:
        ...
class disparity_transform(filter):
    """
    Converts from depth representation to disparity representation and vice - versa in depth frames
    """
    def __init__(self, transform_to_disparity: bool = True) -> None:
        ...
class hole_filling_filter(filter):
    """
    The processing performed depends on the selected hole filling mode.
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, mode: int) -> None:
        """
        Possible values for mode:
        0 - fill_from_left - Use the value from the left neighbor pixel to fill the hole
        1 - farest_from_around - Use the value from the neighboring pixel which is furthest away from the sensor
        2 - nearest_from_around - -Use the value from the neighboring pixel closest to the sensor
        """
class hdr_merge(filter):
    """
    Merges depth frames with different sequence ID
    """
    def __init__(self) -> None:
        ...
class sequence_id_filter(filter):
    """
    Splits depth frames with different sequence ID
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, sequence_id: float) -> None:
        ...
class embedded_filter(options):
    """
    Define the embedded filter workflow.
    """
    def __bool__(self) -> bool:
        ...
    def as_embedded_decimation_filter(self) -> ...:
        ...
    def as_embedded_temporal_filter(self) -> ...:
        ...
    def get_type(self) -> embedded_filter_type:
        """
        Get the embedded filter type
        """
    def is_embedded_decimation_filter(self) -> bool:
        ...
    def is_embedded_temporal_filter(self) -> bool:
        ...
class embedded_decimation_filter(embedded_filter):
    """
    Define the embedded decimation filter workflow.
    """
class embedded_temporal_filter(embedded_filter):
    """
    Define the embedded temporal filter workflow.
    """
class notification:
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def get_category(self) -> notification_category:
        """
        Retrieve the notification's category.
        """
    def get_description(self) -> str:
        """
        Retrieve the notification's description.
        """
    def get_serialized_data(self) -> log_severity:
        """
        Retrieve the notification's serialized data.
        """
    def get_severity(self) -> log_severity:
        """
        Retrieve the notification's severity.
        """
    def get_timestamp(self) -> float:
        """
        Retrieve the notification's arrival timestamp.
        """
    @property
    def category(self) -> notification_category:
        """
        The notification's category. Identical to calling get_category.
        """
    @property
    def description(self) -> str:
        """
        The notification's description. Identical to calling get_description.
        """
    @property
    def serialized_data(self) -> str:
        """
        The notification's serialized data. Identical to calling get_serialized_data.
        """
    @property
    def severity(self) -> log_severity:
        """
        The notification's severity. Identical to calling get_severity.
        """
    @property
    def timestamp(self) -> float:
        """
        The notification's arrival timestamp. Identical to calling get_timestamp.
        """
class sensor(options):
    @staticmethod
    def from_frame(frame: frame) -> sensor:
        ...
    def __bool__(self) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def __nonzero__(self) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def as_color_sensor(self) -> ...:
        ...
    def as_debug_stream_sensor(self) -> ...:
        ...
    def as_depth_sensor(self) -> ...:
        ...
    def as_fisheye_sensor(self) -> ...:
        ...
    def as_max_usable_range_sensor(self) -> ...:
        ...
    def as_motion_sensor(self) -> ...:
        ...
    def as_perception_sensor(self) -> ...:
        ...
    def as_pose_sensor(self) -> ...:
        ...
    def as_roi_sensor(self) -> ...:
        ...
    def as_safety_sensor(self) -> ...:
        ...
    def as_wheel_odometer(self) -> ...:
        ...
    def close(self) -> None:
        """
        Close sensor for exclusive access.
        """
    def get_active_streams(self) -> list[stream_profile]:
        """
        Retrieves the list of stream profiles currently streaming on the sensor.
        """
    def get_embedded_close_range_filter(self) -> ...:
        """
        Return the embedded Improved Close Range Depth filter in the sensor.
        """
    def get_embedded_decimation_filter(self) -> embedded_decimation_filter:
        """
        Return the embedded decimation filter in the sensor.
        """
    def get_embedded_filter(self, filter_type: embedded_filter_type) -> embedded_filter:
        """
        Return the embedded filter in the sensor by filter type.
        """
    def get_embedded_temporal_filter(self) -> embedded_temporal_filter:
        """
        Return the embedded temporal filter in the sensor.
        """
    def get_info(self, info: camera_info) -> str:
        """
        Retrieve camera specific information, like versions of various internal components.
        """
    def get_recommended_filters(self) -> list[filter]:
        """
        Return the recommended list of filters by the sensor.
        """
    def get_stream_profiles(self) -> list[stream_profile]:
        """
        Retrieves the list of stream profiles supported by the sensor.
        """
    def is_color_sensor(self) -> bool:
        ...
    def is_debug_stream_sensor(self) -> bool:
        ...
    def is_depth_sensor(self) -> bool:
        ...
    def is_fisheye_sensor(self) -> bool:
        ...
    def is_max_usable_range_sensor(self) -> bool:
        ...
    def is_motion_sensor(self) -> bool:
        ...
    def is_perception_sensor(self) -> bool:
        ...
    def is_pose_sensor(self) -> bool:
        ...
    def is_roi_sensor(self) -> bool:
        ...
    def is_safety_sensor(self) -> bool:
        ...
    def is_wheel_odometer(self) -> bool:
        ...
    @typing.overload
    def open(self, profile: stream_profile) -> None:
        """
        Open sensor for exclusive access, by commiting to a configuration
        """
    @typing.overload
    def open(self, profiles: list[stream_profile]) -> None:
        """
        Open sensor for exclusive access, by committing to a composite configuration, specifying one or more stream profiles.
        """
    def query_embedded_filters(self) -> list[embedded_filter]:
        """
        Return the list of embedded filters in the sensor.
        """
    def set_notifications_callback(self, callback: typing.Callable[[notification], None]) -> None:
        """
        Register Notifications callback
        """
    @typing.overload
    def start(self, callback: typing.Callable[[frame], None]) -> None:
        """
        Start passing frames into user provided callback.
        """
    @typing.overload
    def start(self, syncer: syncer) -> None:
        """
        Start passing frames into user provided syncer.
        """
    @typing.overload
    def start(self, queue: frame_queue) -> None:
        """
        start passing frames into specified frame_queue
        """
    def stop(self) -> None:
        """
        Stop streaming.
        """
    @typing.overload
    def supports(self, arg0: camera_info) -> bool:
        """
        info
        """
    @typing.overload
    def supports(self, arg0: option) -> bool:
        """
        info
        """
    @property
    def name(self) -> str:
        ...
    @property
    def profiles(self) -> list[stream_profile]:
        """
        The list of stream profiles supported by the sensor. Identical to calling get_stream_profiles
        """
class roi_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
    def get_region_of_interest(self) -> region_of_interest:
        ...
    def set_region_of_interest(self, roi: region_of_interest) -> None:
        ...
class depth_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
    def get_depth_scale(self) -> float:
        """
        Retrieves mapping between the units of the depth image and meters.
        """
class color_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
class motion_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
class fisheye_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
class perception_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
class safety_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
    def get_application_config(self) -> str:
        """
        get application config
        """
    def get_safety_interface_config(self, calib_location: calib_location = ...) -> str:
        """
        get safety interface config
        """
    def get_safety_preset(self, index: int) -> str:
        """
        get safety preset at index
        """
    def set_application_config(self, application_config_json_str: str) -> None:
        """
        set application config
        """
    def set_safety_interface_config(self, safety_interface_config: str) -> None:
        """
        set safety interface config
        """
    def set_safety_preset(self, index: int, safety_preset: str) -> None:
        """
        set safety preset at index
        """
class max_usable_range_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
    def get_max_usable_depth_range(self) -> float:
        ...
class debug_stream_sensor(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
    def get_debug_stream_profiles(self) -> list[stream_profile]:
        ...
class depth_stereo_sensor(depth_sensor):
    def __init__(self, arg0: sensor) -> None:
        ...
    def get_stereo_baseline(self) -> float:
        """
        Retrieve the stereoscopic baseline value from the sensor.
        """
class pose_sensor(sensor):
    @staticmethod
    def remove_static_node(*args, **kwargs):
        """
        remove_static_node(self: pyrealsense2.pyrealsense2.pose_sensor, Removes a named virtual landmark in the current map, known as static node.
        guid: str) -> bool
        """
    def __bool__(self) -> bool:
        ...
    def __init__(self, sensor: sensor) -> None:
        ...
    def __nonzero__(self) -> bool:
        ...
    def export_localization_map(self) -> list[int]:
        """
        Get relocalization map that is currently on device, created and updated during most recent tracking session.
        Can be called before or after stop().
        """
    def get_static_node(self, guid: str) -> tuple[bool, vector, quaternion]:
        """
        Gets the current pose of a static node that was created in the current map or in an imported map.
        Static nodes of imported maps are available after relocalizing the imported map.
        The static node's pose is returned relative to the current origin of coordinates of device poses.
        Thus, poses of static nodes of an imported map are consistent with current device poses after relocalization.
        This function fails if the current tracker confidence is below 3 (high confidence).
        """
    def import_localization_map(self, lmap_buf: list[int]) -> bool:
        """
        Load relocalization map onto device. Only one relocalization map can be imported at a time; any previously existing map will be overwritten.
        The imported map exists simultaneously with the map created during the most recent tracking session after start(),and they are merged after the imported map is relocalized.
        This operation must be done before start().
        """
    def set_static_node(self, guid: str, pos: vector, orient: quaternion) -> bool:
        """
        Creates a named virtual landmark in the current map, known as static node.
        The static node's pose is provided relative to the origin of current coordinate system of device poses.
        This function fails if the current tracker confidence is below 3 (high confidence).
        """
class wheel_odometer(sensor):
    def __init__(self, sensor: sensor) -> None:
        ...
    def load_wheel_odometery_config(self, odometry_config_buf: list[int]) -> bool:
        """
        Load Wheel odometer settings from host to device.
        """
    def send_wheel_odometry(self, wo_sensor_id: int, frame_num: int, translational_velocity: vector) -> bool:
        """
        Send wheel odometry data for each individual sensor (wheel)
        """
class device:
    def __bool__(self) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def __nonzero__(self) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def as_auto_calibrated_device(self) -> ...:
        ...
    def as_calibration_change_device(self) -> ...:
        ...
    def as_debug_protocol(self) -> ...:
        ...
    def as_device_calibration(self) -> ...:
        ...
    def as_firmware_logger(self) -> ...:
        ...
    def as_playback(self) -> ...:
        ...
    def as_recorder(self) -> ...:
        ...
    def as_updatable(self) -> ...:
        ...
    def as_update_device(self) -> ...:
        ...
    def first_color_sensor(self) -> color_sensor:
        ...
    def first_depth_sensor(self) -> depth_sensor:
        ...
    def first_fisheye_sensor(self) -> fisheye_sensor:
        ...
    def first_motion_sensor(self) -> motion_sensor:
        ...
    def first_perception_sensor(self) -> perception_sensor:
        ...
    def first_pose_sensor(self) -> pose_sensor:
        ...
    def first_roi_sensor(self) -> roi_sensor:
        ...
    def first_safety_sensor(self) -> safety_sensor:
        ...
    def get_device_time_ms(self) -> float:
        """
        Retrieve the current device hardware clock time in milliseconds.
        """
    def get_firmware_min_version(self) -> str:
        """
        Get the minimum firmware version supported by this device's SKU (e.g. "5.10.0.17"). Throws if the device does not implement the FW-update protocol or has no defined minimum.
        """
    def get_info(self, info: camera_info) -> str:
        """
        Retrieve camera specific information, like versions of various internal components
        """
    def hardware_reset(self) -> None:
        """
        Send hardware reset request to the device
        """
    def is_auto_calibrated_device(self) -> bool:
        ...
    def is_calibration_change_device(self) -> bool:
        ...
    def is_connected(self) -> bool:
        ...
    def is_debug_protocol(self) -> bool:
        ...
    def is_device_calibration(self) -> bool:
        ...
    def is_firmware_logger(self) -> bool:
        ...
    def is_in_recovery_mode(self) -> bool:
        ...
    def is_metadata_enabled(self) -> bool:
        ...
    def is_playback(self) -> bool:
        ...
    def is_recorder(self) -> bool:
        ...
    def is_updatable(self) -> bool:
        ...
    def is_update_device(self) -> bool:
        ...
    def query_sensors(self) -> list[sensor]:
        """
        Returns the list of adjacent devices, sharing the same physical parent composite device.
        """
    def supports(self, info: camera_info) -> bool:
        """
        Check if specific camera info is supported.
        """
    @property
    def sensors(self) -> list[sensor]:
        """
        List of adjacent devices, sharing the same physical parent composite device. Identical to calling query_sensors.
        """
class updatable(device):
    def __init__(self, arg0: device) -> None:
        ...
    def check_firmware_compatibility(self, image: list[int]) -> bool:
        """
        Check firmware compatibility with device. This method should be called before burning a signed firmware.
        """
    @typing.overload
    def create_flash_backup(self) -> list[int]:
        """
        Create backup of camera flash memory. Such backup does not constitute valid firmware image, and cannot be loaded back to the device, but it does contain all calibration and device information.
        """
    @typing.overload
    def create_flash_backup(self, callback: typing.Callable[[float], None]) -> list[int]:
        """
        Create backup of camera flash memory. Such backup does not constitute valid firmware image, and cannot be loaded back to the device, but it does contain all calibration and device information.
        """
    def enter_update_state(self) -> None:
        """
        Move the device to update state, this will cause the updatable device to disconnect and reconnect as an update device.
        """
    @typing.overload
    def update_unsigned(self, fw_image: list[int], update_mode: int = 0) -> None:
        """
        Update an updatable device to the provided unsigned firmware. This call is executed on the caller's thread.
        """
    @typing.overload
    def update_unsigned(self, fw_image: list[int], callback: typing.Callable[[float], None], update_mode: int = 0) -> None:
        """
        Update an updatable device to the provided unsigned firmware. This call is executed on the caller's thread and provides progress notifications via the callback.
        """
class update_device(device):
    def __init__(self, arg0: device) -> None:
        ...
    @typing.overload
    def update(self, fw_image: list[int]) -> None:
        """
        Update an updatable device to the provided firmware. This call is executed on the caller's thread.
        """
    @typing.overload
    def update(self, fw_image: list[int], callback: typing.Callable[[float], None]) -> None:
        """
        Update an updatable device to the provided firmware. This call is executed on the caller's thread and provides progress notifications via the callback.
        """
class auto_calibrated_device(device):
    def __init__(self, device: device) -> None:
        ...
    @typing.overload
    def calculate_target_z(self, queue1: frame_queue, queue2: frame_queue, queue3: frame_queue, target_width_mm: float, target_height_mm: float) -> float:
        """
        Calculate Z for calibration target - distance to the target's plane.
        """
    @typing.overload
    def calculate_target_z(self, queue1: frame_queue, queue2: frame_queue, queue3: frame_queue, target_width_mm: float, target_height_mm: float, callback: typing.Callable[[float], None]) -> float:
        """
        Calculate Z for calibration target - distance to the target's plane. This call is executed on the caller's thread and provides progress notifications via the callback.
        """
    def get_calibration_config(self) -> str:
        """
        Get Calibration Config Table
        """
    def get_calibration_table(self) -> list[int]:
        """
        Read current calibration table from flash.
        """
    @typing.overload
    def process_calibration_frame(self, frame: frame, timeout_ms: int) -> tuple[list[int], tuple[float, float]]:
        """
        This will add a frame to the calibration process initiated by run_tare_calibration or run_on_chip_calibration as host assistant process. This call is executed on the caller's thread  and it supports progress notifications via the callback.
        """
    @typing.overload
    def process_calibration_frame(self, frame: frame, callback: typing.Callable[[float], None], timeout_ms: int) -> tuple[list[int], tuple[float, float]]:
        """
        This will add a frame to the calibration process initiated by run_tare_calibration or run_on_chip_calibration as host assistant process. This call is executed on the caller's thread and it supports progress notifications via the callback.
        """
    def reset_to_factory_calibration(self) -> None:
        """
        Reset device to factory calibration.
        """
    @typing.overload
    def run_focal_length_calibration(self, left_queue: frame_queue, right_queue: frame_queue, target_width_mm: float, target_heigth_mm: float, adjust_both_sides: int) -> tuple[list[int], float, float]:
        """
        Run target-based focal length calibration. This call is executed on the caller's thread.
        """
    @typing.overload
    def run_focal_length_calibration(self, left_queue: frame_queue, right_queue: frame_queue, target_width_mm: float, target_heigth_mm: float, adjust_both_sides: int, callback: typing.Callable[[float], None]) -> tuple[list[int], float, float]:
        """
        Run target-based focal length calibration. This call is executed on the caller's thread and provides progress notifications via the callback.
        """
    @typing.overload
    def run_on_chip_calibration(self, json_content: str, timeout_ms: int) -> tuple[list[int], tuple[float, float]]:
        """
        This will improve the depth noise (plane fit RMS). This call is executed on the caller's thread.
        """
    @typing.overload
    def run_on_chip_calibration(self, json_content: str, callback: typing.Callable[[float], None], timeout_ms: int) -> tuple[list[int], tuple[float, float]]:
        """
        This will improve the depth noise (plane fit RMS). This call is executed on the caller's thread and provides progress notifications via the callback.
        """
    @typing.overload
    def run_tare_calibration(self, ground_truth_mm: float, json_content: str, timeout_ms: int) -> tuple[list[int], tuple[float, float]]:
        """
        This will adjust camera absolute distance to flat target. This call is executed on the caller's thread.
        """
    @typing.overload
    def run_tare_calibration(self, ground_truth_mm: float, json_content: str, callback: typing.Callable[[float], None], timeout_ms: int) -> tuple[list[int], tuple[float, float]]:
        """
        This will adjust camera absolute distance to flat target. This call is executed on the caller's thread and it supports progress notifications via the callback.
        """
    @typing.overload
    def run_uv_map_calibration(self, left: frame_queue, color: frame_queue, depth: frame_queue, py_px_only: int) -> tuple[list[int], float]:
        """
        Run target-based Depth-RGB UV-map calibraion. This call is executed on the caller's thread.
        """
    @typing.overload
    def run_uv_map_calibration(self, left: frame_queue, color: frame_queue, depth: frame_queue, py_px_only: int, callback: typing.Callable[[float], None]) -> tuple[list[int], float]:
        """
        Run target-based Depth-RGB UV-map calibraion. This call is executed on the caller's thread and provides progress notifications via the callback.
        """
    def set_calibration_config(self, calibration_config_json_str: str) -> None:
        """
        Set Calibration Config Table
        """
    def set_calibration_table(self, arg0: list[int]) -> None:
        """
        Set current table to dynamic area.
        """
    def write_calibration(self) -> None:
        """
        Write calibration that was set by set_calibration_table to device's EEPROM.
        """
class device_calibration(device):
    def __init__(self, device: device) -> None:
        ...
    def register_calibration_change_callback(self, callback: typing.Callable[[calibration_status], None]) -> None:
        """
        Register (only once!) a callback that gets called for each change in calibration
        """
    def trigger_device_calibration(self, calibration_type: calibration_type) -> None:
        """
        Trigger the given calibration, if available
        """
class calibration_change_device(device):
    def __init__(self, device: device) -> None:
        ...
    def register_calibration_change_callback(self, callback: typing.Callable[[calibration_status], None]) -> None:
        """
        Register (only once!) a callback that gets called for each change in calibration
        """
class debug_protocol:
    def __init__(self, arg0: device) -> None:
        ...
    def build_command(self, opcode: int, param1: int = 0, param2: int = 0, param3: int = 0, param4: int = 0, data: list[int] = []) -> list[int]:
        ...
    def send_and_receive_raw_data(self, input: list[int]) -> list[int]:
        ...
class device_list:
    @typing.overload
    def __getitem__(self, arg0: int) -> device:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list[device]:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self) -> typing.Iterator[device]:
        ...
    def __len__(self) -> int:
        ...
    def back(self) -> device:
        ...
    def contains(self, arg0: device) -> bool:
        ...
    def front(self) -> device:
        ...
    def size(self) -> int:
        ...
class playback(device):
    def __init__(self, device: device) -> None:
        ...
    def current_status(self) -> playback_status:
        """
        Returns the current state of the playback device
        """
    def file_name(self) -> str:
        """
        The name of the playback file.
        """
    def get_duration(self) -> datetime.timedelta:
        """
        Retrieves the total duration of the file.
        """
    def get_position(self) -> int:
        """
        Retrieves the current position of the playback in the file in terms of time. Units are expressed in nanoseconds.
        """
    def is_real_time(self) -> bool:
        """
        Indicates if playback is in real time mode or non real time.
        """
    def pause(self) -> None:
        """
        Pauses the playback. Calling pause() in "Paused" status does nothing. If pause() is called while playback status is "Playing" or "Stopped", the playback will not play until resume() is called.
        """
    def resume(self) -> None:
        """
        Un-pauses the playback. Calling resume() while playback status is "Playing" or "Stopped" does nothing.
        """
    def seek(self, time: datetime.timedelta) -> None:
        """
        Sets the playback to a specified time point of the played data.
        """
    def set_real_time(self, real_time: bool) -> None:
        """
        Set the playback to work in real time or non real time. In real time mode, playback will play the same way the file was recorded. If the application takes too long to handle the callback, frames may be dropped. In non real time mode, playback will wait for each callback to finish handling the data before reading the next frame. In this mode no frames will be dropped, and the application controls the framerate of playback via callback duration.
        """
    def set_status_changed_callback(self, callback: typing.Callable[[playback_status], None]) -> None:
        """
        Register to receive callback from playback device upon its status changes. Callbacks are invoked from the reading thread, and as such any heavy processing in the callback handler will affect the reading thread and may cause frame drops/high latency.
        """
class recorder(device):
    """
    Records the given device and saves it to the given file as rosbag format.
    """
    @typing.overload
    def __init__(self, arg0: str, arg1: device) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: device, arg2: bool) -> None:
        ...
    def pause(self) -> None:
        """
        Pause the recording device without stopping the actual device from streaming.
        """
    def resume(self) -> None:
        """
        Unpauses the recording device, making it resume recording.
        """
class event_information:
    def get_new_devices(self) -> device_list:
        """
        Returns a list of all newly connected devices
        """
    def was_added(self, dev: device) -> bool:
        """
        Check if a specific device was added.
        """
    def was_removed(self, dev: device) -> bool:
        """
        Check if a specific device was disconnected.
        """
class context:
    """
    Librealsense context class. Includes realsense API version.
    """
    @staticmethod
    @typing.overload
    def __init__(*args, **kwargs) -> None:
        ...
    @staticmethod
    @typing.overload
    def __init__(*args, **kwargs) -> None:
        ...
    def convert_bag_to_db3(self, input: str, output: str) -> None:
        """
        Convert a legacy ROS1 .bag recording to a ROS2 .db3 file.
        """
    def get_sensor_parent(self, s: sensor) -> device:
        ...
    def load_device(self, filename: str) -> playback:
        """
        Creates a devices from a RealSense file.
        On successful load, the device will be appended to the context and a devices_changed event triggered.
        """
    def query_all_sensors(self) -> list[sensor]:
        """
        Generate a flat list of all available sensors from all RealSense devices.
        """
    @typing.overload
    def query_devices(self) -> device_list:
        """
        Create a static snapshot of all connected devices at the time of the call.
        """
    @typing.overload
    def query_devices(self, arg0: int) -> device_list:
        """
        Create a static snapshot of all connected devices of specific product line at the time of the call.
        """
    def set_devices_changed_callback(self, callback: typing.Callable[[event_information], None]) -> None:
        """
        Register devices changed callback.
        """
    def unload_device(self, filename: str) -> None:
        ...
    def unload_tracking_module(self) -> None:
        ...
    @property
    def devices(self) -> device_list:
        """
        A static snapshot of all connected devices at time of access. Identical to calling query_devices.
        """
    @property
    def sensors(self) -> list[sensor]:
        """
        A flat list of all available sensors from all RealSense devices. Identical to calling query_all_sensors.
        """
class device_hub:
    """
    Encapsulates connect/disconnect handling and waiting for devices.
    """
    def __init__(self, ctx: context) -> None:
        """
        Create a device_hub bound to the given context.
        """
    def is_connected(self, device: device) -> bool:
        """
        Return True if the given device is still connected.
        """
    def wait_for_device(self) -> device:
        """
        If a device is connected return it, otherwise wait until one connects.
        """
class pipeline_profile:
    """
    The pipeline profile includes a device and a selection of active streams, with specific profiles.
    The profile is a selection of the above under filters and conditions defined by the pipeline.
    Streams may belong to more than one sensor of the device.
    """
    def __init__(self) -> None:
        ...
    def get_device(self) -> device:
        """
        Retrieve the device used by the pipeline.
        The device class provides the application access to control camera additional settings - get device information, sensor options information, options value query and set, sensor specific extensions.
        Since the pipeline controls the device streams configuration, activation state and frames reading, calling the device API functions, which execute those operations, results in unexpected behavior.
        The pipeline streaming device is selected during pipeline start(). Devices of profiles, which are not returned by pipeline start() or get_active_profile(), are not guaranteed to be used by the pipeline.
        """
    def get_stream(self, stream_type: stream, stream_index: int = -1) -> stream_profile:
        """
        Return the stream profile that is enabled for the specified stream in this profile.
        """
    def get_streams(self) -> list[stream_profile]:
        """
        Return the selected streams profiles, which are enabled in this profile.
        """
class pipeline_wrapper:
    def __init__(self, arg0: ...) -> None:
        ...
class config:
    """
    The config allows pipeline users to request filters for the pipeline streams and device selection and configuration.
    This is an optional step in pipeline creation, as the pipeline resolves its streaming device internally.
    Config provides its users a way to set the filters and test if there is no conflict with the pipeline requirements from the device.
    It also allows the user to find a matching device for the config filters and the pipeline, in order to select a device explicitly, and modify its controls before streaming starts.
    """
    def __init__(self) -> None:
        ...
    def can_resolve(self, p: pipeline_wrapper) -> bool:
        """
        Check if the config can resolve the configuration filters, to find a matching device and streams profiles. The resolution conditions are as described in resolve().
        """
    def disable_all_streams(self) -> None:
        """
        Disable all device stream explicitly, to remove any requests on the streams profiles.
        The streams can still be enabled due to pipeline computer vision module request. This call removes any filter on the streams configuration.
        """
    def disable_stream(self, stream: stream, index: int = -1) -> None:
        """
        Disable a device stream explicitly, to remove any requests on this stream profile.
        The stream can still be enabled due to pipeline computer vision module request. This call removes any filter on the stream configuration.
        """
    def enable_all_streams(self) -> None:
        """
        Enable all device streams explicitly.
        The conditions and behavior of this method are similar to those of enable_stream().
        This filter enables all raw streams of the selected device. The device is either selected explicitly by the application, or by the pipeline requirements or default. The list of streams is device dependent.
        """
    def enable_device(self, serial: str) -> None:
        """
        Select a specific device explicitly by its serial number, to be used by the pipeline.
        The conditions and behavior of this method are similar to those of enable_stream().
        This method is required if the application needs to set device or sensor settings prior to pipeline streaming, to enforce the pipeline to use the configured device.
        """
    def enable_device_from_file(self, file_name: str, repeat_playback: bool = True) -> None:
        """
        Select a recorded device from a file, to be used by the pipeline through playback.
        The device available streams are as recorded to the file, and resolve() considers only this device and configuration as available.
        This request cannot be used if enable_record_to_file() is called for the current config, and vice versa.
        """
    def enable_record_to_file(self, file_name: str) -> None:
        """
        Requires that the resolved device would be recorded to file.
        This request cannot be used if enable_device_from_file() is called for the current config, and vice versa as available.
        """
    @typing.overload
    def enable_stream(self, stream_type: stream, stream_index: int, width: int, height: int, format: format, framerate: int) -> None:
        """
        Enable a device stream explicitly, with selected stream parameters.
        The method allows the application to request a stream with specific configuration.
        If no stream is explicitly enabled, the pipeline configures the device and its streams according to the attached computer vision modules and processing blocks requirements, or default configuration for the first available device.
        The application can configure any of the input stream parameters according to its requirement, or set to 0 for don't care value.
        The config accumulates the application calls for enable configuration methods, until the configuration is applied.
        Multiple enable stream calls for the same stream override each other, and the last call is maintained.
        Upon calling resolve(), the config checks for conflicts between the application configuration requests and the attached computer vision modules and processing blocks requirements, and fails if conflicts are found.
        Before resolve() is called, no conflict check is done.
        """
    @typing.overload
    def enable_stream(self, stream_type: stream) -> None:
        """
        Stream type only. Other parameters are resolved internally.
        """
    @typing.overload
    def enable_stream(self, stream_type: stream, stream_index: int) -> None:
        """
        Stream type and possibly also stream index. Other parameters are resolved internally.
        """
    @typing.overload
    def enable_stream(self, stream_type: stream, format: format, framerate: int) -> None:
        """
        Stream type and format, and possibly frame rate. Other parameters are resolved internally.
        """
    @typing.overload
    def enable_stream(self, stream_type: stream, width: int, height: int, format: format, framerate: int) -> None:
        """
        Stream type and resolution, and possibly format and frame rate. Other parameters are resolved internally.
        """
    @typing.overload
    def enable_stream(self, stream_type: stream, stream_index: int, format: format, framerate: int) -> None:
        """
        Stream type, index, and format, and possibly framerate. Other parameters are resolved internally.
        """
    def resolve(self, p: pipeline_wrapper) -> pipeline_profile:
        """
        Resolve the configuration filters, to find a matching device and streams profiles.
        The method resolves the user configuration filters for the device and streams, and combines them with the requirements of the computer vision modules and processing blocks attached to the pipeline. If there are no conflicts of requests, it looks for an available device, which can satisfy all requests, and selects the first matching streams configuration.
        In the absence of any request, the config object selects the first available device and the first color and depth streams configuration.The pipeline profile selection during start() follows the same method. Thus, the selected profile is the same, if no change occurs to the available devices.Resolving the pipeline configuration provides the application access to the pipeline selected device for advanced control.The returned configuration is not applied to the device, so the application doesn't own the device sensors. However, the application can call enable_device(), to enforce the device returned by this method is selected by pipeline start(), and configure the device and sensors options or extensions before streaming starts.
        """
class pipeline:
    """
    The pipeline simplifies the user interaction with the device and computer vision processing modules.
    The class abstracts the camera configuration and streaming, and the vision modules triggering and threading.
    It lets the application focus on the computer vision output of the modules, or the device output data.
    The pipeline can manage computer vision modules, which are implemented as a processing blocks.
    The pipeline is the consumer of the processing block interface, while the application consumes the computer vision interface.
    """
    @typing.overload
    def __init__(self) -> None:
        """
        With a default context
        """
    @typing.overload
    def __init__(self, ctx: context) -> None:
        """
        The caller can provide a context created by the application, usually for playback or testing purposes
        """
    def get_active_profile(self) -> pipeline_profile:
        ...
    def poll_for_frames(self) -> composite_frame:
        """
        Check if a new set of frames is available and retrieve the latest undelivered set.
        The frames set includes time-synchronized frames of each enabled stream in the pipeline.
        The method returns without blocking the calling thread, with status of new frames available or not.
        If available, it fetches the latest frames set.
        Device frames, which were produced while the function wasn't called, are dropped.
        To avoid frame drops, this method should be called as fast as the device frame rate.
        The application can maintain the frames handles to defer processing. However, if the application maintains too long history, the device may lack memory resources to produce new frames, and the following calls to this method shall return no new frames, until resources become available.
        """
    def set_device(self, device: device) -> None:
        """
        The function is used to assign the device, useful when the user wish to set controls that cannot be set while streaming. 
        """
    @typing.overload
    def start(self) -> pipeline_profile:
        """
        Start the pipeline streaming with its default configuration.
        The pipeline streaming loop captures samples from the device, and delivers them to the attached computer vision modules and processing blocks, according to each module requirements and threading model.
        During the loop execution, the application can access the camera streams by calling wait_for_frames() or poll_for_frames().
        The streaming loop runs until the pipeline is stopped.
        Starting the pipeline is possible only when it is not started. If the pipeline was started, an exception is raised.
        """
    @typing.overload
    def start(self, config: config) -> pipeline_profile:
        """
        Start the pipeline streaming according to the configuraion.
        The pipeline streaming loop captures samples from the device, and delivers them to the attached computer vision modules and processing blocks, according to each module requirements and threading model.
        During the loop execution, the application can access the camera streams by calling wait_for_frames() or poll_for_frames().
        The streaming loop runs until the pipeline is stopped.
        Starting the pipeline is possible only when it is not started. If the pipeline was started, an exception is raised.
        The pipeline selects and activates the device upon start, according to configuration or a default configuration.
        When the rs2::config is provided to the method, the pipeline tries to activate the config resolve() result.
        If the application requests are conflicting with pipeline computer vision modules or no matching device is available on the platform, the method fails.
        Available configurations and devices may change between config resolve() call and pipeline start, in case devices are connected or disconnected, or another application acquires ownership of a device.
        """
    @typing.overload
    def start(self, callback: typing.Callable[[frame], None]) -> pipeline_profile:
        """
        Start the pipeline streaming with its default configuration.
        The pipeline captures samples from the device, and delivers them to the provided frame callback.
        Starting the pipeline is possible only when it is not started. If the pipeline was started, an exception is raised.
        When starting the pipeline with a callback both wait_for_frames() and poll_for_frames() will throw exception.
        """
    @typing.overload
    def start(self, config: config, callback: typing.Callable[[frame], None]) -> pipeline_profile:
        """
        Start the pipeline streaming according to the configuraion.
        The pipeline captures samples from the device, and delivers them to the provided frame callback.
        Starting the pipeline is possible only when it is not started. If the pipeline was started, an exception is raised.
        When starting the pipeline with a callback both wait_for_frames() and poll_for_frames() will throw exception.
        The pipeline selects and activates the device upon start, according to configuration or a default configuration.
        When the rs2::config is provided to the method, the pipeline tries to activate the config resolve() result.
        If the application requests are conflicting with pipeline computer vision modules or no matching device is available on the platform, the method fails.
        Available configurations and devices may change between config resolve() call and pipeline start, in case devices are connected or disconnected, or another application acquires ownership of a device.
        """
    @typing.overload
    def start(self, queue: frame_queue) -> pipeline_profile:
        """
        Start the pipeline streaming with its default configuration.
        The pipeline captures samples from the device, and delivers them to the provided frame queue.
        Starting the pipeline is possible only when it is not started. If the pipeline was started, an exception is raised.
        When starting the pipeline with a callback both wait_for_frames() and poll_for_frames() will throw exception.
        """
    @typing.overload
    def start(self, config: config, queue: frame_queue) -> pipeline_profile:
        """
        Start the pipeline streaming according to the configuraion.
        The pipeline captures samples from the device, and delivers them to the provided frame queue.
        Starting the pipeline is possible only when it is not started. If the pipeline was started, an exception is raised.
        When starting the pipeline with a callback both wait_for_frames() and poll_for_frames() will throw exception.
        The pipeline selects and activates the device upon start, according to configuration or a default configuration.
        When the rs2::config is provided to the method, the pipeline tries to activate the config resolve() result.
        If the application requests are conflicting with pipeline computer vision modules or no matching device is available on the platform, the method fails.
        Available configurations and devices may change between config resolve() call and pipeline start, in case devices are connected or disconnected, or another application acquires ownership of a device.
        """
    def stop(self) -> None:
        """
        Stop the pipeline streaming.
        The pipeline stops delivering samples to the attached computer vision modules and processing blocks, stops the device streaming and releases the device resources used by the pipeline. It is the application's responsibility to release any frame reference it owns.
        The method takes effect only after start() was called, otherwise an exception is raised.
        """
    def try_wait_for_frames(self, timeout_ms: int = 5000) -> tuple[bool, composite_frame]:
        ...
    def wait_for_frames(self, timeout_ms: int = 5000) -> composite_frame:
        """
        Wait until a new set of frames becomes available.
        The frames set includes time-synchronized frames of each enabled stream in the pipeline.
        In case of different frame rates of the streams, the frames set include a matching frame of the slow stream, which may have been included in previous frames set.
        The method blocks the calling thread, and fetches the latest unread frames set.
        Device frames, which were produced while the function wasn't called, are dropped. To avoid frame drops, this method should be called as fast as the device frame rate.
        The application can maintain the frames handles to defer processing. However, if the application maintains too long history, the device may lack memory resources to produce new frames, and the following call to this method shall fail to retrieve new frames, until resources become available.
        """
class video_stream:
    """
    All the parameters required to define a video stream.
    """
    bpp: int
    fmt: format
    fps: int
    height: int
    index: int
    intrinsics: intrinsics
    type: stream
    uid: int
    width: int
    def __init__(self) -> None:
        ...
class motion_stream:
    """
    All the parameters required to define a motion stream.
    """
    fmt: format
    fps: int
    index: int
    intrinsics: motion_device_intrinsic
    type: stream
    uid: int
    def __init__(self) -> None:
        ...
class pose_stream:
    """
    All the parameters required to define a pose stream.
    """
    fmt: format
    fps: int
    index: int
    type: stream
    uid: int
    def __init__(self) -> None:
        ...
class perception_stream:
    """
    All the parameters required to define a perception stream.
    """
    fmt: format
    fps: int
    index: int
    type: stream
    uid: int
    def __init__(self) -> None:
        ...
class software_video_frame:
    """
    All the parameters required to define a video frame
    """
    bpp: int
    depth_units: float
    domain: timestamp_domain
    frame_number: int
    profile: video_stream_profile
    stride: int
    timestamp: float
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def pixels(self) -> BufData:
        ...
    @pixels.setter
    def pixels(self, arg1: typing_extensions.Buffer) -> None:
        ...
class software_motion_frame:
    """
    All the parameters required to define a motion frame.
    """
    data: vector
    domain: timestamp_domain
    frame_number: int
    profile: motion_stream_profile
    timestamp: float
    def __init__(self) -> None:
        ...
class software_pose_frame:
    """
    All the parameters required to define a pose frame.
    """
    data: pose
    domain: timestamp_domain
    frame_number: int
    profile: pose_stream_profile
    timestamp: float
    def __init__(self) -> None:
        ...
class software_notification:
    """
    All the parameters required to define a sensor notification.
    """
    category: notification_category
    description: str
    serialized_data: str
    severity: log_severity
    type: int
    def __init__(self) -> None:
        ...
class software_sensor(sensor):
    def add_motion_stream(self, motion_stream: motion_stream, is_default: bool = False) -> stream_profile:
        """
        Add motion stream to software sensor
        """
    def add_option(self, option: option, range: option_range, is_writable: bool = True) -> None:
        """
        Register option that will be supported by the sensor
        """
    def add_perception_stream(self, perception_stream: perception_stream, is_default: bool = False) -> stream_profile:
        """
        Add perception stream to software sensor
        """
    def add_pose_stream(self, pose_stream: pose_stream, is_default: bool = False) -> stream_profile:
        """
        Add pose stream to software sensor
        """
    def add_read_only_option(self, option: option, val: float) -> None:
        """
        Register read-only option that will be supported by the sensor
        """
    def add_video_stream(self, video_stream: video_stream, is_default: bool = False) -> stream_profile:
        """
        Add video stream to software sensor
        """
    def on_motion_frame(self, frame: software_motion_frame) -> None:
        """
        Inject motion frame into the sensor
        """
    def on_notification(self, notif: software_notification) -> None:
        ...
    def on_pose_frame(self, frame: software_pose_frame) -> None:
        """
        Inject pose frame into the sensor
        """
    def on_video_frame(self, frame: software_video_frame) -> None:
        """
        Inject video frame into the sensor
        """
    def set_metadata(self, value: frame_metadata_value, type: int) -> None:
        """
        Set frame metadata for the upcoming frames
        """
    def set_read_only_option(self, option: option, val: float) -> None:
        """
        Update value of registered read-only option
        """
class software_device(device):
    def __init__(self) -> None:
        ...
    def add_sensor(self, name: str) -> software_sensor:
        """
        Add software sensor with given name to the software device.
        """
    def add_to(self, ctx: context) -> None:
        """
        Add software device to existing context.
        Any future queries on the context will return this device.
        This operation cannot be undone (except for destroying the context)
        """
    def create_matcher(self, matcher: matchers) -> None:
        """
        Set the wanted matcher type that will be used by the syncer
        """
    def register_info(self, info: camera_info, val: str) -> None:
        """
        Add a new camera info value, like serial number
        """
    def set_destruction_callback(self, callback: typing.Callable[[], None]) -> None:
        """
        Register destruction callback
        """
    def update_info(self, info: camera_info, val: str) -> None:
        """
        Update an existing camera info value, like serial number
        """
class firmware_log_message:
    def get_data(self) -> list[int]:
        """
        Get data 
        """
    def get_severity(self) -> log_severity:
        """
        Get severity 
        """
    def get_severity_str(self) -> str:
        """
        Get severity string 
        """
    def get_size(self) -> int:
        """
        Get size 
        """
    def get_timestamp(self) -> int:
        """
        Get timestamp 
        """
class firmware_log_parsed_message:
    def get_file_name(self) -> str:
        """
        Get file name 
        """
    def get_line(self) -> int:
        """
        Get line 
        """
    def get_message(self) -> str:
        """
        Get message 
        """
    def get_module_name(self) -> str:
        """
        Get module name 
        """
    def get_sequence_id(self) -> int:
        """
        Get sequence id
        """
    def get_severity(self) -> str:
        """
        Get severity 
        """
    def get_thread_name(self) -> str:
        """
        Get thread name 
        """
    def get_timestamp(self) -> int:
        """
        Get timestamp 
        """
class firmware_logger(device):
    def __init__(self, device: device) -> None:
        ...
    def create_message(self) -> firmware_log_message:
        """
        Create FW Log
        """
    def create_parsed_message(self) -> firmware_log_parsed_message:
        """
        Create FW Parsed Log
        """
    def get_firmware_log(self, msg: firmware_log_message) -> bool:
        """
        Get FW Log
        """
    def get_flash_log(self, msg: firmware_log_message) -> bool:
        """
        Get Flash Log
        """
    def get_number_of_fw_logs(self) -> int:
        """
        Get Number of Fw Logs Polled From Device
        """
    def init_parser(self, xml_content: str) -> bool:
        """
        Initialize Parser with content of xml file
        """
    def parse_log(self, msg: firmware_log_message, parsed_msg: firmware_log_parsed_message) -> bool:
        """
        Parse Fw Log 
        """
    def start_collecting(self) -> None:
        """
        Start collecting FW logs
        """
    def stop_collecting(self) -> None:
        """
        Stop collecting FW logs
        """
class terminal_parser:
    def __init__(self, xml_content: str) -> None:
        ...
    def parse_command(self, cmd: str) -> list[int]:
        """
        Parse Command 
        """
    def parse_response(self, cmd: str, response: list[int]) -> str:
        """
        Parse Response 
        """
class save_single_frameset(filter):
    def __init__(self, filename: str = 'RealSense Frameset ') -> None:
        ...
class STDepthControlGroup:
    deepSeaMedianThreshold: int
    deepSeaNeighborThreshold: int
    deepSeaSecondPeakThreshold: int
    lrAgreeThreshold: int
    minusDecrement: int
    plusIncrement: int
    scoreThreshA: int
    scoreThreshB: int
    textureCountThreshold: int
    textureDifferenceThreshold: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STRsm:
    diffThresh: float
    removeThresh: int
    rsmBypass: int
    sloRauDiffThresh: float
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STRauSupportVectorControl:
    minEast: int
    minNSsum: int
    minNorth: int
    minSouth: int
    minWEsum: int
    minWest: int
    uShrink: int
    vShrink: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STColorControl:
    disableRAUColor: int
    disableSADColor: int
    disableSADNormalize: int
    disableSLOLeftColor: int
    disableSLORightColor: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STRauColorThresholdsControl:
    rauDiffThresholdBlue: int
    rauDiffThresholdGreen: int
    rauDiffThresholdRed: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STSloColorThresholdsControl:
    diffThresholdBlue: int
    diffThresholdGreen: int
    diffThresholdRed: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STSloPenaltyControl:
    sloK1Penalty: int
    sloK1PenaltyMod1: int
    sloK1PenaltyMod2: int
    sloK2Penalty: int
    sloK2PenaltyMod1: int
    sloK2PenaltyMod2: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STHdad:
    ignoreSAD: int
    lambdaAD: float
    lambdaCensus: float
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STColorCorrection:
    colorCorrection1: float
    colorCorrection10: float
    colorCorrection11: float
    colorCorrection12: float
    colorCorrection2: float
    colorCorrection3: float
    colorCorrection4: float
    colorCorrection5: float
    colorCorrection6: float
    colorCorrection7: float
    colorCorrection8: float
    colorCorrection9: float
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STAEControl:
    meanIntensitySetPoint: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STDepthTableControl:
    depthClampMax: int
    depthClampMin: int
    depthUnits: int
    disparityMode: int
    disparityShift: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STCensusRadius:
    uDiameter: int
    vDiameter: int
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class STAFactor:
    a_factor: float
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class rs400_advanced_mode:
    def __init__(self, device: device) -> None:
        ...
    def get_ae_control(self, mode: int = 0) -> STAEControl:
        ...
    def get_amp_factor(self, mode: int = 0) -> STAFactor:
        ...
    def get_census(self, mode: int = 0) -> STCensusRadius:
        ...
    def get_color_control(self, mode: int = 0) -> STColorControl:
        ...
    def get_color_correction(self, mode: int = 0) -> STColorCorrection:
        ...
    def get_depth_control(self, mode: int = 0) -> STDepthControlGroup:
        ...
    def get_depth_table(self, mode: int = 0) -> STDepthTableControl:
        ...
    def get_hdad(self, mode: int = 0) -> STHdad:
        ...
    def get_rau_support_vector_control(self, mode: int = 0) -> STRauSupportVectorControl:
        ...
    def get_rau_thresholds_control(self, mode: int = 0) -> STRauColorThresholdsControl:
        ...
    def get_rsm(self, mode: int = 0) -> STRsm:
        ...
    def get_slo_color_thresholds_control(self, mode: int = 0) -> STSloColorThresholdsControl:
        ...
    def get_slo_penalty_control(self, mode: int = 0) -> STSloPenaltyControl:
        ...
    def is_enabled(self) -> bool:
        ...
    def load_json(self, json_content: str) -> None:
        ...
    def serialize_json(self) -> str:
        ...
    def set_ae_control(self, group: STAEControl) -> None:
        ...
    def set_amp_factor(self, group: STAFactor) -> None:
        ...
    def set_census(self, group: STCensusRadius) -> None:
        ...
    def set_color_control(self, group: STColorControl) -> None:
        ...
    def set_color_correction(self, group: STColorCorrection) -> None:
        ...
    def set_depth_control(self, group: STDepthControlGroup) -> None:
        ...
    def set_depth_table(self, group: STDepthTableControl) -> None:
        ...
    def set_hdad(self, group: STHdad) -> None:
        ...
    def set_rau_support_vector_control(self, group: STRauSupportVectorControl) -> None:
        ...
    def set_rau_thresholds_control(self, group: STRauColorThresholdsControl) -> None:
        ...
    def set_rsm(self, arg0: STRsm) -> None:
        """
        group
        """
    def set_slo_color_thresholds_control(self, group: STSloColorThresholdsControl) -> None:
        ...
    def set_slo_penalty_control(self, group: STSloPenaltyControl) -> None:
        ...
    def toggle_advanced_mode(self, enable: bool) -> None:
        ...
class serializable_device:
    def __init__(self, device: device) -> None:
        ...
    def load_json(self, json_content: str) -> None:
        ...
    def serialize_json(self) -> str:
        ...
class ip_address:
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: ip_address) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
        """
        b4
        """
    @typing.overload
    def __init__(self, arg0: int) -> None:
        """
        b
        """
    def __ne__(self, arg0: ip_address) -> bool:
        ...
    def __str__(self) -> str:
        ...
    def clear(self) -> None:
        ...
    def empty(self) -> bool:
        ...
    @typing.overload
    def get_components(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
        """
        Get IP address components
        """
    @typing.overload
    def get_components(self, arg0: int) -> None:
        """
        Get IP address components
        """
    def is_valid(self) -> bool:
        ...
class link_priority:
    """
    Members:
    
      usb_only
    
      eth_only
    
      eth_first
    
      usb_first
    
      dynamic_eth_first
    
      dynamic_usb_first
    """
    __members__: typing.ClassVar[dict[str, link_priority]]
    dynamic_eth_first: typing.ClassVar[link_priority]
    dynamic_usb_first: typing.ClassVar[link_priority]
    eth_first: typing.ClassVar[link_priority]
    eth_only: typing.ClassVar[link_priority]
    usb_first: typing.ClassVar[link_priority]
    usb_only: typing.ClassVar[link_priority]
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class eth_config_device(device):
    """
    Ethernet configuration extension for devices that support ethernet configuration
    """
    def __init__(self, device: device) -> None:
        """
        Create eth_config_device from regular device
        """
    def get_dds_domain(self) -> int:
        """
        Get current DDS domain (0-232)
        """
    def get_dhcp_config(self) -> tuple:
        """
        Get DHCP configuration. Returns tuple of (enabled, timeout)
        """
    def get_gateway(self) -> tuple:
        """
        Get current gateway address. Returns tuple of (configured_gateway, actual_gateway)
        """
    def get_ip_address(self) -> tuple:
        """
        Get current IP address. Returns tuple of (configured_ip, actual_ip)
        """
    def get_link_priority(self) -> link_priority:
        """
        Get current link priority setting
        """
    def get_link_speed(self) -> int:
        """
        Get Ethernet link speed, 0 if not linked
        """
    def get_link_timeout(self) -> int:
        """
        Get current link timeout in milliseconds
        """
    def get_mtu(self) -> int:
        """
        Get MTU (Maximum Transmission Unit) in bytes
        """
    def get_netmask(self) -> tuple:
        """
        Get current network mask. Returns tuple of (configured_netmask, actual_netmask)
        """
    def get_transmission_delay(self) -> int:
        """
        Get transmission delay in microseconds
        """
    def get_udp_ttl(self) -> int:
        """
        Get UDP TTL (Time To Live)
        """
    def restore_defaults(self) -> None:
        """
        Restores configuration to factory settings
        """
    def set_dds_domain(self, domain: int) -> None:
        """
        Set DDS domain (0-232)
        """
    def set_dhcp_config(self, enabled: bool, timeout: int) -> None:
        """
        Set DHCP configuration
        """
    def set_gateway(self, gateway: ip_address) -> None:
        """
        Set gateway address
        """
    def set_ip_address(self, ip: ip_address) -> None:
        """
        Set IP address
        """
    def set_link_priority(self, priority: link_priority) -> None:
        """
        Set link priority
        """
    def set_link_timeout(self, timeout: int) -> None:
        """
        Set link timeout in milliseconds
        """
    def set_mtu(self, mtu: int) -> None:
        """
        Set MTU (Maximum Transmission Unit)
        """
    def set_netmask(self, netmask: ip_address) -> None:
        """
        Set network mask
        """
    def set_transmission_delay(self, delay: int) -> None:
        """
        Set transmission delay
        """
    def set_udp_ttl(self, ttl: int) -> None:
        """
        Set UDP TTL (Time To Live)
        """
    def supports_eth_config(self) -> bool:
        """
        Check if device supports ethernet configuration
        """
class save_to_ply(filter):
    option_ignore_color: typing.ClassVar[option]
    option_ply_binary: typing.ClassVar[option]
    option_ply_mesh: typing.ClassVar[option]
    option_ply_normals: typing.ClassVar[option]
    option_ply_threshold: typing.ClassVar[option]
    def __init__(self, filename: str = 'RealSense Pointcloud ', pc: pointcloud = ...) -> None:
        ...
class log_message:
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def filename(self) -> str:
        ...
    def full(self) -> str:
        ...
    def line_number(self) -> int:
        ...
    def raw(self) -> str:
        ...
def enable_metadata() -> None:
    """
    Enable per-frame metadata at OS level for connected D400/D500 devices. Windows: writes HKLM UVC registry keys; must be called from an admin process. Throws RuntimeError on failure.
    """
def enable_rolling_log_file(max_size: int) -> None:
    ...
def log(severity: log_severity, message: str) -> None:
    ...
def log_to_callback(min_severity: log_severity, callback: typing.Callable, asynchronous: bool = False) -> None:
    ...
def log_to_console(min_severity: log_severity) -> None:
    ...
def log_to_file(min_severity: log_severity, file_path: str) -> None:
    ...
def m420_converter(target_format: format) -> filter:
    ...
def nv12_converter(target_format: format) -> filter:
    ...
def option_from_string(arg0: str) -> option:
    ...
def reset_logger() -> None:
    ...
def rs2_deproject_pixel_to_point(intrin: intrinsics, pixel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)], depth: float) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
    """
    Given pixel coordinates and depth in an image with no distortion or inverse distortion coefficients, compute the corresponding point in 3D space relative to the same camera
    """
def rs2_fov(intrin: intrinsics) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
    """
    Calculate horizontal and vertical field of view, based on video intrinsics
    """
def rs2_project_color_pixel_to_depth_pixel(data: BufData, depth_scale: float, depth_min: float, depth_max: float, depth_intrin: intrinsics, color_intrin: intrinsics, color_to_depth: extrinsics, depth_to_color: extrinsics, from_pixel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
    """
    Given pixel coordinates of the color image and a minimum and maximum depth, compute the corresponding pixel coordinates in the depth image. Returns [-1 -1] on failure.
    """
def rs2_project_point_to_pixel(intrin: intrinsics, point: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
    """
    Given a point in 3D space, compute the corresponding pixel coordinates in an image with no distortion or forward distortion coefficients produced by the same camera
    """
def rs2_transform_point_to_point(extrin: extrinsics, from_point: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
    """
    Transform 3D coordinates relative to one sensor to 3D coordinates relative to another viewpoint
    """
def supports_eth_config(device: device) -> bool:
    """
    Check if device supports ethernet configuration
    """
def uyvy_converter(target_format: format) -> filter:
    ...
def yuy2_converter(target_format: format) -> filter:
    ...
D400: product_line
D500: product_line
DEPTH: product_line
L500: product_line
SR300: product_line
T200: product_line
TRACKING: product_line
__full_version__: str = '2.58.4.10922'
__version__: str = '2.58.4'
any: product_line
any_intel: product_line
non_intel: product_line
sw_only: product_line
