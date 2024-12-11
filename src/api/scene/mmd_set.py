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
    default=0.05,
    min=0.02,
    max=1.0)
approach_speed = bpy.props.FloatProperty(
    name="Speed Up Opening",
    default=3,
    min=1,
    max=10,
)
