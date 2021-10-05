# BLUI v0.8.2

import bpy
from bpy.app.handlers import persistent

@persistent
def load_handler_for_startup(_):
    print("Changing Startup Defaults!")

    bpy.ops.wm.splash('INVOKE_DEFAULT')

def register():
    print("Registering to Change Defaults")
    bpy.app.handlers.load_factory_startup_post.append(load_handler_for_startup)


def unregister():
    print("Unregistering to Change Defaults")
    bpy.app.handlers.load_factory_startup_post.remove(load_handler_for_startup)
