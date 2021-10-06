# BLUI v0.8.4

import bpy, os, urllib.request, addon_utils
from bpy.app.handlers import persistent

@persistent
def load_handler_for_preferences(_):
    print("Changing Preference Defaults!")

    string = bpy.app.version_string
    blenderversion = string.rstrip(string[-2:])
    keymap_filepath = str(os.path.expanduser('~/AppData/Roaming/Blender Foundation/Blender/')) + blenderversion + str('/scripts/startup/bl_app_templates_user/BLUI/BLUI_Keymap.py')

    bpy.ops.preferences.keyconfig_import(filepath=keymap_filepath)
    #bpy.ops.preferences.keyconfig_activate(filepath=keymap_filepath)

@persistent
def load_handler_for_startup(_):
    print("Changing Startup Defaults!")

    prefs = bpy.context.preferences
    active_addons = prefs.addons

    addons = []
    addon = {
        'addon_name':'',
        'url':'',
        }
        
    addon1 = addon.copy()
    addon1['addon_name'] = 'MrMannequinsTools'
    addon1['url'] = 'https://github.com/Jim-Kroovy/Mr-Mannequins-Tools/releases/download/v1.4/MrMannequinsTools-1.4.zip'

    addon2 = addon.copy()
    addon2['addon_name'] = 'blender-for-unrealengine'
    addon2['url'] = 'https://github.com/xavier150/Blender-For-UnrealEngine-Addons/releases/download/v0.2.8/blender-for-unrealengine.zip'

    addon3 = addon.copy()
    addon3['addon_name'] = 'TexTools_1_4_4'
    addon3['url'] = 'https://github.com/SavMartin/TexTools-Blender/releases/download/v1.4.4/TexTools_1_4_4.zip'

    addon4 = addon.copy()
    addon4['addon_name'] = 'modifier_stack_manager'
    addon4['url'] = 'https://github.com/salaivv/modifier-stack-manager/releases/download/0.2/modifier_stack_manager.zip'

    addon5 = addon.copy()
    addon5['addon_name'] = 'RightMouseNavigation'
    addon5['url'] = 'https://github.com/SpectralVectors/RightMouseNavigation/releases/download/1.8/RightMouseNavigation.zip'

    addon6 = addon.copy()
    addon6['addon_name'] = 'CommentBox-main'
    addon6['url'] = 'https://github.com/SpectralVectors/CommentBox/archive/refs/heads/main.zip'

    for addon in active_addons:

        if addon_utils.check('MrMannequinsTools') == (True, False):
            addons.append(addon1)
            
        if addon_utils.check('blender-for-unrealengine') == (True, False):
            addons.append(addon2)        
            
        if addon_utils.check('TexTools_1_4_4') == (True, False):
            addons.append(addon3)      
            
        if addon_utils.check('modifier_stack_manager') == (True, False):
            addons.append(addon4)       
            
        if addon_utils.check('RightMouseNavigation') == (True, False):
            addons.append(addon5)        
            
        if addon_utils.check('CommentBox-main') == (True, False):
            addons.append(addon6)

    for addon in addons:
        url_file = bpy.path.basename(addon['url'])
        module_name = bpy.path.display_name_from_filepath(addon['url'])
        filepath = str(os.path.expanduser('~/Downloads/') + url_file)
        file = urllib.request.urlretrieve(addon['url'], filepath)
        overwrite_setting = False
        bpy.ops.preferences.addon_install(overwrite=overwrite_setting, filepath=filepath)
        try:
            bpy.ops.preferences.addon_enable(module=module_name)
        except: # ModuleNotFoundError
            bpy.ops.preferences.addon_enable(module=addon['addon_name'])        

    bpy.ops.wm.splash('INVOKE_DEFAULT')

def register():
    print("Registering to Change Defaults")
    bpy.app.handlers.load_factory_preferences_post.append(load_handler_for_preferences)
    bpy.app.handlers.load_factory_startup_post.append(load_handler_for_startup)


def unregister():
    print("Unregistering to Change Defaults")
    bpy.app.handlers.load_factory_preferences_post.remove(load_handler_for_preferences)
    bpy.app.handlers.load_factory_startup_post.remove(load_handler_for_startup)
