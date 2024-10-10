# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and EcceTal
# This file is part of ET Helper for Blender.

import bpy

from .translator import translations_dict
from .common import scene
from .api import ui
from .handler import resolution

bl_info = {
    "name": "ET Helper",
    "author": "EcceTal",
    "version": (0, 1),
    "blender": (3, 6, 0),
    "location": "View3D > N-Panel  > ET Helper",
    "description": "ET Helper.",
    "category": "Interface",
}


def register():
    try:
        # 翻译
        bpy.app.translations.register(__name__, translations_dict)

        # Blender Scene
        bpy.types.Scene.resolution_preset = scene.resolution_preset
        bpy.types.Scene.aspect_ratio_preset = scene.aspect_ratio_preset
        bpy.types.Scene.orientation_preset = scene.orientation_preset

        # UI
        bpy.utils.register_class(ui.ETHelperPanel)

        # Handler
        bpy.utils.register_class(resolution.ApplyResolutionPreset)

    except Exception as e:
        print(f"Register Exception: {e}")
        unregister()
        pass
    pass


def unregister():
    # 翻译
    bpy.app.translations.unregister(__name__)
    # UI
    bpy.utils.unregister_class(ui.ETHelperPanel)
    # Handler
    bpy.utils.unregister_class(resolution.ApplyResolutionPreset)
    # 删除Blender Scene
    if hasattr(bpy.types.Scene, "resolution_preset"):
        del bpy.types.Scene.resolution_preset
    if hasattr(bpy.types.Scene, "aspect_ratio_preset"):
        del bpy.types.Scene.aspect_ratio_preset
    if hasattr(bpy.types.Scene, "orientation_preset"):
        del bpy.types.Scene.orientation_preset
    pass


if __name__ == "__main__":
    pass
