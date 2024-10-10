# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and EcceTal
# This file is part of ET Helper for Blender.

import bpy

from bpy.props import EnumProperty


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
        ('2.39:1', '2.39:1', 'Film Standards'),
        ('4:3', '4:3', 'Old Standard'),
        ('3:2', '3:2', 'Other'),
        ('16:9', '16:9', 'Standard'),
        ('382:239', '382:239', 'Bilibili cover image')
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
