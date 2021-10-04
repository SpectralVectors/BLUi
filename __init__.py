# BLUI v0.8.1

import bpy
from bpy.app.handlers import persistent

class BLUI_OT_comment_box(Operator):
    bl_idname = "blui.comment_box"
    bl_label = "Comment Box"
    bl_description = "Frames around the selected nodes, requests name and color"
    bl_options = {'REGISTER', 'UNDO'}
    bl_space_type = 'NODE_EDITOR'
    bl_context_mode = 'OBJECT'
    bl_property = 'comment_name'


    comment_name : bpy.props.StringProperty(
        name = 'Label -',
        default = 'Your Text Here'
    )

    comment_color : bpy.props.FloatVectorProperty(
        name = 'Color -',
        default = (0.8, 0.3, 0.3),
        min=0, max=1, step=1, precision=3,
        subtype='COLOR_GAMMA', size=3
    )


    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


    def execute(self, context):

        nodes = context.selected_nodes
        selected = []
        for node in nodes:
            if node.select == True:
                selected.append(node)

        bpy.ops.node.add_node(type='NodeFrame')
        frame = context.active_node
        frame.label = self.comment_name
        frame.use_custom_color = True
        frame.color = self.comment_color

        for node in selected:
            node.parent = frame

        return {'FINISHED'}

def register():
    print("Registering to Change Defaults")
    bpy.app.handlers.load_factory_startup_post.append(load_handler_for_startup)
    bpy.utils.register_class(BLUI_OT_comment_box)

def unregister():
    print("Unregistering to Change Defaults")
    bpy.app.handlers.load_factory_startup_post.remove(load_handler_for_startup)
    bpy.utils.unregister_class(BLUI_OT_comment_box)

if __name__ == "__main__":
    register()

bpy.ops.wm.splash()