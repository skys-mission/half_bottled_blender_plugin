# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and EcceTal
# This file is part of ET Helper for Blender.

import bpy

from bpy.props import EnumProperty, BoolProperty, PointerProperty


# 渲染预设

def resolution_preset_callback(self, context):
    bpy.ops.render.apply_resolution_preset()


def aspect_ratio_preset_callback(self, context):
    bpy.ops.render.apply_resolution_preset()


def orientation_preset_callback(self, context):
    bpy.ops.render.apply_resolution_preset()


resolution_preset = EnumProperty(
    items=[
        ('default', 'default', 'default'),
        ('480P', '480P', 'Set resolution to 480P'),
        ('720P', '720P', 'Set resolution to 720P'),
        ('1080P', '1080P', 'Set resolution to 1080P'),
        ('2K', '2K', 'Set resolution to 2K'),
        ('4K', '4K', 'Set resolution to 4K'),
        ('8K', '8K', 'Set resolution to 8K'),
        ('16K', '16K', 'Set resolution to 16K')
    ],
    name="Resolution",
    update=resolution_preset_callback
)

aspect_ratio_preset = EnumProperty(
    items=[
        ('default', 'default', 'default'),
        ('1:1', '1:1', 'Other'),
        ('2:1', '2:1', 'Other'),
        ('2.35:1', '2.35:1', 'Old Film Standards'),
        ('2.39:1', '2.39:1 Film Standards', 'Film Standards'),
        ('4:3', '4:3', 'Old Standard'),
        ('3:2', '3:2', 'Other'),
        ('16:9', '16:9', 'Standard'),
        ('382:239', '382:239 Bilibili cover image', 'Bilibili cover image')
    ],
    name="Aspect Ratio",
    update=aspect_ratio_preset_callback
)

orientation_preset = EnumProperty(
    items=[
        ('default', 'default', 'default'),
        ('LANDSCAPE', 'Landscape', ''),
        ('PORTRAIT', 'Portrait', '')
    ],
    name="Rotate",
    update=orientation_preset_callback
)

# 摄像机

# 焦距选项
focal_lengths = [
    ('50', '50mm human eye perspective', 'human eye perspective'),
    ('14', '14mm ultra-wide field', 'Highlight background'),
    ('24', '24mm wide angle', 'scenery, street snap'),
    ('35', '35mm', '35mm'),
    ('85', '85mm classic portrait', 'classic portrait, background blur'),
    ('135', '135mm long-focus', 'long-focus, strong background blur')
]

# 光圈选项
apertures = [
    ('2.8', 'f/2.8 default', 'Background blur, portrait/night scene photography'),
    ('1.4', 'f/1.4 low light env', 'Background blur, portrait/night scene photography'),
    ('4', 'f/4 medium aperture', 'Slightly Blurred. Suitable for average lighting conditions'),
    ('5.6', 'f/5.6', 'Suitable for average lighting conditions'),
    ('8', 'f/8 small aperture', 'Requires strong lighting'),
    ('11', 'f/11', 'Requires strong lighting'),
    ('13', 'f/13', 'Requires a strong light environment'),
    ('22', 'f/22 minimum aperture', 'Requires a strong light environment'),
    ('32', 'f/32', 'f/32'),
    ('0.95', 'f/0.95', 'f/0.95')
]


class CameraSettingsProperties(bpy.types.PropertyGroup):
    focal_length: EnumProperty(
        items=focal_lengths,
        name="Focal Length",
        description="Focal Length."
    )
    aperture: EnumProperty(
        items=apertures,
        name="F-Stop",
        description="F-Stop."
    )
    depth_of_field: BoolProperty(
        name="Depth of Field",
        description="Depth of Field",
        default=False
    )
    target_object: PointerProperty(
        type=bpy.types.Object,
        name="Focus on Object",
        description="Select focus object"
    )
