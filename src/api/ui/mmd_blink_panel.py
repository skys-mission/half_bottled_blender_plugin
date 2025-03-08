# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyWhisky
# pylint: disable=R0801
"""
...
"""

import random
import bpy  # pylint: disable=import-error
from ...util.logger import Log


class RandomBlinkPanel(bpy.types.Panel):  # pylint: disable=too-few-public-methods
    """
        ...根据まばたき眨眼
    """
    bl_label = "MMD Random Blink"
    bl_idname = "VIEW3D_PT_Random_blink"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Whisky Helper'
    bl_order = 4

    def draw(self, context):
        """
        ...
        """
        layout = self.layout

        # 第一行：标签
        row = layout.row()
        row.label(text="Timeline")

        # 第二行：起始和结束参数
        row = layout.row()
        row.prop(context.scene, "blink_start_frame")
        row.prop(context.scene, "blink_end_frame")
        row = layout.row()
        # row = layout.row()
        row.prop(context.scene, "blinking_frequency")
        row = layout.row()
        row.prop(context.scene, "blinking_wave_ratio")
        # 第三行：随机眨眼按钮
        row = layout.row()
        row.operator("scene.gen_random_blink")


class RandomBlinkOperator(bpy.types.Operator):
    """
    ...
    """
    bl_idname = "scene.gen_random_blink"
    bl_label = "Gen random blink"

    def generate_blink_frames(self,  # pylint: disable=too-many-arguments,too-many-positional-arguments
                              start_frame,
                              end_frame,
                              fps,
                              interval_seconds,
                              wave_ratio):  # pylint: disable=too-many-arguments,too-many-positional-arguments
        """
        生成眨眼形态键动画帧序列
        
        :param start_frame: 起始帧
        :param end_frame: 结束帧
        :param fps: 帧率
        :param interval_seconds: 眨眼间隔（秒）
        :param wave_ratio: 间隔波动比例（0.1-1）
        :return: 包含帧数据的字典 {形态键名: [{frame: 帧数, value: 值}]}
        """
        frames = {}
        current_time = start_frame / fps
        end_time = end_frame / fps

        while current_time < end_time:
            # 计算实际间隔（加入随机波动）
            actual_interval = interval_seconds * random.uniform(1 - wave_ratio, 1 + wave_ratio)
            blink_time = current_time + actual_interval

            # 转换为帧数
            blink_frame = int(blink_time * fps)

            # 确保在有效范围内
            if blink_frame > end_frame:
                break

            # 强制设置起始帧和结束帧为0
            # 生成眨眼动画（从0到1再回到0）
            frames.setdefault('まばたき', []).extend([
                {'frame': blink_frame - 2, 'value': 0.0},
                {'frame': blink_frame, 'value': 1.0},
                {'frame': blink_frame + 2, 'value': 0.0}
            ])

            current_time = blink_time

        # 强制设置起始帧和结束帧为0
        frames['まばたき'].insert(0, {'frame': start_frame, 'value': 0.0})
        frames['まばたき'].append({'frame': end_frame, 'value': 0.0})

        return frames

    @staticmethod
    def find_shape_keys_recursive(obj, shape_key_name):
        """
        ...
        """
        found = []
        if obj.type == 'MESH' and obj.data.shape_keys:
            for key in obj.data.shape_keys.key_blocks:
                if key.name == shape_key_name:
                    found.append(obj)
                    break

        for child in obj.children:
            found.extend(RandomBlinkOperator.find_shape_keys_recursive(child, shape_key_name))
        return found

    def apply_blink_animation(self, mesh, blink_data, start_frame):
        """
        ...
        """
        morph_key = 'まばたき'
        # 强制设置起始帧为0
        blink_data[morph_key].insert(0, {
            'frame': start_frame,
            'value': 0.0,
            'frame_type': 'KEYFRAME'})
        # 获取最大帧并清除旧关键帧
        max_frame = max(f['frame'] for f in blink_data[morph_key])
        for i in range(start_frame, max_frame + 1):
            self.clear_shape_key_keyframe(mesh, morph_key, i)

        # 查找有效形态键
        found_key = next((k for k in mesh.data.shape_keys.key_blocks if k.name == morph_key), None)
        morph_key = found_key.name if found_key else 'まばたき'

        # 应用关键帧并记录日志
        for frame_data in blink_data[morph_key]:
            try:
                self.set_shape_key_value(  # pylint: disable=too-many-function-args
                    mesh,
                    morph_key,
                    frame_data['value'],
                    frame_data['frame'],
                )  # pylint: disable=too-many-function-args
                Log.info(
                    f"Successfully set shape key '{morph_key}':"
                    f" frame {frame_data['frame']}, value {frame_data['value']}")
            except Exception as e:
                Log.warning(f"Keyframe setting failed.：{str(e)}")
                raise

    @staticmethod
    def set_shape_key_value(obj, shape_key_name, value, frame):
        """
        ...
        """
        if obj and obj.type == 'MESH':
            shape_keys = obj.data.shape_keys
            if shape_keys and shape_key_name in shape_keys.key_blocks:
                shape_key = shape_keys.key_blocks[shape_key_name]
                # 设置关键帧插值类型
                shape_key.value = value
                shape_key.keyframe_insert(
                    data_path="value",
                    frame=frame
                )

    @staticmethod
    def clear_shape_key_keyframe(obj, shape_key_name, frame):
        """
        ...
        """
        if obj and obj.type == 'MESH':
            shape_keys = obj.data.shape_keys
            if shape_keys and shape_key_name in shape_keys.key_blocks:
                try:
                    shape_keys.key_blocks[shape_key_name].keyframe_delete(
                        data_path="value",
                        frame=frame
                    )
                except RuntimeError:
                    pass

    def execute(self, context):
        """
        ...
        """
        scene = context.scene
        fps = scene.render.fps

        context.window_manager.progress_begin(0, 100)
        context.window.cursor_modal_set('WAIT')

        try:
            # 生成眨眼动画数据
            blink_data = self.generate_blink_frames(
                start_frame=scene.blink_start_frame,
                end_frame=scene.blink_end_frame,
                fps=fps,
                interval_seconds=scene.blinking_frequency,
                wave_ratio=scene.blinking_wave_ratio
            )

            # 应用动画到选中的网格对象
            meshes = find_mmd_meshes()
            for mesh in meshes:
                self.apply_blink_animation(mesh, blink_data, scene.blink_start_frame)

            context.window_manager.progress_update(100)
            self.report({'INFO'},
                        f"Successfully generated {len(blink_data['まばたき'])} blink animations")
        except Exception as e:  # pylint: disable=broad-exception-caught
            # 结束进度条
            context.window_manager.progress_end()
            # 恢复鼠标指针
            context.window.cursor_modal_restore()
            Log.raise_error(str(e), e.__class__)

        # 结束进度条
        context.window_manager.progress_end()

        # 恢复鼠标指针
        context.window.cursor_modal_restore()
        return {'FINISHED'}


