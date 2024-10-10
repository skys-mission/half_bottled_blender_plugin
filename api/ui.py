import bpy

class ETHelperPanel(bpy.types.Panel):
    bl_label = "ET Helper"
    bl_idname = "OBJECT_PT_resolution_preset"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ET Helper'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "resolution_preset")
        layout.prop(scene, "aspect_ratio_preset")
        layout.prop(scene, "orientation_preset")