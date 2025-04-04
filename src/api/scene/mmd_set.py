# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyMilkWhisky
"""
Blender Scene文件
"""
import bpy  # pylint: disable=import-error

lips_audio_path = bpy.props.StringProperty(
    name="Audio Path",
    description="Path to the Audio file.",
    default="",
    maxlen=512,
    subtype='FILE_PATH',
)

lips_start_frame = bpy.props.IntProperty(name="Start Frame", default=1)

buffer_frame = bpy.props.FloatProperty(
    name="Delayed Opening",
    description="The mouth does not open immediately upon recognition;"
                " the unit is in milliseconds,"
                " and the buffer value is calculated"
                " based on the acceleration parameters for opening the mouth",
    default=0.15,
    min=0.02,
    max=1.0)

approach_speed = bpy.props.FloatProperty(
    name="Speed Up Opening",
    description="The larger this parameter is, "
                "the greater the value of the morph key for delayed mouth opening will be.",
    default=1.6,
    min=1,
    max=10,
)

db_threshold = bpy.props.FloatProperty(
    name="DB Threshold",
    description="Minimum threshold for audio volume detection",
    default=-50.00,
    min=-65.00,
    max=0)

rms_threshold = bpy.props.FloatProperty(
    name="RMS Threshold",
    description="Minimum threshold for audio root mean square identification",
    default=0.05,
    min=0.001,
    max=1.0,
)

max_morph_value = bpy.props.FloatProperty(
    name="Max Morph Value",
    description="Threshold for the maximum value of the morphological key",
    default=0.97,
    min=0.01,
    max=1.0,
)

blink_start_frame = bpy.props.IntProperty(name="start", default=1, min=1)
blink_end_frame = bpy.props.IntProperty(name="end", default=250, min=1)

blinking_frequency = bpy.props.FloatProperty(
    name="blink interval",
    description="The interval in seconds between blinks.",
    default=4.0,
    min=1.0,
    max=3600.0,
)

blinking_wave_ratio = bpy.props.FloatProperty(
    name="blinking wave ratio",
    description="Blink interval = "
                "blink interval + "
                "rand(-fluctuation ratio, fluctuation ratio)",
    default=0.1,
    min=0,
    max=1,
)