def find_shape_keys_with_name(obj, shape_key_name):
    """
    递归查询对象及其子对象中的所有网格体，并查找是否包含指定名称的形态键。

    参数:
        obj (bpy.types.Object): 要查询的对象。
        shape_key_name (str): 要查找的形态键名称。

    返回:
        list: 包含指定名称形态键的对象列表。
    """
    found_objects = []

    # 检查当前对象是否为网格体，并且是否有形态键
    if obj.type == 'MESH' and obj.data.shape_keys:
        for shape_key in obj.data.shape_keys.key_blocks:
            if shape_key.name == shape_key_name:
                found_objects.append(obj)
                break

    # 递归查询子对象
    for child in obj.children:
        found_objects.extend(find_shape_keys_with_name(child, shape_key_name))

    return found_objects


def find_mmd_meshes():
    """
    ...
    """
    # 记录包含指定形态键的对象
    found_objects = []

    selected_objects = bpy.context.selected_objects

    if not selected_objects:
        Log.raise_error("Please select an object first.", Exception)
        return found_objects

    # 要查找的形态键名称
    shape_key_name = 'まばたき'

    for obj in selected_objects:
        found_objects.extend(find_shape_keys_with_name(obj, shape_key_name))

    # 打印结果
    if found_objects:
        Log.info(f"Found  {len(found_objects)} "
                 f"objects containing the shape key '{shape_key_name}'.")
        for obj in found_objects:
            Log.info(f"Object containing the shape key '{shape_key_name}', {obj.name} found.")
    else:
        Log.raise_error(f"No object containing the shape key "
                        f"'{shape_key_name}' was found.", Exception)
    return found_objects
