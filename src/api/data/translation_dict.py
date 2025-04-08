# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyMilkWhisky
"""
翻译相关
"""


def get_translation_zh_dict(local):
    """
    获取翻译字典

    本函数用于根据指定的本地化参数，返回一个包含翻译映射的字典

    参数:
    local (str): 本地化参数，用于指定需要的翻译语言

    返回:
    dict: 包含翻译映射的字典
    """
    translation_dict = {
        local: translation_zh_map
    }

    return translation_dict


translation_zh_map = {
    ("*", "MMD Lip Gen"): "MMD口型生成",
    ("*", "Audio Path"): "音频文件",
    ("*", "Bilibili cover image"): "必剪封面",
    ("*", "382:239 Bilibili cover image"): "382:239 B站封面",
    ("*", "Other"): "其它",
    ("*", "Old Film Standards"): "旧电影标准",
    ("*", "Film Standards"): "电影标准",
    ("*", "2.39:1 Film Standards"): "2.39:1 电影标准",
    ("*", "Standard"): "标准",
    ("*", "Film Standard"): "旧标准",
    ("*", "Landscape"): "横屏",
    ("*", "Portrait"): "竖屏",
    ("*", "Resolution"): "分辨率",
    ("*", "Aspect Ratio"): "宽高比",
    ("*", "Rotate"): "旋转",
    ("*", "ET Helper"): "亦癫助手",
    ("*", "Render Preset"): "渲染预设",
    ("*", "Set Camera"): "设置相机",
    ("*", "Focal Length"): "焦距",
    ("*", "F-Stop"): "光圈",
    ("*", "Depth of Field"): "景深",
    ("*", "Focus on Object"): "聚焦到物体",
    ("*", "Select focus object"): "选择聚焦物体",
    ("*", "Apply settings to the selected camera"): "将设置应用到选定的相机",
    ("*", "14mm ultra-wide field"): "14mm 超广角镜头",
    ("*", "Highlight background"): "突出背景",
    ("*", "24mm wide angle"): "24mm 广角镜头",
    ("*", "scenery, street snap"): "风景摄影，街头抓拍",
    ("*", "50mm human eye perspective"): "50mm 人眼视角镜头",
    ("*", "human eye perspective"): "人眼视角",
    ("*", "85mm classic portrait"): "85mm 经典肖像镜头",
    ("*", "classic portrait, background blur"): "经典肖像，背景虚化",
    ("*", "35mm long-focus"): "35mm 长焦镜头",
    ("*", "long-focus, strong background blur"): "长焦，强烈的背景虚化",
    ("*", "f/1.4 low light env"): "f/1.4 低光环境",
    ("*", "Background blur, portrait/night scene photography"): "背景虚化，适用于人像/夜景摄影",
    ("*", "f/2.8 default"): "f/2.8 默认光圈",
    ("*", "f/4 medium aperture"): "f/4 中等光圈",
    ("*", "Suitable for average lighting conditions"): "适合一般光照条件",
    ("*", "f/8 small aperture"): "f/8 小光圈",
    ("*", "Requires strong lighting"): "需要强光",
    ("*", "f/22 minimum aperture"): "f/22 最小光圈",
    ("*", "Requires a strong light environment"): "需要强光环境",
    ("*", "Slightly Blurred. Suitable for average lighting conditions"): "轻微虚化，适合一般光照条件",
    ("*", "Whisky Helper"): "Whisky助手",
    ("*", "default"): "默认",
    ("*", "Start Frame"): "起始帧",
    ("*", "Delayed Opening"): "延时张嘴",
    ("*", "Speed Up Opening"): "加速张嘴",
    ("*", "DB Threshold"): "分贝阈值",
    ("*", "RMS Threshold"): "均方根阈值",
    ("*", "Max Morph Value"): "最大阈值",
    ("*", "Threshold for the maximum value of the morphological key"): "形态键最大值的阈值",
    ("*", "Minimum threshold for audio root mean square identification"): "识别音频均方根的最小阈值",
    ("*", "Minimum threshold for audio volume detection"): "识别音频音量的最小阈值",
    ("*", "The mouth does not open immediately upon recognition;"
          " the unit is in milliseconds,"
          " and the buffer value is calculated"
          " based on the acceleration parameters for opening the mouth"): "不是识别开始就张嘴的，"
                                                                          "单位毫秒，"
                                                                          "根据加速张嘴参数计算缓冲值",
    ("*", "The larger this parameter is, "
          "the greater the value of the morph key "
          "for delayed mouth opening will be."): "这个参数越大，延时张嘴的形态键数值就会越大",
    ("*", "Timeline"): "时间线",
    ("*", "start frame"): "起始帧",
    ("*", "end frame"): "结束帧",
    ("*", "MMD Random Blink"): "MMD 随机眨眼",
    ("*", "start"): "起始",
    ("*", "end"): "结束",
    ("*", "blink interval"): "眨眼间隔",
    ("*", "The interval in seconds between blinks."): "眨眼的间隔时间，单位秒",
    ("*", "blinking wave ratio"): "波动比例",
    ("*","Blink interval = "
         "blink interval + "
         "rand(-fluctuation ratio, "
         "fluctuation ratio)"):"眨眼间隔=眨眼间隔+rand(-波动比例,波动比例)",
    ("Operator", "Gen random blink"): "生成随机眨眼",
    ("Operator", "apply camera settings"): "应用相机设置",
    ("Operator", "Gen Lips"): "口型生成",
    ("Operator", "user doc"): "用户文档",
    ("Operator", "open source"): "开源地址",
}
