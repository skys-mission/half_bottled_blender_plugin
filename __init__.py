# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and EcceTal
# This file is part of ET Helper for Blender.
import sys

import bpy

from bpy.props import PointerProperty

from .translator import translations_dict
from .common import scene
from .api import ui
from .handler import resolution, camera

bl_info = {
    "name": "ET Helper",
    "author": "EcceTal <skysmission@outlook.com>",
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
        # Blender Scene for camera
        bpy.utils.register_class(scene.CameraSettingsProperties)
        bpy.types.Scene.camera_settings = PointerProperty(type=scene.CameraSettingsProperties)

        # UI
        bpy.utils.register_class(ui.RenderPresetPanel)
        bpy.utils.register_class(ui.SetCamera)

        # Render Handler
        bpy.utils.register_class(resolution.ApplyResolutionPreset)

        # Render Camera
        bpy.utils.register_class(camera.CAMERA_OT_apply_settings)

    except Exception as e:
        print(f"Register Exception: {e}")
        unregister()
        pass
    pass


def unregister():
    # original_excepthook = sys.excepthook
    # sys.excepthook = custom_excepthook
    # 卸载翻译
    bpy.app.translations.unregister(__name__)
    # 卸载摄像机功能
    bpy.types.Scene.camera_settings = PointerProperty(type=scene.CameraSettingsProperties)
    bpy.utils.unregister_class(scene.CameraSettingsProperties)
    bpy.utils.unregister_class(ui.SetCamera)
    bpy.utils.unregister_class(camera.CAMERA_OT_apply_settings)
    # 卸载Render UI
    bpy.utils.unregister_class(ui.RenderPresetPanel)
    # 卸载Render Handler
    bpy.utils.unregister_class(resolution.ApplyResolutionPreset)
    # 删除Blender Scene
    if hasattr(bpy.types.Scene, "resolution_preset"):
        del bpy.types.Scene.resolution_preset
    if hasattr(bpy.types.Scene, "aspect_ratio_preset"):
        del bpy.types.Scene.aspect_ratio_preset
    if hasattr(bpy.types.Scene, "orientation_preset"):
        del bpy.types.Scene.orientation_preset
    if hasattr(bpy.types.Scene, "camera_settings"):
        del bpy.types.Scene.camera_settings

    # sys.excepthook = original_excepthook
    pass


def custom_excepthook(exc_type, exc_value, exc_traceback):
    print(f"自定义异常处理: {exc_type.__name__}: {exc_value}")


if __name__ == "__main__":
    pass
