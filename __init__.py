# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyMilkWhisky
"""
Blender Addon 入口
"""
from .src.core.addon import AddonManager
from .src.common.addon_info import ADDON_INFO

# 注册插件信息
bl_info = ADDON_INFO


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
    AddonManager.unload_addon()


if __name__ == "__main__":
    pass
