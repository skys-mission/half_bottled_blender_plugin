# -*- coding: utf-8 -*-
# Copyright (c) 2025, https://github.com/skys-mission and SoyWhisky
"""
Blender Addon 入口
"""
from .src.core.addon import AddonManager

# 注册插件信息
bl_info = {
    "name": "Whisky Helper",
    "author": "SoyWhisky, github.com/skys-mission",
    "version": (0, 3, 2),
    "blender": (3, 6, 0),
    "location": "View3D > N-Panel  > Whisky Helper",
    "description": "Whisky Helper.",
    "category": "3D View",
    "doc_url": "https://soywhisky.com/doc/blender/addon/whisky_helper_for_blender",
    "tracker_url": "https://github.com/skys-mission/whisky_helper_for_blender/issues"
}


def register():
    """
    注册插件。

    本函数在插件加载时被调用，用于设置插件名称并初始化插件。
    """
    AddonManager.set_addon_name(__name__)
    AddonManager.init_addon()


def unregister():
    """
    注销插件。

    本函数在插件卸载时被调用，用于卸载插件。
    """
    try:
        AddonManager.unload_addon()
    except Exception as e:  # pylint: disable=broad-exception-caught
        from .src.audio.pkg import unload_pkg  # pylint: disable=import-outside-toplevel
        unload_pkg()
        raise e


if __name__ == "__main__":
    pass
