# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and EcceTal
# This file is part of ET Helper for Blender.
from bpy.types import Operator


class CAMERA_OT_apply_settings(Operator):
    bl_idname = "camera.apply_settings"
    bl_label = "apply settings"
    bl_description = "Apply settings to the selected camera"

    @classmethod
    def poll(cls, context):
        return context.object and context.object.type == 'CAMERA'

    def execute(self, context):
        settings = context.scene.camera_settings
        camera = context.object.data

        camera.lens = float(settings.focal_length)
        camera.dof.use_dof = settings.depth_of_field
        camera.dof.aperture_fstop = float(settings.aperture)

        if settings.depth_of_field and settings.target_object:
            camera.dof.focus_object = settings.target_object

        self.report({'INFO'}, "Camera settings have been applied.")
        return {'FINISHED'}
