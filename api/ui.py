import bpy

class RenderPresetPanel(bpy.types.Panel):
    bl_label = "Render Preset"
    bl_idname = "OBJECT_PT_RENDER_PRESET"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ET Helper'
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "resolution_preset")
        layout.prop(scene, "aspect_ratio_preset")
        layout.prop(scene, "orientation_preset")

class SetCamera(bpy.types.Panel):
    bl_label = "Set Camera"
    bl_idname = "OBJECT_PT_SET_CAMERA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ET Helper'
    bl_order = 2

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        settings = scene.camera_settings

        layout.prop(settings, "focal_length")
        layout.prop(settings, "aperture")
        layout.prop(settings, "depth_of_field")

        if settings.depth_of_field:
            layout.prop(settings, "target_object")

        row = layout.row()
        row.operator("camera.apply_settings")
        row.enabled = context.object and context.object.type == 'CAMERA'
