# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyMilkWhisky
"""
初始化代码
"""
from ..api.bridge import Bridge
from ..api.handler.camera import CameraApplySettingsOperator
from ..api.scene.camera_set_scene import CameraSettingsProperties
from ..api.scene.render_preset_scene import (
    resolution_preset, aspect_ratio_preset, orientation_preset)
from ..api.ui.camera_set_panel import CameraSetPanel
from ..api.ui.render_preset_panel import RenderPresetPanel


class AddonManager:
    """
    插件管理器类。
    负责插件的初始化和卸载。
    """
    _addon_name = "whisky_helper"
    # 定义bl_classes元组，包含所有需要注册的类
    _bl_classes = (
        # 1.Properties(属性定义)
        # 2.Operator(操作器)
        # 3.Menu(菜单)
        # 4.Panel(面板)
        CameraSettingsProperties,
        CameraApplySettingsOperator,
        RenderPresetPanel,
        CameraSetPanel,
    )

    @staticmethod
    def init_addon():
        """
        初始化插件时调用此函数。
        它负责注册翻译、类和场景属性。
        """

        # 翻译
        Bridge.App.register_translations(
            AddonManager._addon_name
        )

        # Classes
        AddonManager.register_classes()
        # Scene
        AddonManager.register_scene()

    @staticmethod
    def unload_addon():
        """
        卸载插件时调用此函数。
        它负责注销场景属性、类和翻译。
        """

        # Scene
        AddonManager.unregister_scene()
        # Classes
        AddonManager.unregister_classes()
        # 翻译
        Bridge.App.unregister_translations(AddonManager._addon_name)

    @staticmethod
    def register_scene():
        """
        注册场景属性。
        这些属性包括渲染预设、摄像机设置等。
        """
        scene = Bridge.Types.get_scene()
        pp = Bridge.Props.get_pointer_property()

        # Render Preset 相关
        scene.resolution_preset = resolution_preset
        scene.aspect_ratio_preset = aspect_ratio_preset
        scene.orientation_preset = orientation_preset

        # 摄像机预设相关
        scene.camera_settings = pp(type=CameraSettingsProperties)

    @staticmethod
    def unregister_scene():
        """
        注销场景属性。
        这些属性包括渲染预设、摄像机设置等。
        """
        scene = Bridge.Types.get_scene()

        # 删除Blender Scene
        if hasattr(scene, 'resolution_preset'):
            del scene.resolution_preset
        if hasattr(scene, 'aspect_ratio_preset'):
            del scene.aspect_ratio_preset
        if hasattr(scene, 'orientation_preset'):
            del scene.orientation_preset
        if hasattr(scene, 'camera_settings'):
            del scene.camera_settings

    @staticmethod
    def register_classes():
        """
        注册所有bl_classes中的类。
        """
        for cls in AddonManager._bl_classes:
            Bridge.Utils.register_class(cls)

    @staticmethod
    def unregister_classes():
        """
        注销所有bl_classes中的类。
        逆序注销以避免潜在的依赖问题。
        """
        for cls in reversed(AddonManager._bl_classes):
            Bridge.Utils.unregister_class(cls)

    @staticmethod
    def set_addon_name(name):
        """
        ...
        """
        AddonManager._addon_name = name
