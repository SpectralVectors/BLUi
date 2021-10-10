###########################
#### BLUi 0.8.6 Keymap ####
###########################

###########################
#### TABLE OF CONTENTS ####
###########################
#
# - 3D VIEW - 117
#
# - 3D VIEW TOOLS - 216
#
# - ANIMATION - 827
#
# - ARMATURE - 871
#
# - BEVEL - 912
#
# - CLIP EDITOR - 941
#
# - CONSOLE - 1072
#
# - CURVE - 1112
#
# - CUSTOM NORMALS - 1150
#
# - DOPESHEET - 1171
#
# - EYEDROPPER - 1243
#
# - FILE BROWSER - 1268
#
# - FONT - 1341
#
# - FRAMES - 1389
#
# - GENERIC GIZMO - 1402
#
# - GENERIC TOOL - 1447
#
# - GESTURE - 1482
#
# - GRAPH EDITOR - 1521
#
# - GREASE PENCIL - 1589
#
# - IMAGE EDITOR - 1864
#
# - INFO - 2031
#
# - KNIFE MODAL - 2053
#
# - LATTICE - 2080
#
# - MARKERS - 2102
#
# - MASK EDITING - 2125
#
# - MESH - 2170
#
# - METABALL - 2226
#
# - NLA EDITOR - 2254
#
# - NODE EDITOR - 2321
#
# - OBJECT MODE - 2436
#
# - OUTLINER - 2509
#
# - PAINT - 2568
#
# - PARTICLE - 2613
#
# - POSE - 2640
#
# - PROPERTY EDITOR - 2686
#
# - REGION CONTEXT MENU - 2711
#
# - SCREEN - 2719
#
# - SCULPT - 2763
#
# - SEQUENCER - 2848
#
# - STANDARD MODAL MAP - 2977
#
# - TEXT - 2990
#
# - TIMESCRUB - 3085
#
# - TOOLBAR POPUP - 3093
#
# - TRANSFORM MODAL MAP - 3105
#
# - UV EDITOR - 3160
#
# - USER INTERFACE - 3211
#
# - VERTEX PAINT - 3232
#
# - VIEW 2D - 3261
#
# - VIEW 3D MODAL - 3307
#
# - WEIGHT PAINT - 3469
#
# - WINDOW - 3486
#
###########################

keyconfig_version = (2, 93, 21)
keyconfig_data = \
[
###########
# 3D VIEW #
###########
("3D View",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties":[("name", 'TOPBAR_PT_name'),("keep_open", False),],},),
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("view3d.localview", {"type": 'I', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("view3d.localview", {"type": 'MOUSESMARTZOOM', "value": 'ANY'}, None),
            ("wm.call_menu_pie",{"type": 'V', "value": 'PRESS', "repeat": True},{"properties":[("name", 'VIEW3D_MT_view_pie'),]},),
            ("view3d.rotate", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("view3d.move", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None),
            ("view3d.zoom", {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("view3d.view_selected",{"type": 'F', "value": 'PRESS', "shift": True, "repeat": True},{"properties":[("use_all_regions", True),],},),
            ("view3d.view_selected",{"type": 'F', "value": 'PRESS', "repeat": True},{"properties":[("use_all_regions", False),],},),
            ("view3d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
            ("view3d.rotate", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
            ("view3d.rotate", {"type": 'MOUSEROTATE', "value": 'ANY'}, None),
            ("view3d.move", {"type": 'TRACKPADPAN', "value": 'ANY', "shift": True}, None),
            ("view3d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
            ("view3d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
            ("view3d.zoom",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True},{"properties":[("delta", 1),],},),
            ("view3d.zoom",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True},{"properties":[("delta", -1),],},),
            ("view3d.zoom",{"type": 'WHEELINMOUSE', "value": 'PRESS'},{"properties":[("delta", 1),],},),
            ("view3d.zoom",{"type": 'WHEELOUTMOUSE', "value": 'PRESS'},{"properties":[("delta", -1),],},),
            ("view3d.zoom",{"type": 'WHEELINMOUSE', "value": 'PRESS', "alt": True},{"properties":[("delta", 1),],},),
            ("view3d.zoom",{"type": 'WHEELOUTMOUSE', "value": 'PRESS', "alt": True},{"properties":[("delta", -1),],},),
            ("view3d.dolly",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "repeat": True},{"properties":[("delta", 1),],},),
            ("view3d.dolly",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "repeat": True},{"properties":[("delta", -1),],},),
            ("view3d.view_all",{"type": 'A', "value": 'PRESS', "repeat": True},{"properties":[("center", False),],},),
            ("view3d.view_all",{"type": 'A', "value": 'PRESS', "shift": True, "repeat": True},{"properties":[("use_all_regions", True),("center", False),],},),
            ("view3d.view_camera", {"type": 'F4', "value": 'PRESS', "repeat": True}, None),
            ("view3d.view_axis",{"type": 'F1', "value": 'PRESS', "repeat": True},{"properties":[("type", 'FRONT'),],},),
            ("view3d.view_axis",{"type": 'F2', "value": 'PRESS', "repeat": True},    {"properties":[("type", 'RIGHT'),],},),
            ("view3d.view_axis",{"type": 'F3', "value": 'PRESS', "repeat": True},{"properties":[("type", 'TOP'),],},),
            ("view3d.view_axis",{"type": 'F1', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties":[("type", 'BACK'),],},),
            ("view3d.view_axis",{"type": 'F2', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties":[("type", 'LEFT'),],},),
            ("view3d.view_axis",{"type": 'F3', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties":[("type", 'BOTTOM'),],},),
            ("view3d.view_orbit",{"type": 'F5', "value": 'PRESS', "repeat": True},{"properties":[("angle", 3.1415927),("type", 'ORBITRIGHT'),],},),
            ("view3d.ndof_orbit_zoom", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
            ("view3d.ndof_orbit", {"type": 'NDOF_MOTION', "value": 'ANY', "ctrl": True}, None),
            ("view3d.ndof_pan", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True}, None),
            ("view3d.ndof_all", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True, "ctrl": True}, None),
            ("view3d.view_selected",{"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'},{"properties": [("use_all_regions", False),], },),
            ("view3d.view_roll",{"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},{"properties": [("type", 'LEFT'),], },),
            ("view3d.view_roll",{"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},{"properties": [("type", 'RIGHT'),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS'},{"properties": [("type", 'FRONT'),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_BACK', "value": 'PRESS'},{"properties": [("type", 'BACK'),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_LEFT', "value": 'PRESS'},{"properties": [("type", 'LEFT'),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS'},{"properties": [("type", 'RIGHT'),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_TOP', "value": 'PRESS'},{"properties": [("type", 'TOP'),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_BOTTOM', "value": 'PRESS'},{"properties": [("type", 'BOTTOM'),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS', "shift": True},{"properties": [("type", 'FRONT'),("align_active", True),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS', "shift": True},{"properties": [("type", 'RIGHT'),("align_active", True),], },),
            ("view3d.view_axis",{"type": 'NDOF_BUTTON_TOP', "value": 'PRESS', "shift": True},{"properties": [("type", 'TOP'),("align_active", True),], },),
            ("view3d.select",{"type": 'LEFTMOUSE', "value": 'CLICK'},{"properties": [("deselect_all", True),], },),
            ("view3d.select",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},{"properties": [("extend", True),], },),
            ("view3d.select",{"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},{"properties": [("deselect", True),], },),
            ("view3d.select",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},{"properties": [("extend", True),("toggle", True),("center", True),], },),
            ("view3d.select",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "alt": True},{"properties": [("toggle", True),("enumerate", True),], },),
            ("view3d.select",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True, "alt": True},{"properties": [("toggle", True),("center", True),("enumerate", True),], },),
            ("view3d.zoom_border", {"type": 'Z', "value": 'PRESS', "repeat": True}, None),
            ("view3d.copybuffer", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("view3d.pastebuffer", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.call_menu_pie",{"type": 'X', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("name", 'VIEW3D_MT_snap_pie'),], },),
            ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("wm.call_menu_pie",{"type": 'PERIOD', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_MT_pivot_pie'),], },),
            ("wm.call_menu_pie",{"type": 'COMMA', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_MT_orientations_pie'),], },),
            ("view3d.toggle_xray", {"type": 'X', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("wm.context_toggle",{"type": 'X', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_snap'),], },),
            ("view3d.view_axis",{"type": 'NUMPAD_1', "value": 'PRESS', "repeat": True},{"properties": [("type", 'FRONT'),], },),
            ("view3d.view_axis",{"type": 'NUMPAD_1', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'BACK'),], },),
            ("view3d.view_axis",{"type": 'NUMPAD_3', "value": 'PRESS', "repeat": True},{"properties": [("type", 'RIGHT'),], },),
            ("view3d.view_axis",{"type": 'NUMPAD_3', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'LEFT'),], },),
            ("view3d.view_axis",{"type": 'NUMPAD_7', "value": 'PRESS', "repeat": True},{"properties": [("type", 'TOP'),], },),
            ("view3d.view_axis",{"type": 'NUMPAD_7', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'BOTTOM'),], },),
            ("view3d.view_persportho", {"type": 'NUMPAD_5', "value": 'PRESS', "repeat": True}, None),
            ("view3d.view_camera", {"type": 'NUMPAD_0', "value": 'PRESS', "repeat": True}, None),
            ("view3d.view_orbit",{"type": 'NUMPAD_4', "value": 'PRESS', "repeat": True},{"properties": [("type", 'ORBITLEFT'),], },),
            ("view3d.view_orbit",{"type": 'NUMPAD_6', "value": 'PRESS', "repeat": True},{"properties": [("type", 'ORBITRIGHT'),], },),
            ("view3d.view_orbit",{"type": 'NUMPAD_8', "value": 'PRESS', "repeat": True},{"properties": [("type", 'ORBITUP'),], },),
            ("view3d.view_orbit",{"type": 'NUMPAD_2', "value": 'PRESS', "repeat": True},{"properties": [("type", 'ORBITDOWN'),], },),
            ("view3d.view_persportho", {"type": 'G', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("view3d.view_axis",{"type": 'H', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("type", 'FRONT'),], },),
            ("view3d.view_axis",{"type": 'K', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("type", 'LEFT'),], },),
            ("view3d.view_axis",{"type": 'J', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("type", 'TOP'),], },),
            ("view3d.toggle_shading",{"type": 'TWO', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("type", 'WIREFRAME'),], },),
            ("view3d.toggle_shading",{"type": 'THREE', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("type", 'SOLID'),], },),
            ("view3d.toggle_shading",{"type": 'FOUR', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("type", 'RENDERED'),], },),
            ("blui.right_mouse_navigation", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),],},),

("3D View Generic",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("wm.context_toggle",{"type": 'LEFT_BRACKET', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.show_region_toolbar'),], },), 
            ("wm.context_toggle",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.show_region_ui'),], },), 
            ("wm.context_toggle",{"type": 'N', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'space_data.show_region_ui'),], },), ],},),

#################
# 3D VIEW TOOLS #
#################
("3D View Tool: Cursor",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.cursor3d", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("transform.translate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("cursor_transform", True),("release_confirm", True),], },), 
            ("view3d.cursor3d", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("transform.translate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("cursor_transform", True),("release_confirm", True),], },), ],},),

("3D View Tool: Edit Armature, Bone Envelope",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.bbone_resize",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.bbone_resize",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Armature, Bone Size",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.transform",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'BONE_ENVELOPE'),("release_confirm", True),], },), 
            ("transform.transform",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'BONE_ENVELOPE'),("release_confirm", True),], },), ],},),

("3D View Tool: Edit Armature, Extrude",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("armature.extrude_move",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("armature.extrude_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), ],},),

("3D View Tool: Edit Armature, Extrude to Cursor",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("armature.click_extrude", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), ("armature.click_extrude", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Edit Armature, Roll",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.transform",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'BONE_ROLL'),("release_confirm", True),], },), 
            ("transform.transform",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'BONE_ROLL'),("release_confirm", True),], },), ],},),

("3D View Tool: Edit Curve, Draw",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("curve.draw",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), 
            ("curve.draw",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), ],},),

("3D View Tool: Edit Curve, Extrude",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("curve.extrude_move",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("curve.extrude_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), ],},),

("3D View Tool: Edit Curve, Extrude to Cursor",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("curve.vertex_add", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("curve.vertex_add", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Edit Curve, Radius",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.transform",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'CURVE_SHRINKFATTEN'),("release_confirm", True),], },), 
            ("transform.transform",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'CURVE_SHRINKFATTEN'),("release_confirm", True),], },), ],},),

("3D View Tool: Edit Curve, Randomize",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.vertex_random",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("wait_for_input", False),], },), 
            ("transform.vertex_random",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), ],},),

("3D View Tool: Edit Curve, Tilt",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.tilt",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.tilt",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Gpencil, Bend",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.bend",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.bend",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Gpencil, Extrude",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.extrude_move", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.extrude_move", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Edit Gpencil, Interpolate",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.interpolate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Gpencil, Radius",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.transform",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'GPENCIL_SHRINKFATTEN'),("release_confirm", True),], },), 
            ("transform.transform",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'GPENCIL_SHRINKFATTEN'),("release_confirm", True),], },), ],},),

("3D View Tool: Edit Gpencil, Select Box",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select_box", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),], },), 
            ("gpencil.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },), 
            ("gpencil.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True, "ctrl": True},{"properties": [("mode", 'AND'),], },), ],},),

("3D View Tool: Edit Gpencil, Select Circle",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), 
            ("gpencil.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),("mode", 'ADD'),], },), 
            ("gpencil.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),("mode", 'SUB'),], },), ],},),

("3D View Tool: Edit Gpencil, Select Lasso",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),], },), 
            ("gpencil.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },), 
            ("gpencil.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True, "ctrl": True},{"properties": [("mode", 'AND'),], },), ],}),

("3D View Tool: Edit Gpencil, Shear",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.shear",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.shear",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Gpencil, To Sphere",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.tosphere",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.tosphere",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Gpencil, Transform Fill",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.transform_fill",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("gpencil.transform_fill",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Gpencil, Tweak",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("deselect_all", True),], },), 
            ("gpencil.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },), ],},),

("3D View Tool: Edit Mesh, Bevel",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.bevel",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("mesh.bevel",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Mesh, Bisect",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.bisect", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), ("mesh.bisect", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Edit Mesh, Edge Slide",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.edge_slide",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.edge_slide",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Mesh, Extrude Along Normals",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.extrude_region_shrink_fatten",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("TRANSFORM_OT_shrink_fatten", [("release_confirm", True),  ], ),], },), 
            ("mesh.extrude_region_shrink_fatten",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_shrink_fatten", [("release_confirm", True),  ], ),], },), ],},),

("3D View Tool: Edit Mesh, Extrude Individual",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.extrude_faces_move",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("TRANSFORM_OT_shrink_fatten", [("release_confirm", True),  ], ),], },), 
            ("mesh.extrude_faces_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_shrink_fatten", [("release_confirm", True),  ], ),], },), ],},),

("3D View Tool: Edit Mesh, Extrude Manifold",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.extrude_manifold",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("MESH_OT_extrude_region", [("use_dissolve_ortho_edges", True),  ], ),("TRANSFORM_OT_translate", [("orient_type", 'NORMAL'),  ("constraint_axis", (False, False, True)),  ("release_confirm", True),  ("use_automerge_and_split", True),  ], ),], },), 
            ("mesh.extrude_manifold",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("MESH_OT_extrude_region", [("use_dissolve_ortho_edges", True),  ], ),("TRANSFORM_OT_translate", [("orient_type", 'NORMAL'),  ("constraint_axis", (False, False, True)),  ("release_confirm", True),  ("use_automerge_and_split", True),  ], ),], },), ],},),

("3D View Tool: Edit Mesh, Extrude Region",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.extrude_context_move",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("mesh.extrude_context_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), ],}),

("3D View Tool: Edit Mesh, Extrude to Cursor",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.dupli_extrude_cursor", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("mesh.dupli_extrude_cursor", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Edit Mesh, Inset Faces",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.inset",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("mesh.inset",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Mesh, Knife",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.knife_tool",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), 
            ("mesh.knife_tool",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), ],},),

("3D View Tool: Edit Mesh, Loop Cut",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.loopcut_slide",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_edge_slide", [("release_confirm", True),  ], ),], },), 
            ("mesh.loopcut_slide",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_edge_slide", [("release_confirm", True),  ], ),], },), ],},),

("3D View Tool: Edit Mesh, Offset Edge Loop Cut",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.offset_edge_loops_slide", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("mesh.offset_edge_loops_slide", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Edit Mesh, Poly Build",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.polybuild_extrude_at_cursor_move",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("mesh.polybuild_face_at_cursor_move",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("mesh.polybuild_delete_at_cursor", {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True}, None), ("mesh.polybuild_extrude_at_cursor_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("mesh.polybuild_face_at_cursor_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("mesh.polybuild_delete_at_cursor", {"type": 'MIDDLEMOUSE', "value": 'CLICK', "shift": True}, None), ],},),

("3D View Tool: Edit Mesh, Push/Pull",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.push_pull",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.push_pull",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Mesh, Randomize",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.vertex_random",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("wait_for_input", False),], },), 
            ("transform.vertex_random",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), ],},),

("3D View Tool: Edit Mesh, Rip Edge",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.rip_edge_move",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("mesh.rip_edge_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), ],},),

("3D View Tool: Edit Mesh, Rip Region",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.rip_move",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), 
            ("mesh.rip_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },), ],},),

("3D View Tool: Edit Mesh, Shrink/Fatten",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.shrink_fatten",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.shrink_fatten",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Mesh, Smooth",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.vertices_smooth",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("wait_for_input", False),], },), 
            ("mesh.vertices_smooth",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), ],},),

("3D View Tool: Edit Mesh, Spin",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.spin", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("mesh.spin", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Edit Mesh, Spin Duplicates",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("mesh.spin",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("dupli", True),], },), 
            ("mesh.spin",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("dupli", True),], },), ],},),

("3D View Tool: Edit Mesh, To Sphere",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.tosphere",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.tosphere",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Edit Mesh, Vertex Slide",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.vert_slide",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.vert_slide",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Measure",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.ruler_add", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("view3d.ruler_remove", {"type": 'X', "value": 'PRESS', "repeat": True}, None), 
            ("view3d.ruler_remove", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None), 
            ("view3d.ruler_add", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Move",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.translate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.translate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Object, Add Primitive",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.interactive_add",{"type": 'EVT_TWEAK_L', "value": 'ANY', "any": True},{"properties": [("wait_for_input", False),], },), 
            ("view3d.interactive_add",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "any": True},{"properties": [("wait_for_input", False),], },), ],},),

("3D View Tool: Paint Gpencil, Arc",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.primitive", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None), 
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True, "alt": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None), 
            ("gpencil.select_lasso", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None), ],},),

("3D View Tool: Paint Gpencil, Box",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.primitive", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None), 
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True, "alt": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None), 
            ("gpencil.select_lasso", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None), ],},),

("3D View Tool: Paint Gpencil, Circle",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.primitive", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None), 
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True, "alt": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None), 
            ("gpencil.select_lasso", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None), ],},),

("3D View Tool: Paint Gpencil, Curve",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.primitive", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True, "alt": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("gpencil.select_lasso", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None), ],},),

("3D View Tool: Paint Gpencil, Cutter",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.stroke_cutter", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True, "alt": True}, None), 
            ("gpencil.stroke_cutter", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("gpencil.select_lasso", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None), ],},),

("3D View Tool: Paint Gpencil, Eyedropper",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("ui.eyedropper_gpencil_color", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("ui.eyedropper_gpencil_color", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("ui.eyedropper_gpencil_color", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None), 
            ("ui.eyedropper_gpencil_color", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("ui.eyedropper_gpencil_color", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("ui.eyedropper_gpencil_color", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None), ],},),

("3D View Tool: Paint Gpencil, Interpolate",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.interpolate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Paint Gpencil, Line",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.primitive", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None), 
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True, "alt": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None), 
            ("gpencil.select_lasso", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None), ],},),

("3D View Tool: Paint Gpencil, Polyline",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.primitive", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.primitive", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True, "alt": True}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), 
            ("gpencil.primitive", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None), 
            ("gpencil.select_lasso", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None), ],},),

("3D View Tool: Paint Weight, Gradient",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("paint.weight_gradient", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("paint.weight_gradient", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Paint Weight, Sample Vertex Group",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("paint.weight_sample_group", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("paint.weight_sample_group", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Paint Weight, Sample Weight",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("paint.weight_sample", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("paint.weight_sample", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Pose, Breakdowner",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("pose.breakdown", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("pose.breakdown", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Pose, Push",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("pose.push", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("pose.push", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Pose, Relax",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("pose.relax", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("pose.relax", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Rotate",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.rotate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.rotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Scale",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.resize",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },), 
            ("transform.resize",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },), ],},),

("3D View Tool: Sculpt Gpencil, Select Box",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select_box", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),], },), 
            ("gpencil.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },), 
            ("gpencil.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True, "ctrl": True},{"properties": [("mode", 'AND'),], },), ],},),

("3D View Tool: Sculpt Gpencil, Select Circle",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), 
            ("gpencil.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),("mode", 'ADD'),], },), 
            ("gpencil.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),("mode", 'SUB'),], },), ],},),

("3D View Tool: Sculpt Gpencil, Select Lasso",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("gpencil.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),], },), 
            ("gpencil.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },), 
            ("gpencil.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True, "ctrl": True},{"properties": [("mode", 'AND'),], },), ],},),

("3D View Tool: Sculpt Gpencil, Tweak",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.cursor3d", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("transform.translate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("cursor_transform", True),("release_confirm", True),], },), ],},),

("3D View Tool: Sculpt, Box Face Set",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.face_set_box_gesture", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), ],},),

("3D View Tool: Sculpt, Box Hide",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("paint.hide_show",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("action", 'HIDE'),], },), 
            ("paint.hide_show",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("action", 'SHOW'),], },), 
            ("paint.hide_show",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("action", 'SHOW'),("area", 'ALL'),], },), 
            ("paint.hide_show",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("action", 'HIDE'),], },), 
            ("paint.hide_show",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("action", 'SHOW'),], },), ],},),

("3D View Tool: Sculpt, Box Mask",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'ADD'),], },), 
            ("view3d.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },), 
            ("view3d.select_box",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'ADD'),], },), 
            ("view3d.select_box",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'SUB'),], },), ],},),

("3D View Tool: Sculpt, Box Trim",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.trim_box_gesture", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), ],},),

("3D View Tool: Sculpt, Cloth Filter",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.cloth_filter", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("sculpt.cloth_filter", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Sculpt, Color Filter",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.color_filter", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("sculpt.color_filter", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Sculpt, Face Set Edit",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.face_set_edit", {"type": 'LEFTMOUSE', "value": 'ANY'}, None), 
            ("sculpt.face_set_edit", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), ],},),

("3D View Tool: Sculpt, Lasso Face Set",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.face_set_lasso_gesture", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), ],},),

("3D View Tool: Sculpt, Lasso Mask",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("paint.mask_lasso_gesture",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("value", 1.0),], },), 
            ("paint.mask_lasso_gesture",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("value", 0.0),], },), 
            ("paint.mask_lasso_gesture",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("value", 1.0),], },), 
            ("paint.mask_lasso_gesture",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("value", 0.0),], },), ],},),

("3D View Tool: Sculpt, Lasso Trim",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.trim_lasso_gesture", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), ],},),

("3D View Tool: Sculpt, Line Mask",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("paint.mask_line_gesture",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("value", 1.0),], },), 
            ("paint.mask_line_gesture",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("value", 0.0),], },), ],},),

("3D View Tool: Sculpt, Line Project",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.project_line_gesture", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), ],},),

("3D View Tool: Sculpt, Mask By Color",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.mask_by_color", {"type": 'LEFTMOUSE', "value": 'ANY'}, None), 
            ("sculpt.mask_by_color", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("sculpt.mask_by_color", {"type": 'MIDDLEMOUSE', "value": 'ANY'}, None), 
            ("sculpt.mask_by_color", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Sculpt, Mask by Color",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.mask_by_color", {"type": 'LEFTMOUSE', "value": 'ANY'}, None), 
            ("sculpt.mask_by_color", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), ],},),

("3D View Tool: Sculpt, Mesh Filter",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.mesh_filter", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("sculpt.mesh_filter", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Select Box",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.select_box", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("view3d.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),], },), 
            ("view3d.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },), 
            ("view3d.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True, "ctrl": True},{"properties": [("mode", 'AND'),], },), ],},),

("3D View Tool: Select Circle",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },), 
            ("view3d.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),("mode", 'ADD'),], },), 
            ("view3d.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),("mode", 'SUB'),], },), ],},),

("3D View Tool: Select Lasso",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("view3d.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),], },), 
            ("view3d.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },), 
            ("view3d.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True, "ctrl": True},{"properties": [("mode", 'AND'),], },), ],},),

("3D View Tool: Shear",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.shear",{"type": 'EVT_TWEAK_L', "value": 'NORTH'},{"properties": [("orient_axis_ortho", 'Y'),("release_confirm", True),], },), 
            ("transform.shear",{"type": 'EVT_TWEAK_L', "value": 'SOUTH'},{"properties": [("orient_axis_ortho", 'Y'),("release_confirm", True),], },), 
            ("transform.shear",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("orient_axis_ortho", 'X'),("release_confirm", True),], },), 
            ("transform.shear",{"type": 'EVT_TWEAK_M', "value": 'NORTH'},{"properties": [("orient_axis_ortho", 'Y'),("release_confirm", True),], },), 
            ("transform.shear",{"type": 'EVT_TWEAK_M', "value": 'SOUTH'},{"properties": [("orient_axis_ortho", 'Y'),("release_confirm", True),], },), 
            ("transform.shear",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("orient_axis_ortho", 'X'),("release_confirm", True),], },), ],},),

("3D View Tool: Transform",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("transform.from_gizmo", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("transform.from_gizmo", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None), ],},),

("3D View Tool: Tweak",
    {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {"items":
            [("view3d.select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("deselect_all", True),], },), 
            ("view3d.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("toggle", True),], },), ],},),

#############
# ANIMATION #
#############
("Animation",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("wm.context_toggle",{"type": 'T', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.show_seconds'),], },), ],},),

("Animation Channels",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("anim.channels_click", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None), 
            ("anim.channels_click",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },), 
            ("anim.channels_click",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("children_only", True),], },), 
            ("anim.channels_rename", {"type": 'RET', "value": 'PRESS', "repeat": True}, None), 
            ("anim.channels_rename", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None), 
            ("anim.channel_select_keys", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None), 
            ("anim.channel_select_keys",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "shift": True},{"properties": [("extend", True),], },), 
            ("anim.channels_find", {"type": 'F', "value": 'PRESS', "ctrl": True, "repeat": True}, None), 
            ("anim.channels_select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },), 
            ("anim.channels_select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },), 
            ("anim.channels_select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },), 
            ("anim.channels_select_box", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None), 
            ("anim.channels_select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("extend", True),], },), 
            ("anim.channels_select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("deselect", True),], },), 
            ("anim.channels_delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None), 
            ("anim.channels_delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None), 
            ("anim.channels_setting_toggle", {"type": 'W', "value": 'PRESS', "shift": True, "repeat": True}, None), 
            ("anim.channels_setting_enable", {"type": 'W', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None), 
            ("anim.channels_setting_disable", {"type": 'W', "value": 'PRESS', "alt": True, "repeat": True}, None), 
            ("anim.channels_editable_toggle", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None), 
            ("anim.channels_expand", {"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True}, None), 
            ("anim.channels_collapse", {"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True}, None), 
            ("anim.channels_expand",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("all", False),], },), 
            ("anim.channels_collapse",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("all", False),], },), 
            ("anim.channels_move",{"type": 'PAGE_UP', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'UP'),], },), 
            ("anim.channels_move",{"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'DOWN'),], },), 
            ("anim.channels_move",{"type": 'PAGE_UP', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'TOP'),], },), 
            ("anim.channels_move",{"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'BOTTOM'),],},  ), 
            ("anim.channels_group", {"type": 'G', "value": 'PRESS', "ctrl": True, "repeat": True}, None), 
            ("anim.channels_ungroup", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True}, None), 
            ("wm.call_menu",  {"type": 'RIGHTMOUSE', "value": 'PRESS'},  {"properties":[("name", 'DOPESHEET_MT_channel_context_menu'),],},  ), 
            ("wm.call_menu",  {"type": 'APP', "value": 'PRESS', "repeat": True},  {"properties":[("name", 'DOPESHEET_MT_channel_context_menu'),],},  ), ],},),

############
# ARMATURE #
############
("Armature",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("armature.hide",{"type": 'H', "value": 'PRESS', "ctrl": True},{"properties":[("unselected", False),],},),
            ("armature.hide",{"type": 'H', "value": 'PRESS', "shift": True},{"properties":[("unselected", True),],},),
            ("armature.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
            ("armature.parent_set", {"type": 'P', "value": 'PRESS'}, None),
            ("armature.parent_clear", {"type": 'P', "value": 'PRESS', "shift": True}, None),
            ("armature.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'SELECT'),],},),
            ("armature.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},{"properties":[("action", 'DESELECT'),],},),
            ("armature.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'INVERT'),],},),
            ("armature.select_hierarchy",{"type": 'LEFT_BRACKET', "value": 'PRESS'},{"properties":[("direction", 'PARENT'),("extend", False),],},),
            ("armature.select_hierarchy",{"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True},{"properties":[("direction", 'PARENT'),("extend", True),],},),
            ("armature.select_hierarchy",{"type": 'RIGHT_BRACKET', "value": 'PRESS'},{"properties":[("direction", 'CHILD'),("extend", False),],},),
            ("armature.select_hierarchy",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True},{"properties":[("direction", 'CHILD'),("extend", True),],},),
            ("armature.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("armature.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("armature.select_similar", {"type": 'G', "value": 'PRESS', "shift": True}, None),
            ("armature.select_linked_pick",{"type": 'RIGHT_BRACKET', "value": 'PRESS'},{"properties":[("deselect", False),],},),
            ("armature.shortest_path_pick", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
            ("wm.call_menu",{"type": 'DEL', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_armature_delete'),],},),
            ("wm.call_menu",{"type": 'BACK_SPACE', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_armature_delete'),],},),
            ("armature.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("armature.dissolve", {"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True}, None),
            ("armature.dissolve", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_armature_context_menu'),],},),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_armature_context_menu'),],},),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties":[("name", 'builtin.select_box'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS'},{"properties":[("name", 'builtin.move'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS'},{"properties":[("name", 'builtin.rotate'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS'},{"properties":[("name", 'builtin.scale'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS'},{"properties":[("name", 'builtin.transform'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS'},{"properties":[("name", 'builtin.annotate'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS'},{"properties":[("name", 'builtin.measure'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS'},{"properties":[("name", 'builtin.cursor'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'Y', "value": 'PRESS'},{"properties":[("name", 'builtin.roll'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS', "ctrl": True},{"properties":[("name", 'builtin.extrude'),("cycle", True),],},),],},),

#########
# BEVEL #
#########
("Bevel Modal Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None), 
            ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("CONFIRM", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None), 
            ("VALUE_OFFSET", {"type": 'A', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("VALUE_PROFILE", {"type": 'P', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("VALUE_SEGMENTS", {"type": 'S', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("SEGMENTS_UP", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "any": True}, None), 
            ("SEGMENTS_UP", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("SEGMENTS_DOWN", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "any": True}, None), 
            ("SEGMENTS_DOWN", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("OFFSET_MODE_CHANGE", {"type": 'M', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("CLAMP_OVERLAP_TOGGLE", {"type": 'C', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("AFFECT_CHANGE", {"type": 'V', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("HARDEN_NORMALS_TOGGLE", {"type": 'H', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("MARK_SEAM_TOGGLE", {"type": 'U', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("MARK_SHARP_TOGGLE", {"type": 'K', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("OUTER_MITER_CHANGE", {"type": 'O', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("INNER_MITER_CHANGE", {"type": 'I', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("PROFILE_TYPE_CHANGE", {"type": 'Z', "value": 'PRESS', "any": True, "repeat": True}, None), 
            ("VERTEX_MESH_CHANGE", {"type": 'N', "value": 'PRESS', "any": True, "repeat": True}, None), ],},),

###############
# CLIP EDITOR #
###############
("Clip",
    {"space_type": 'CLIP_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",  {"type": 'RET', "value": 'PRESS', "repeat": True},  {"properties":[("name", 'TOPBAR_PT_name'),("keep_open", False),],},  ), 
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None), 
            ("clip.open", {"type": 'O', "value": 'PRESS', "alt": True, "repeat": True}, None), 
            ("clip.track_markers",  {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True, "repeat": True},  {"properties":[("backwards", True),("sequence", False),],},  ), 
            ("clip.track_markers",  {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True, "repeat": True},  {"properties":[("backwards", False),("sequence", False),],},  ), 
            ("clip.track_markers",  {"type": 'T', "value": 'PRESS', "ctrl": True, "repeat": True},  {"properties":[("backwards", False),("sequence", True),],},  ), 
            ("clip.track_markers",  {"type": 'T', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},  {"properties":[("backwards", True),("sequence", True),],},  ), 
            ("wm.context_toggle_enum",  {"type": 'TAB', "value": 'PRESS', "repeat": True},{"properties":[("data_path", 'space_data.mode'),("value_1", 'TRACKING'),("value_2", 'MASK'),],},),
            ("clip.solve_camera", {"type": 'S', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("clip.prefetch", {"type": 'P', "value": 'PRESS', "repeat": True}, None),],},),

("Clip Dopesheet Editor",
    {"space_type": 'CLIP_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("clip.dopesheet_select_channel",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties":[("extend", True),],},),
            ("clip.dopesheet_view_all", {"type": 'HOME', "value": 'PRESS', "repeat": True}, None),
            ("clip.dopesheet_view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),],},),

("Clip Editor",
    {"space_type": 'CLIP_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("clip.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("clip.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
            ("clip.view_pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
            ("clip.view_zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
            ("clip.view_zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
            ("clip.view_zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
            ("clip.view_zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS'}, None),
            ("clip.view_zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS'}, None),
            ("clip.view_zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS', "alt": True}, None),
            ("clip.view_zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("clip.view_zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True}, None),
            ("clip.view_zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True}, None),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties":[("ratio", 8.0),],},),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties":[("ratio", 4.0),],},),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("ratio", 2.0),], },),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_8', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("ratio", 8.0),], },),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_4', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("ratio", 4.0),], },),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_2', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("ratio", 2.0),], },),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_1', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 1.0),], },),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_2', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 0.5),], },),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_4', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 0.25),], },),
            ("clip.view_zoom_ratio",{"type": 'NUMPAD_8', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 0.125),], },),
            ("clip.view_all", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("clip.view_selected", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("clip.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("clip.view_ndof", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
            ("clip.frame_jump",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("position", 'PATHSTART'),], },),
            ("clip.frame_jump",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("position", 'PATHEND'),], },),
            ("clip.frame_jump",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "alt": True, "repeat": True},{"properties": [("position", 'FAILEDPREV'),], },),
            ("clip.frame_jump",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "alt": True, "repeat": True},{"properties": [("position", 'PATHSTART'),], },),
            ("clip.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("clip.select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),("deselect_all", True),], },),
            ("clip.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("clip.select_box", {"type": 'Q', "value": 'PRESS', "repeat": True}, None),
            ("clip.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("clip.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("clip.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("wm.call_menu",{"type": 'G', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("name", 'CLIP_MT_select_grouped'),], },),
            ("clip.add_marker_slide", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
            ("clip.delete_marker", {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("clip.delete_marker", {"type": 'DEL', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("clip.slide_marker", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("clip.disable_markers",{"type": 'D', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("action", 'TOGGLE'),], },),
            ("clip.delete_track", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("clip.delete_track", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("clip.lock_tracks",{"type": 'L', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'LOCK'),], },),
            ("clip.lock_tracks",{"type": 'L', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("action", 'UNLOCK'),], },),
            ("clip.hide_tracks",{"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("unselected", False),], },),
            ("clip.hide_tracks",{"type": 'H', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("unselected", True),], },),
            ("clip.hide_tracks_clear", {"type": 'H', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("clip.slide_plane_marker", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("clip.keyframe_insert", {"type": 'S', "value": 'PRESS', "repeat": True}, None),
            ("clip.keyframe_delete", {"type": 'S', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("clip.join_tracks", {"type": 'J', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'CLIP_MT_tracking_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'CLIP_MT_tracking_context_menu'),], },),
            ("wm.context_toggle",{"type": 'L', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'space_data.lock_selection'),], },),
            ("wm.context_toggle",{"type": 'D', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("data_path", 'space_data.show_disabled'),], },),
            ("wm.context_toggle",{"type": 'S', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("data_path", 'space_data.show_marker_search'),], },),
            ("wm.context_toggle",{"type": 'M', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'space_data.use_mute_footage'),], },),
            ("transform.translate", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("transform.resize", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("transform.rotate", {"type": 'E', "value": 'PRESS', "repeat": True}, None),
            ("clip.clear_track_path",{"type": 'T', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("action", 'REMAINED'),("clear_active", False),], },),
            ("clip.clear_track_path",{"type": 'T', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("action", 'UPTO'),("clear_active", False),], },),
            ("clip.clear_track_path",{"type": 'T', "value": 'PRESS', "shift": True, "alt": True, "repeat": True},{"properties": [("action", 'ALL'),("clear_active", False),], },),
            ("wm.call_menu_pie",{"type": 'PERIOD', "value": 'PRESS', "repeat": True},{"properties": [("name", 'CLIP_MT_pivot_pie'),], },),
            ("clip.copy_tracks", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("clip.paste_tracks", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),],},),

("Clip Graph Editor",
    {"space_type": 'CLIP_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("clip.graph_select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),], },),
            ("clip.graph_select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("clip.graph_select_box", {"type": 'Q', "value": 'PRESS', "repeat": True}, None),
            ("clip.graph_select_all", {"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("clip.graph_delete_curve", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("clip.graph_delete_curve", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("clip.graph_delete_knot", {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("clip.graph_delete_knot", {"type": 'DEL', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("clip.graph_view_all", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("clip.graph_view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("clip.graph_center_current_frame", {"type": 'NUMPAD_0', "value": 'PRESS', "repeat": True}, None),
            ("wm.context_toggle",{"type": 'L', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'space_data.lock_time_cursor'),], },),
            ("clip.clear_track_path",{"type": 'T', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("action", 'REMAINED'),("clear_active", True),], },),
            ("clip.clear_track_path",{"type": 'T', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("action", 'UPTO'),("clear_active", True),], },),
            ("clip.clear_track_path",{"type": 'T', "value": 'PRESS', "shift": True, "alt": True, "repeat": True},{"properties": [("action", 'ALL'),("clear_active", True),], },),
            ("clip.graph_disable_markers",{"type": 'D', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("action", 'TOGGLE'),], },),
            ("transform.translate", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("transform.resize", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("transform.rotate", {"type": 'E', "value": 'PRESS', "repeat": True}, None),],},),

("Clip Time Scrub",
    {"space_type": 'CLIP_EDITOR', "region_type": 'PREVIEW'},
        {"items":
            [("clip.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),],},),

###########
# CONSOLE #
###########
("Console",
    {"space_type": 'CONSOLE', "region_type": 'WINDOW'},
        {"items":
            [("console.move",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),], },),
            ("console.move",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),], },),
            ("console.move",{"type": 'HOME', "value": 'PRESS', "repeat": True},{"properties": [("type", 'LINE_BEGIN'),], },),
            ("console.move",{"type": 'END', "value": 'PRESS', "repeat": True},{"properties": [("type", 'LINE_END'),], },),
            ("wm.context_cycle_int",{"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("data_path", 'space_data.font_size'),("reverse", False),], },),
            ("wm.context_cycle_int",{"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("data_path", 'space_data.font_size'),("reverse", True),], },),
            ("wm.context_cycle_int",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.font_size'),("reverse", False),], },),
            ("wm.context_cycle_int",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.font_size'),("reverse", True),], },),
            ("console.move",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("console.move",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_CHARACTER'),], },),
            ("console.history_cycle",{"type": 'UP_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("reverse", True),], },),
            ("console.history_cycle",{"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("reverse", False),], },),
            ("console.delete",{"type": 'DEL', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_CHARACTER'),], },),
            ("console.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("console.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("console.delete",{"type": 'DEL', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),], },),
            ("console.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),], },),
            ("console.clear_line", {"type": 'RET', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("console.clear_line", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("console.execute",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("interactive", True),], },),
            ("console.execute",{"type": 'NUMPAD_ENTER', "value": 'PRESS', "repeat": True},{"properties": [("interactive", True),], },),
            ("console.copy_as_script", {"type": 'C', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
            ("console.copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("console.paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("console.select_set", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("console.select_word", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
            ("console.insert",{"type": 'TAB', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("text", '\t'),], },),
            ("console.indent_or_autocomplete", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("console.unindent", {"type": 'TAB', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'CONSOLE_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'CONSOLE_MT_context_menu'),], },),
            ("console.insert", {"type": 'TEXTINPUT', "value": 'ANY', "any": True}, None),
            ("console.autocomplete", {"type": 'DOWN_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True}, None),],},),

#########
# CURVE #
#########
("Curve",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("curve.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'SELECT'),],},),
            ("curve.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},{"properties":[("action", 'DESELECT'),],},),
            ("curve.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'INVERT'),],},),
            ("curve.select_row", {"type": 'R', "value": 'PRESS', "shift": True}, None),
            ("curve.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("curve.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("curve.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS'}, None),
            ("curve.shortest_path_pick", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
            ("curve.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("wm.call_menu",{"type": 'BACK_SPACE', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_curve_delete'),],},),
            ("wm.call_menu",{"type": 'DEL', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_curve_delete'),],},),
            ("curve.dissolve_verts", {"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True}, None),
            ("curve.dissolve_verts", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
            ("curve.tilt_clear", {"type": 'T', "value": 'PRESS', "alt": True}, None),
            ("curve.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
            ("curve.hide",{"type": 'H', "value": 'PRESS', "ctrl": True},{"properties":[("unselected", False),],},),
            ("curve.hide",{"type": 'H', "value": 'PRESS', "shift": True},{"properties":[("unselected", True),],},),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_curve_context_menu'),],},),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_curve_context_menu'),],},),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS'},{"properties":[("data_path", 'tool_settings.use_proportional_edit'),],},),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties":[("name", 'builtin.select_box'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS'},{"properties":[("name", 'builtin.move'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS'},{"properties":[("name", 'builtin.rotate'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS'},{"properties":[("name", 'builtin.scale'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS'},{"properties":[("name", 'builtin.transform'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS'},{"properties":[("name", 'builtin.annotate'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS'},{"properties":[("name", 'builtin.measure'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS'},{"properties":[("name", 'builtin.cursor'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS', "ctrl": True},{"properties":[("name", 'builtin.extrude'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'Y', "value": 'PRESS'},{"properties":[("name", 'builtin.tilt'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'U', "value": 'PRESS'},{"properties":[("name", 'builtin.radius'),("cycle", True),],},),],},),

##################
# CUSTOM NORMALS #
##################
("Custom Normals Modal Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
            ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("RESET", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("INVERT", {"type": 'I', "value": 'PRESS', "repeat": True}, None),
            ("SPHERIZE", {"type": 'S', "value": 'PRESS', "repeat": True}, None),
            ("ALIGN", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("USE_MOUSE", {"type": 'M', "value": 'PRESS', "repeat": True}, None),
            ("USE_PIVOT", {"type": 'L', "value": 'PRESS', "repeat": True}, None),
            ("USE_OBJECT", {"type": 'O', "value": 'PRESS', "repeat": True}, None),
            ("SET_USE_3DCURSOR", {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True}, None),
            ("SET_USE_SELECTED", {"type": 'RIGHTMOUSE', "value": 'CLICK', "ctrl": True}, None),],},),

#############
# DOPESHEET #
#############
("Dopesheet",
    {"space_type": 'DOPESHEET_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("screen.frame_offset",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("delta", -1),], },),
            ("screen.frame_offset",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("delta", 1),], },),
            ("screen.frame_jump",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("end", True),], },),
            ("screen.frame_jump",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("end", False),], },),
            ("action.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),("deselect_all", True),("column", False),("channel", False),], },),
            ("action.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True},{"properties": [("extend", False),("column", True),("channel", False),], },),
            ("action.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),("column", False),("channel", False),], },),
            ("action.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties": [("extend", True),("column", True),("channel", False),], },),
            ("action.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},{"properties": [("extend", False),("column", False),("channel", True),], },),
            ("action.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},{"properties": [("extend", True),("column", False),("channel", True),], },),
            ("action.select_leftright",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("mode", 'CHECK'),("extend", True),], },),
            ("action.select_leftright",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'LEFT'),("extend", False),], },),
            ("action.select_leftright",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'RIGHT'),("extend", False),], },),
            ("action.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("action.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("action.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("action.select_box",{"type": 'Q', "value": 'PRESS', "repeat": True},{"properties": [("axis_range", False),], },),
            ("action.select_box",{"type": 'Q', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("axis_range", True),], },),
            ("action.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("axis_range", False),("wait_for_input", False),("mode", 'SET'),("tweak", True),], },),
            ("action.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("axis_range", False),("wait_for_input", False),("mode", 'ADD'),("tweak", True),], },),
            ("action.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("axis_range", False),("wait_for_input", False),("mode", 'SUB'),("tweak", True),], },),
            ("action.select_column",{"type": 'K', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'KEYS'),], },),
            ("action.select_column",{"type": 'K', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("mode", 'CFRA'),], },),
            ("action.select_column",{"type": 'K', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("mode", 'MARKERS_COLUMN'),], },),
            ("action.select_column",{"type": 'K', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("mode", 'MARKERS_BETWEEN'),], },),
            ("action.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("action.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("action.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True}, None),
            ("action.frame_jump", {"type": 'G', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.context_menu_enum",{"type": 'X', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'space_data.auto_snap'),], },),
            ("wm.call_menu_pie",{"type": 'X', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("name", 'DOPESHEET_MT_snap_pie'),], },),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'DOPESHEET_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'DOPESHEET_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True},{"properties": [("name", 'DOPESHEET_MT_delete'),], },),
            ("wm.call_menu",{"type": 'DEL', "value": 'PRESS', "repeat": True},{"properties": [("name", 'DOPESHEET_MT_delete'),], },),
            ("action.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("action.keyframe_insert", {"type": 'S', "value": 'PRESS', "repeat": True}, None),
            ("action.copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("action.paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("action.paste",{"type": 'V', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("flipped", True),], },),
            ("action.previewrange_set", {"type": 'P', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True}, None),
            ("action.view_all", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("action.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("action.view_selected", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("action.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS', "repeat": True}, None),
            ("anim.channels_editable_toggle", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
            ("anim.channels_find", {"type": 'F', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("transform.transform",{"type": 'W', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TIME_TRANSLATE'),], },),
            ("transform.transform",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'TIME_TRANSLATE'),], },),
            ("transform.transform",{"type": 'EVT_TWEAK_M', "value": 'ANY'},{"properties": [("mode", 'TIME_TRANSLATE'),], },),
            ("transform.transform",{"type": 'E', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TIME_EXTEND'),], },),
            ("transform.transform",{"type": 'R', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TIME_SCALE'),], },),
            ("transform.transform",{"type": 'T', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("mode", 'TIME_SLIDE'),], },),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_proportional_action'),], },),
            ("marker.add", {"type": 'M', "value": 'PRESS', "repeat": True}, None),
            ("marker.rename", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),
            ("anim.start_frame_set", {"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("anim.end_frame_set", {"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True}, None),],},),

("Dopesheet Generic",
    {"space_type": 'DOPESHEET_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("wm.context_toggle",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.show_region_ui'),], },),],},),

##############
# EYEDROPPER #
##############
("Eyedropper ColorRamp PointSampling Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CANCEL", {"type": 'BACK_SPACE', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("SAMPLE_CONFIRM", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
            ("SAMPLE_CONFIRM", {"type": 'RET', "value": 'RELEASE', "any": True}, None),
            ("SAMPLE_CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'RELEASE', "any": True}, None),
            ("SAMPLE_SAMPLE", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ("SAMPLE_RESET", {"type": 'SPACE', "value": 'RELEASE', "any": True}, None),],},),

("Eyedropper Modal Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
            ("SAMPLE_CONFIRM", {"type": 'RET', "value": 'RELEASE', "any": True}, None),
            ("SAMPLE_CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'RELEASE', "any": True}, None),
            ("SAMPLE_CONFIRM", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),
            ("SAMPLE_BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ("SAMPLE_RESET", {"type": 'SPACE', "value": 'RELEASE', "any": True}, None),],},),

################
# FILE BROWSER #
################
("File Browser",
    {"space_type": 'FILE_BROWSER', "region_type": 'WINDOW'},
        {"items":
            [("file.parent", {"type": 'UP_ARROW', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("file.parent", {"type": 'UP_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("file.previous", {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("file.previous", {"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("file.next", {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("file.next", {"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("file.refresh", {"type": 'R', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("file.previous", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("file.next", {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("wm.context_toggle",{"type": 'H', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'space_data.params.show_hidden'),], },),
            ("file.directory_new",{"type": 'I', "value": 'PRESS', "repeat": True},{"properties": [("confirm", False),], },),
            ("file.rename", {"type": 'F2', "value": 'PRESS', "repeat": True}, None),
            ("file.delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("file.smoothscroll", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
            ("wm.context_toggle",{"type": 'T', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'space_data.show_region_toolbar'),], },),
            ("file.bookmark_add", {"type": 'B', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("file.filenum",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True},{"properties": [("increment", 1),], },),
            ("file.filenum",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("increment", 10),], },),
            ("file.filenum",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("increment", 100),], },),
            ("file.filenum",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True},{"properties": [("increment", -1),], },),
            ("file.filenum",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("increment", -10),], },),
            ("file.filenum",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("increment", -100),], },),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'FILEBROWSER_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'FILEBROWSER_MT_context_menu'),], },),],},),

("File Browser Buttons",
    {"space_type": 'FILE_BROWSER', "region_type": 'WINDOW'},
        {"items":
            [("file.filenum",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True},{"properties": [("increment", 1),], },),
            ("file.filenum",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("increment", 10),], },),
            ("file.filenum",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("increment", 100),], },),
            ("file.filenum",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True},{"properties": [("increment", -1),  ], },),
            ("file.filenum",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("increment", -10),  ], },),
            ("file.filenum",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("increment", -100),  ], },),],},),

("File Browser Main",
    {"space_type": 'FILE_BROWSER', "region_type": 'WINDOW'},
        {"items":
            [("file.execute",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'},{"properties": [("need_active", True),  ], },),
            ("file.refresh", {"type": 'R', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("file.select", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
            ("file.select",{"type": 'LEFTMOUSE', "value": 'CLICK'},{"properties": [("open", False),  ("deselect_all", True),  ], },),
            ("file.select",{"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},{"properties": [("extend", True),  ("open", False),  ], },),
            ("file.select",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},{"properties": [("extend", True),  ("fill", True),  ("open", False),  ], },),
            ("file.select",{"type": 'RIGHTMOUSE', "value": 'CLICK', "shift": True},{"properties": [("extend", True),  ("open", False),  ], },),
            ("file.select",{"type": 'RIGHTMOUSE', "value": 'CLICK', "alt": True},{"properties": [("extend", True),  ("fill", True),  ("open", False),  ], },),
            ("file.select_walk",{"type": 'UP_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'UP'),  ], },),
            ("file.select_walk",{"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'UP'),  ("extend", True),  ], },),
            ("file.select_walk",{"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("direction", 'UP'),  ("extend", True),  ("fill", True),  ], },),
            ("file.select_walk",{"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'DOWN'),  ], },),
            ("file.select_walk",{"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'DOWN'),  ("extend", True),  ], },),
            ("file.select_walk",{"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("direction", 'DOWN'),  ("extend", True),  ("fill", True),  ], },),
            ("file.select_walk",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'LEFT'),  ], },),
            ("file.select_walk",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'LEFT'),  ("extend", True),  ], },),
            ("file.select_walk",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("direction", 'LEFT'),  ("extend", True),  ("fill", True),  ], },),
            ("file.select_walk",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'RIGHT'),  ], },),
            ("file.select_walk",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'RIGHT'),  ("extend", True),  ], },),
            ("file.select_walk",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("direction", 'RIGHT'),  ("extend", True),  ("fill", True),  ], },),
            ("file.previous", {"type": 'BUTTON4MOUSE', "value": 'CLICK'}, None),
            ("file.next", {"type": 'BUTTON5MOUSE', "value": 'CLICK'}, None),
            ("file.select_all", {"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("file.select_box", {"type": 'Q', "value": 'PRESS', "repeat": True}, None),
            ("file.select_box", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("file.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),  ], },),
            ("file.highlight", {"type": 'MOUSEMOVE', "value": 'ANY', "any": True}, None),
            ("file.sort_column_ui_context", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),],},),

########
# FONT #
########
("Font",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("font.style_toggle",{"type": 'B', "value": 'PRESS', "ctrl": True},{"properties": [("style", 'BOLD'),  ], },),
            ("font.style_toggle",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties": [("style", 'ITALIC'),  ], },),
            ("font.style_toggle",{"type": 'U', "value": 'PRESS', "ctrl": True},{"properties": [("style", 'UNDERLINE'),  ], },),
            ("font.style_toggle",{"type": 'P', "value": 'PRESS', "ctrl": True},{"properties": [("style", 'SMALL_CAPS'),  ], },),
            ("font.delete",{"type": 'DEL', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_OR_SELECTION'),  ], },),
            ("font.delete",{"type": 'DEL', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),  ], },),
            ("font.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_OR_SELECTION'),  ], },),
            ("font.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_OR_SELECTION'),  ], },),
            ("font.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),],},),
            ("font.move",{"type": 'HOME', "value": 'PRESS'},{"properties": [("type", 'LINE_BEGIN'),], },),
            ("font.move",{"type": 'END', "value": 'PRESS'},{"properties": [("type", 'LINE_END'),], },),
            ("font.move",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("font.move",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_CHARACTER'),], },),
            ("font.move",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),], },),
            ("font.move",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),], },),
            ("font.move",{"type": 'UP_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_LINE'),], },),
            ("font.move",{"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_LINE'),], },),
            ("font.move",{"type": 'PAGE_UP', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_PAGE'),], },),
            ("font.move",{"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_PAGE'),], },),
            ("font.move_select",{"type": 'HOME', "value": 'PRESS', "shift": True},{"properties": [("type", 'LINE_BEGIN'),], },),
            ("font.move_select",{"type": 'END', "value": 'PRESS', "shift": True},{"properties": [("type", 'LINE_END'),], },),
            ("font.move_select",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("font.move_select",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'NEXT_CHARACTER'),], },),
            ("font.move_select",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),], },),
            ("font.move_select",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),], },),
            ("font.move_select",{"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_LINE'),], },),
            ("font.move_select",{"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'NEXT_LINE'),], },),
            ("font.move_select",{"type": 'PAGE_UP', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_PAGE'),], },),
            ("font.move_select",{"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'NEXT_PAGE'),], },),
            ("font.change_spacing",{"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("delta", -1),], },),
            ("font.change_spacing",{"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("delta", 1),], },),
            ("font.change_character",{"type": 'UP_ARROW', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("delta", 1),], },),
            ("font.change_character",{"type": 'DOWN_ARROW', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("delta", -1),], },),
            ("font.select_all", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
            ("font.text_copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
            ("font.text_cut", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
            ("font.text_paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("font.line_break", {"type": 'RET', "value": 'PRESS'}, None),
            ("font.text_insert", {"type": 'TEXTINPUT', "value": 'ANY', "any": True}, None),
            ("font.text_insert",{"type": 'BACK_SPACE', "value": 'PRESS', "alt": True},{"properties": [("accent", True),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_edit_font_context_menu'),], },),],},),

##########
# FRAMES #
##########
("Frames",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("screen.frame_jump",{"type": 'MEDIA_LAST', "value": 'PRESS', "repeat": True},{"properties": [("end", True),], },),
            ("screen.frame_jump",{"type": 'MEDIA_FIRST', "value": 'PRESS', "repeat": True},{"properties": [("end", False),], },),
            ("screen.animation_play", {"type": 'SPACE', "value": 'PRESS', "repeat": True}, None),
            ("screen.animation_cancel", {"type": 'ESC', "value": 'PRESS', "repeat": True}, None),
            ("screen.animation_play", {"type": 'MEDIA_PLAY', "value": 'PRESS', "repeat": True}, None),
            ("screen.animation_cancel", {"type": 'MEDIA_STOP', "value": 'PRESS', "repeat": True}, None),],},),

#################
# GENERIC GIZMO #
#################
("Generic Gizmo",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gizmogroup.gizmo_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),],},),

("Generic Gizmo Click Drag",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gizmogroup.gizmo_tweak", {"type": 'LEFTMOUSE', "value": 'CLICK', "any": True}, None),
            ("gizmogroup.gizmo_tweak", {"type": 'EVT_TWEAK_L', "value": 'ANY', "any": True}, None),],},),

("Generic Gizmo Drag",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gizmogroup.gizmo_tweak", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),],},),

("Generic Gizmo Maybe Drag",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gizmogroup.gizmo_tweak", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),],},),

("Generic Gizmo Select",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gizmogroup.gizmo_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),],},),

("Generic Gizmo Tweak Modal Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
            ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
            ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),],},),

################
# GENERIC TOOL #
################
("Generic Tool: Annotate",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.annotate",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("mode", 'DRAW'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'DRAW'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),],},),

("Generic Tool: Annotate Eraser",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.annotate",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),],},),

("Generic Tool: Annotate Line",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.annotate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'DRAW_STRAIGHT'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'DRAW_STRAIGHT'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),],},),

("Generic Tool: Annotate Polygon",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.annotate",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("mode", 'DRAW_POLY'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("mode", 'DRAW_POLY'),("wait_for_input", False),], },),
            ("gpencil.annotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),],},),

###########
# GESTURE #
###########
("Gesture Box",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
            ("SELECT", {"type": 'RIGHTMOUSE', "value": 'RELEASE', "any": True}, None),
            ("BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
            ("DESELECT", {"type": 'LEFTMOUSE', "value": 'RELEASE', "shift": True}, None),
            ("BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("SELECT", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),
            ("BEGIN", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("DESELECT", {"type": 'MIDDLEMOUSE', "value": 'RELEASE'}, None),],},),

("Gesture Lasso",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("MOVE", {"type": 'SPACE', "value": 'ANY', "any": True}, None),],},),

("Gesture Straight Line",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
            ("BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("SELECT", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),],},),

("Gesture Zoom Border",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
            ("BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("IN", {"type": 'LEFTMOUSE', "value": 'RELEASE'}, None),
            ("BEGIN", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("OUT", {"type": 'MIDDLEMOUSE', "value": 'RELEASE'}, None),],},),

################
# GRAPH EDITOR #
################
("Graph Editor",
    {"space_type": 'GRAPH_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("screen.frame_offset",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("delta", -1),], },),
            ("screen.frame_offset",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("delta", 1),], },),
            ("screen.frame_jump",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("end", True),], },),
            ("screen.frame_jump",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("end", False),], },),
            ("graph.cursor_set", {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True}, None),
            ("graph.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),("deselect_all", True),("column", False),("curves", False),], },),
            ("graph.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True},{"properties": [("extend", False),("column", True),("curves", False),], },),
            ("graph.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),("column", False),("curves", False),], },),
            ("graph.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties": [("extend", True),("column", True),("curves", False),], },),
            ("graph.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},{"properties": [("extend", False),("column", False),("curves", True),], },),
            ("graph.clickselect",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},{"properties": [("extend", True),("column", False),("curves", True),], },),
            ("graph.select_leftright",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("mode", 'CHECK'),("extend", True),], },),
            ("graph.select_leftright",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'LEFT'),("extend", False),], },),
            ("graph.select_leftright",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'RIGHT'),("extend", False),], },),
            ("graph.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("graph.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("graph.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("graph.select_box",{"type": 'Q', "value": 'PRESS', "repeat": True},{"properties": [("axis_range", False),], },),
            ("graph.select_box",{"type": 'Q', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("axis_range", True),], },),
            ("graph.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("axis_range", False),("tweak", True),("mode", 'SET'),], },),
            ("graph.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("axis_range", False),("tweak", True),("mode", 'ADD'),], },),
            ("graph.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("axis_range", False),("tweak", True),("mode", 'SUB'),], },),
            ("graph.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("graph.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("graph.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True}, None),
            ("wm.call_menu",{"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True},{"properties": [("name", 'GRAPH_MT_delete'),], },),
            ("wm.call_menu",{"type": 'DEL', "value": 'PRESS', "repeat": True},{"properties": [("name", 'GRAPH_MT_delete'),], },),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'GRAPH_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'GRAPH_MT_context_menu'),], },),
            ("graph.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("graph.keyframe_insert", {"type": 'S', "value": 'PRESS', "repeat": True}, None),
            ("graph.copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("graph.paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("graph.paste",{"type": 'V', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("flipped", True),], },),
            ("graph.previewrange_set", {"type": 'P', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True}, None),
            ("graph.view_all", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("graph.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("graph.view_selected", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("graph.view_frame", {"type": 'A', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("anim.channels_editable_toggle", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
            ("transform.translate", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("transform.translate", {"type": 'EVT_TWEAK_M', "value": 'ANY'}, None),
            ("transform.transform",{"type": 'Y', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TIME_EXTEND'),], },),
            ("transform.rotate", {"type": 'E', "value": 'PRESS', "repeat": True}, None),
            ("transform.resize", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_proportional_fcurve'),], },),
            ("wm.context_menu_enum",{"type": 'X', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'space_data.auto_snap'),], },),
            ("marker.add", {"type": 'M', "value": 'PRESS', "repeat": True}, None),
            ("marker.rename", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),
            ("wm.call_menu_pie",{"type": 'X', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("name", 'GRAPH_MT_snap_pie'),], },),],},),

("Graph Editor Generic",
    {"space_type": 'GRAPH_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("anim.channels_find", {"type": 'F', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("graph.hide",{"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("unselected", False),], },),
            ("graph.hide",{"type": 'H', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("unselected", True),], },),
            ("graph.reveal", {"type": 'H', "value": 'PRESS', "alt": True, "repeat": True}, None),],},),

#################
# GREASE PENCIL #
#################
("Grease Pencil",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.active_frames_delete_all", {"type": 'BACK_SPACE', "value": 'PRESS', "key_modifier": 'D', "repeat": True}, None),
            ("gpencil.active_frames_delete_all", {"type": 'DEL', "value": 'PRESS', "key_modifier": 'D', "repeat": True}, None),],},),

("Grease Pencil Stroke Curve Edit Mode",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.stroke_editcurve_set_handle_type", {"type": 'V', "value": 'PRESS'}, None),],},),

("Grease Pencil Stroke Edit Mode",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select",{"type": 'LEFTMOUSE', "value": 'CLICK'},{"properties": [("deselect_all", True),], },),
            ("gpencil.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),("toggle", True),], },),
            ("gpencil.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("gpencil.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("gpencil.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("gpencil.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.select_alternate", {"type": 'L', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.call_menu",{"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_MT_edit_gpencil_delete'),], },),
            ("wm.call_menu",{"type": 'DEL', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_MT_edit_gpencil_delete'),], },),
            ("gpencil.dissolve", {"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("gpencil.dissolve", {"type": 'DEL', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("gpencil.active_frames_delete_all", {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.active_frames_delete_all", {"type": 'DEL', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_gpencil_edit_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_MT_gpencil_edit_context_menu'),], },),
            ("wm.call_menu",{"type": 'P', "value": 'PRESS', "repeat": True},{"properties": [("name", 'GPENCIL_MT_separate'),], },),
            ("gpencil.stroke_join", {"type": 'J', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("gpencil.stroke_join",{"type": 'J', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("type", 'JOINCOPY'),], },),
            ("gpencil.copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("gpencil.paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.call_menu_pie",{"type": 'X', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("name", 'GPENCIL_MT_snap_pie'),], },),
            ("gpencil.reveal", {"type": 'H', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("gpencil.hide",{"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("unselected", False),], },),
            ("gpencil.layer_isolate", {"type": 'NUMPAD_ASTERIX', "value": 'PRESS', "repeat": True}, None),
            ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_proportional_edit'),], },),
            ("wm.call_menu",{"type": 'G', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("name", 'GPENCIL_MT_gpencil_vertex_group'),], },),
            ("gpencil.selectmode_toggle",{"type": 'ONE', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("mode", 0),], },),
            ("gpencil.selectmode_toggle",{"type": 'TWO', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("mode", 1),], },),
            ("gpencil.selectmode_toggle",{"type": 'THREE', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("mode", 2),], },),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.select_box'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.move'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.rotate'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.scale'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.transform'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.annotate'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.measure'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.cursor'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("name", 'builtin.extrude'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("name", 'builtin.radius'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'B', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("name", 'builtin.bend'),("cycle", True),], },),],}, ),

("Grease Pencil Stroke Paint (Draw brush)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.draw",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("mode", 'DRAW'),("wait_for_input", False),], },),
            ("gpencil.draw",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("mode", 'DRAW'),("wait_for_input", False),], },),
            ("gpencil.draw",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties": [("mode", 'DRAW_STRAIGHT'),("wait_for_input", False),], },),
            ("gpencil.draw",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.draw", {"type": 'O', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.draw", {"type": 'J', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.draw", {"type": 'J', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("gpencil.draw", {"type": 'J', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.draw", {"type": 'K', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.draw", {"type": 'K', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("gpencil.draw", {"type": 'K', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.draw", {"type": 'L', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.draw", {"type": 'L', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("gpencil.draw", {"type": 'L', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("gpencil.draw", {"type": 'B', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.draw", {"type": 'P', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.draw", {"type": 'P', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("gpencil.draw",{"type": 'ERASER', "value": 'PRESS'},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Paint (Erase)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.draw",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.draw",{"type": 'ERASER', "value": 'PRESS'},{"properties": [("mode", 'ERASER'),("wait_for_input", False),], },),
            ("gpencil.select_box", {"type": 'B', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_R', "value": 'ANY', "ctrl": True, "alt": True}, None),],}, ),

("Grease Pencil Stroke Paint (Fill)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.fill",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("on_back", False),], },),
            ("gpencil.fill",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("on_back", True),], },),
            ("gpencil.draw",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'DRAW'),("wait_for_input", False),("disable_straight", True),], },),
            ("gpencil.draw",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties": [("mode", 'DRAW'),("wait_for_input", False),("disable_straight", True),("disable_fill", True),], },),
            ("gpencil.select_lasso", {"type": 'EVT_TWEAK_R', "value": 'ANY', "ctrl": True, "alt": True}, None),],},),

("Grease Pencil Stroke Paint (Tint)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Paint Mode",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("wm.radial_control",{"type": 'U', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_paint.brush.gpencil_settings.pen_strength'),], },),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_paint.brush.size'),], },),
            ("wm.call_panel",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_PT_gpencil_draw_context_menu'),], },),
            ("wm.call_panel",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_PT_gpencil_draw_context_menu'),], },),
            ("wm.call_menu",{"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True},{"properties": [("name", 'GPENCIL_MT_gpencil_draw_delete'),], },),
            ("wm.call_menu",{"type": 'DEL', "value": 'PRESS', "repeat": True},{"properties": [("name", 'GPENCIL_MT_gpencil_draw_delete'),], },),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin_brush.Draw'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'F', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin_brush.Fill'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin_brush.Erase'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'K', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.cutter'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.cursor'),("cycle", True),], },),
            ("wm.call_menu",{"type": 'Y', "value": 'PRESS', "repeat": True},{"properties": [("name", 'GPENCIL_MT_layer_active'),], },),
            ("wm.call_menu",{"type": 'I', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_MT_gpencil_animation'),], },),],},),

("Grease Pencil Stroke Sculpt (Clone)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt (Grab)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt (Pinch)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt (Push)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt (Randomize)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt (Smooth)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt (Strength)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt (Thickness)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt (Twist)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("gpencil.sculpt_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Sculpt Mode",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),("toggle", True),], },),
            ("gpencil.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("gpencil.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("gpencil.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("gpencil.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.select_alternate", {"type": 'L', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_sculpt_paint.brush.strength'),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_sculpt_paint.brush.size'),], },),
            ("gpencil.copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.context_toggle",{"type": 'Q', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path", 'space_data.overlay.use_gpencil_edit_lines'),], },),
            ("wm.context_toggle",{"type": 'Q', "value": 'PRESS', "shift": True, "alt": True, "repeat": True},{"properties": [("data_path", 'space_data.overlay.use_gpencil_multiedit_line_only'),], },),
            ("wm.call_panel",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_PT_gpencil_sculpt_context_menu'),], },),],},),

("Grease Pencil Stroke Vertex (Average)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.gpencil_settings.pen_strength'),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.size'),], },),],},),

("Grease Pencil Stroke Vertex (Blur)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.gpencil_settings.pen_strength'),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.size'),], },),],},),

("Grease Pencil Stroke Vertex (Draw)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.gpencil_settings.pen_strength'),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.size'),], },),],},),

("Grease Pencil Stroke Vertex (Replace)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.size'),], },),],},),

("Grease Pencil Stroke Vertex (Smear)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("wm.radial_control",{"type": 'U', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.gpencil_settings.pen_strength'),], },),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.size'),], },),],},),

("Grease Pencil Stroke Vertex Mode",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),("toggle", True),], },),
            ("gpencil.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("gpencil.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("gpencil.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("gpencil.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.select_alternate", {"type": 'L', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("gpencil.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("gpencil.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("wm.radial_control",{"type": 'U', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.gpencil_settings.pen_strength'),], },),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_vertex_paint.brush.size'),], },),
            ("wm.context_toggle",{"type": 'Q', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path", 'space_data.overlay.use_gpencil_edit_lines'),], },),
            ("wm.context_toggle",{"type": 'Q', "value": 'PRESS', "shift": True, "alt": True, "repeat": True},{"properties": [("data_path", 'space_data.overlay.use_gpencil_multiedit_line_only'),], },),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin_brush.Draw'),], },),
            ("wm.call_panel",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_PT_gpencil_vertex_context_menu'),], },),],},),

("Grease Pencil Stroke Weight (Draw)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("gpencil.weight_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),],},),

("Grease Pencil Stroke Weight Mode",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("wm.radial_control",{"type": 'U', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_weight_paint.brush.strength'),], },),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.gpencil_weight_paint.brush.size'),], },),
            ("wm.call_panel",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_PT_gpencil_weight_context_menu'),], },),
            ("wm.call_panel",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_PT_gpencil_weight_context_menu'),], },),],},),

################
# IMAGE EDITOR #
################
("Image",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("image.view_all", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("image.view_selected", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("image.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None),
            ("image.view_pan", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("image.view_pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
            ("image.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("image.view_ndof", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
            ("image.view_zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS'}, None),
            ("image.view_zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS'}, None),
            ("image.view_zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS', "alt": True}, None),
            ("image.view_zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("image.view_zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True}, None),
            ("image.view_zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True}, None),
            ("image.view_zoom", {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("image.view_zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
            ("image.view_zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
            ("image.view_zoom_border", {"type": 'Z', "value": 'PRESS', "repeat": True}, None),
            ("image.view_zoom_ratio",{"type": 'F4', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("ratio", 8.0),], },),
            ("image.view_zoom_ratio",{"type": 'F3', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("ratio", 4.0),], },),
            ("image.view_zoom_ratio",{"type": 'F2', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("ratio", 2.0),], },),
            ("image.view_zoom_ratio",{"type": 'F4', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("ratio", 8.0),], },),
            ("image.view_zoom_ratio",{"type": 'F3', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("ratio", 4.0),], },),
            ("image.view_zoom_ratio",{"type": 'F2', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("ratio", 2.0),], },),
            ("image.view_zoom_ratio",{"type": 'F1', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 1.0),], },),
            ("image.view_zoom_ratio",{"type": 'F2', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 0.5),], },),
            ("image.view_zoom_ratio",{"type": 'F3', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 0.25),], },),
            ("image.view_zoom_ratio",{"type": 'F4', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 0.125),], },),
            ("image.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("image.sample", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("image.curves_point_set",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("point", 'BLACK_POINT'),], },),
            ("image.curves_point_set",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("point", 'WHITE_POINT'),], },),
            ("wm.call_menu_pie",{"type": 'PERIOD', "value": 'PRESS', "repeat": True},{"properties": [("name", 'IMAGE_MT_pivot_pie'),], },),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.select_box'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.transform'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.transform'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.transform'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.cursor'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.annotate'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'I', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.sample'),("cycle", True),], },),],},),

("Image Editor Tool: Sample",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("image.sample", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("image.sample", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),],},),

("Image Editor Tool: Uv, Cursor",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("uv.cursor_set", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("transform.translate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("cursor_transform", True),("release_confirm", True),], },),
            ("uv.cursor_set", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("transform.translate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("cursor_transform", True),("release_confirm", True),], },),],},),

("Image Editor Tool: Uv, Move",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("transform.translate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },),
            ("transform.translate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },),],},),

("Image Editor Tool: Uv, Rip Region",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("uv.rip_move",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },),
            ("uv.rip_move",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("TRANSFORM_OT_translate", [("release_confirm", True),  ], ),], },),],},),

("Image Editor Tool: Uv, Rotate",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("transform.rotate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },),
            ("transform.rotate",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },),],},),

("Image Editor Tool: Uv, Scale",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("transform.resize",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },),
            ("transform.resize",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("release_confirm", True),], },),],},),

("Image Editor Tool: Uv, Sculpt Stroke",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.uv_sculpt_stroke", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("sculpt.uv_sculpt_stroke",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'INVERT'),], },),
            ("sculpt.uv_sculpt_stroke",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("mode", 'RELAX'),], },),
            ("brush.scale_size",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("scalar", 0.9),], },),
            ("brush.scale_size",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("scalar", 1.1111112),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.uv_sculpt.brush.size'),("data_path_secondary", 'tool_settings.unified_paint_settings.size'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),("rotation_path", 'tool_settings.uv_sculpt.brush.texture_slot.angle'),("color_path", 'tool_settings.uv_sculpt.brush.cursor_color_add'),("fill_color_path", ''),("fill_color_override_path", ''),("fill_color_override_test_path", ''),("zoom_path", ''),("image_id", 'tool_settings.uv_sculpt.brush'),("secondary_tex", False),], },),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path_primary", 'tool_settings.uv_sculpt.brush.strength'),("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),("rotation_path", 'tool_settings.uv_sculpt.brush.texture_slot.angle'),("color_path", 'tool_settings.uv_sculpt.brush.cursor_color_add'),("fill_color_path", ''),("fill_color_override_path", ''),("fill_color_override_test_path", ''),("zoom_path", ''),("image_id", 'tool_settings.uv_sculpt.brush'),("secondary_tex", False),], },),
            ("sculpt.uv_sculpt_stroke", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("sculpt.uv_sculpt_stroke",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'INVERT'),], },),
            ("sculpt.uv_sculpt_stroke",{"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True},{"properties": [("mode", 'RELAX'),], },),],},),

("Image Editor Tool: Uv, Select Box",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("uv.select_box", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("uv.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),], },),
            ("uv.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },),],},),

("Image Editor Tool: Uv, Select Circle",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("uv.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("uv.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),("mode", 'ADD'),], },),
            ("uv.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),("mode", 'SUB'),], },),],},),

("Image Editor Tool: Uv, Select Lasso",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("uv.select_lasso", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("uv.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),], },),
            ("uv.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),], },),],},),

("Image Editor Tool: Uv, Tweak",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("uv.select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("deselect_all", True),], },),
            ("uv.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),],},),

("Image Generic",
    {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("image.new", {"type": 'N', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("image.open", {"type": 'O', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("image.reload", {"type": 'R', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("image.read_viewlayers", {"type": 'R', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("image.save", {"type": 'S', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("image.save_as", {"type": 'S', "value": 'PRESS', "shift": True, "alt": True, "repeat": True}, None),],},),

("Image Paint",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("paint.image_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties":[("mode", 'NORMAL'),],},),
            ("paint.image_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties":[("mode", 'INVERT'),],},),
            ("paint.sample_color", {"type": 'I', "value": 'PRESS'}, None),
            ("paint.brush_colors_flip", {"type": 'X', "value": 'PRESS'}, None),
            ("paint.grab_clone", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("brush.scale_size",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties":[("scalar", 0.9),],},),
            ("brush.scale_size",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties":[("scalar", 1.1111112),],},),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS'},{"properties":[("data_path_primary", 'tool_settings.image_paint.brush.size'),("data_path_secondary", 'tool_settings.unified_paint_settings.size'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),("fill_color_path", 'tool_settings.image_paint.brush.color'),("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),("zoom_path", 'space_data.zoom'),("image_id", 'tool_settings.image_paint.brush'),("secondary_tex", True),],},),
            ("wm.radial_control",{"type": 'U', "value": 'PRESS'},{"properties":[("data_path_primary", 'tool_settings.image_paint.brush.strength'),("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),("fill_color_path", 'tool_settings.image_paint.brush.color'),("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),("zoom_path", ''),("image_id", 'tool_settings.image_paint.brush'),("secondary_tex", True),],},),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "ctrl": True},{"properties":[("data_path_primary", 'tool_settings.image_paint.brush.texture_slot.angle'),("data_path_secondary", ''),("use_secondary", ''),("rotation_path", 'tool_settings.image_paint.brush.texture_slot.angle'),("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),("fill_color_path", 'tool_settings.image_paint.brush.color'),("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),("zoom_path", ''),("image_id", 'tool_settings.image_paint.brush'),("secondary_tex", False),],},),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "ctrl": True, "alt": True},{"properties":[("data_path_primary", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),("data_path_secondary", ''),("use_secondary", ''),("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),("fill_color_path", 'tool_settings.image_paint.brush.color'),("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),("zoom_path", ''),("image_id", 'tool_settings.image_paint.brush'),("secondary_tex", True),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties":[("mode", 'TRANSLATION'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},{"properties":[("mode", 'SCALE'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},{"properties":[("mode", 'ROTATION'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},{"properties":[("mode", 'TRANSLATION'),("texmode", 'SECONDARY'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties":[("mode", 'SCALE'),("texmode", 'SECONDARY'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},{"properties":[("mode", 'ROTATION'), ("texmode", 'SECONDARY'), ],},),
            ("wm.context_toggle",{"type": 'M', "value": 'PRESS'},{"properties":[("data_path", 'image_paint_object.data.use_paint_mask'), ],},),
            ("wm.context_toggle",{"type": 'S', "value": 'PRESS', "shift": True},{"properties":[("data_path", 'tool_settings.image_paint.brush.use_smooth_stroke'), ],},),
            ("wm.call_menu",{"type": 'R', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_angle_control'), ],},),
            ("wm.call_panel",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_PT_paint_texture_context_menu'), ],},),
            ("wm.call_panel",{"type": 'APP', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_PT_paint_texture_context_menu'), ],},),
            ("paint.brush_select",{"type": 'D', "value": 'PRESS'},{"properties":[("image_tool", 'DRAW'), ],},),
            ("paint.brush_select",{"type": 'B', "value": 'PRESS'},{"properties":[("image_tool", 'SOFTEN'), ],},),
            ("paint.brush_select",{"type": 'G', "value": 'PRESS'},{"properties":[("image_tool", 'FILL'), ],},),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties":[("name", 'builtin.select_box'), ("cycle", True), ],},),],},),

########
# INFO #
########
("Info",
    {"space_type": 'INFO', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("info.select_pick", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("info.select_pick",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("info.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("wait_for_input", False),], },),
            ("info.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("info.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("info.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("info.select_box", {"type": 'Q', "value": 'PRESS', "repeat": True}, None),
            ("info.report_replay", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("info.report_delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("info.report_delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("info.report_copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'INFO_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'INFO_MT_context_menu'),], },),],},),

###############
# KNIFE MODAL #
###############
("Knife Tool Modal Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("PANNING", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("ADD_CUT_CLOSED", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "any": True}, None),
            ("ADD_CUT", {"type": 'LEFTMOUSE', "value": 'ANY', "any": True}, None),
            ("NEW_CUT", {"type": 'E', "value": 'PRESS', "repeat": True}, None),
            ("SNAP_MIDPOINTS_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "repeat": True}, None),
            ("SNAP_MIDPOINTS_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE'}, None),
            ("SNAP_MIDPOINTS_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "repeat": True}, None),
            ("SNAP_MIDPOINTS_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE'}, None),
            ("IGNORE_SNAP_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("IGNORE_SNAP_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("IGNORE_SNAP_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("IGNORE_SNAP_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("ANGLE_SNAP_TOGGLE", {"type": 'C', "value": 'PRESS', "repeat": True}, None),
            ("CUT_THROUGH_TOGGLE", {"type": 'X', "value": 'PRESS', "repeat": True}, None),
            ("PANNING", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None),
            ("PANNING", {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("CONFIRM", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),],},),

###########
# LATTICE #
###########
("Lattice",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("lattice.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'SELECT'), ],},),
            ("lattice.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},{"properties":[("action", 'DESELECT'), ],},),
            ("lattice.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'INVERT'), ],},),
            ("lattice.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("lattice.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("object.vertex_parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_lattice_context_menu'), ],},),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_lattice_context_menu'), ],},),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS'},{"properties":[("data_path", 'tool_settings.use_proportional_edit'), ],},),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties":[("name", 'builtin.select_box'), ("cycle", True), ],},),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS'},{"properties":[("name", 'builtin.move'), ("cycle", True), ],},),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS'},{"properties":[("name", 'builtin.rotate'), ("cycle", True), ],},),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS'},{"properties":[("name", 'builtin.scale'), ("cycle", True), ],},),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS'},{"properties":[("name", 'builtin.transform'), ("cycle", True), ],},),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS'},{"properties":[("name", 'builtin.measure'), ("cycle", True), ],},),],},),

###########
# MARKERS #
###########
("Markers",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("marker.add", {"type": 'M', "value": 'PRESS', "repeat": True}, None),
            ("marker.move", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("marker.duplicate", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("marker.select", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("marker.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("marker.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("extend", False),("camera", True),], },),
            ("marker.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("extend", True),("camera", True),], },),
            ("marker.select_box", {"type": 'Q', "value": 'PRESS', "repeat": True}, None),
            ("marker.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("marker.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("marker.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("marker.delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("marker.delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("marker.rename", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),
            ("marker.move", {"type": 'W', "value": 'PRESS', "repeat": True}, None),],},),

################
# MASK EDITING #
################
("Mask Editing",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("mask.new", {"type": 'N', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_proportional_edit_mask'),], },),
            ("mask.add_vertex_slide", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
            ("mask.add_feather_vertex_slide", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
            ("mask.delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("mask.delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("mask.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", False),("deselect", False),("toggle", True),], },),
            ("mask.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("mask.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("mask.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("mask.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("mask.select_linked_pick",{"type": 'L', "value": 'PRESS', "repeat": True},{"properties": [("deselect", False),], },),
            ("mask.select_linked_pick",{"type": 'L', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("deselect", True),], },),
            ("mask.select_box", {"type": 'Q', "value": 'PRESS', "repeat": True}, None),
            ("mask.select_circle", {"type": 'C', "value": 'PRESS', "repeat": True}, None),
            ("mask.select_lasso",{"type": 'EVT_TWEAK_R', "value": 'ANY', "ctrl": True, "alt": True},{"properties": [("mode", 'ADD'),], },),
            ("mask.select_lasso",{"type": 'EVT_TWEAK_R', "value": 'ANY', "shift": True, "ctrl": True, "alt": True},{"properties": [("mode", 'SUB'),], },),
            ("mask.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("mask.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("mask.hide_view_clear", {"type": 'H', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("mask.hide_view_set",{"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("unselected", False),], },),
            ("mask.hide_view_set",{"type": 'H', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("unselected", True),], },),
            ("clip.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("extend", False),], },),
            ("mask.cyclic_toggle", {"type": 'C', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("mask.slide_point", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("mask.slide_spline_curvature", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("mask.handle_type_set", {"type": 'V', "value": 'PRESS', "repeat": True}, None),
            ("mask.parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("mask.parent_clear", {"type": 'P', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("mask.shape_key_insert", {"type": 'I', "value": 'PRESS', "repeat": True}, None),
            ("mask.shape_key_clear", {"type": 'I', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("mask.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("mask.copy_splines", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("mask.paste_splines", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("transform.translate", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("transform.resize", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("transform.rotate", {"type": 'E', "value": 'PRESS', "repeat": True}, None),],},),

########
# MESH #
########
("Mesh",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("mesh.loop_select",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'},{"properties": [("extend", False),  ("deselect", False),  ("toggle", False),  ("ring", False),  ], },),
            ("mesh.loop_select",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "shift": True},{"properties": [("extend", True),  ("deselect", False),  ("toggle", False),  ("ring", False),  ], },),
            ("mesh.loop_select",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "ctrl": True},{"properties": [("extend", False),  ("deselect", True),  ("toggle", False),  ("ring", False),  ], },),
            ("mesh.loop_select",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "alt": True},{"properties": [("extend", False),  ("deselect", False),  ("toggle", False),  ("ring", True),  ], },),
            ("mesh.loop_select",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "shift": True, "alt": True},{"properties": [("extend", True),  ("deselect", False),  ("toggle", False),  ("ring", True),  ], },),
            ("mesh.loop_select",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "ctrl": True, "alt": True},{"properties": [("extend", False),  ("deselect", True),  ("toggle", False),  ("ring", True),  ], },),
            ("mesh.shortest_path_pick",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("use_fill", False),  ], },),
            ("mesh.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True},{"properties": [("action", 'SELECT'),  ], },),
            ("mesh.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("action", 'DESELECT'),  ], },),
            ("mesh.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties": [("action", 'INVERT'),  ], },),
            ("mesh.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("mesh.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("mesh.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS'}, None),
            ("mesh.select_mode",{"type": 'ONE', "value": 'PRESS'},{"properties": [("type", 'VERT'),  ], },),
            ("mesh.select_mode",{"type": 'TWO', "value": 'PRESS'},{"properties": [("type", 'EDGE'),  ], },),
            ("mesh.select_mode",{"type": 'THREE', "value": 'PRESS'},{"properties": [("type", 'FACE'),  ], },),
            ("mesh.select_mode",{"type": 'ONE', "value": 'PRESS', "shift": True},{"properties": [("use_extend", True),  ("type", 'VERT'),  ], },),
            ("mesh.select_mode",{"type": 'TWO', "value": 'PRESS', "shift": True},{"properties": [("use_extend", True),  ("type", 'EDGE'),  ], },),
            ("mesh.select_mode",{"type": 'THREE', "value": 'PRESS', "shift": True},{"properties": [("use_extend", True),  ("type", 'FACE'),  ], },),
            ("mesh.select_mode",{"type": 'ONE', "value": 'PRESS', "ctrl": True},{"properties": [("use_expand", True),  ("type", 'VERT'),  ], },),
            ("mesh.select_mode",{"type": 'TWO', "value": 'PRESS', "ctrl": True},{"properties": [("use_expand", True),  ("type", 'EDGE'),  ], },),
            ("mesh.select_mode",{"type": 'THREE', "value": 'PRESS', "ctrl": True},{"properties": [("use_expand", True),  ("type", 'FACE'),  ], },),
            ("mesh.select_mode",{"type": 'ONE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("use_extend", True),  ("use_expand", True),  ("type", 'VERT'),  ], },),
            ("mesh.select_mode",{"type": 'TWO', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("use_extend", True),  ("use_expand", True),  ("type", 'EDGE'),  ], },),
            ("mesh.select_mode",{"type": 'THREE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("use_extend", True),  ("use_expand", True),  ("type", 'FACE'),  ], },),
            ("mesh.hide",{"type": 'H', "value": 'PRESS', "ctrl": True},{"properties": [("unselected", False),  ], },),
            ("mesh.hide",{"type": 'H', "value": 'PRESS', "shift": True},{"properties": [("unselected", True),  ], },),
            ("mesh.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
            ("mesh.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("wm.call_menu",{"type": 'BACK_SPACE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_edit_mesh_delete'),  ], },),
            ("wm.call_menu",{"type": 'DEL', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_edit_mesh_delete'),  ], },),
            ("mesh.dissolve_mode", {"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True}, None),
            ("mesh.dissolve_mode", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS'},{"properties": [("data_path", 'tool_settings.use_proportional_edit'),  ], },),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_edit_mesh_context_menu'),  ], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_edit_mesh_context_menu'),  ], },),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties": [("name", 'builtin.select_box'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS'},{"properties": [("name", 'builtin.move'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS'},{"properties": [("name", 'builtin.rotate'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS'},{"properties": [("name", 'builtin.scale'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS'},{"properties": [("name", 'builtin.transform'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS'},{"properties": [("name", 'builtin.annotate'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS'},{"properties": [("name", 'builtin.measure'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS'},{"properties":[("name", 'builtin.cursor'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'B', "value": 'PRESS', "ctrl": True},{"properties":[("name", 'builtin.bevel'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'I', "value": 'PRESS'},{"properties":[("name", 'builtin.inset_faces'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS', "ctrl": True},{"properties":[("name", 'builtin.extrude_region'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'K', "value": 'PRESS'},{"properties":[("name", 'builtin.knife'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS', "alt": True},{"properties":[("name", 'builtin.loop_cut'),("cycle", True),],},),],},),

############
# METABALL #
############
("Metaball",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("mball.reveal_metaelems", {"type": 'H', "value": 'PRESS', "alt": True}, None),
            ("mball.hide_metaelems",{"type": 'H', "value": 'PRESS', "ctrl": True},{"properties":[("unselected", False),],},),
            ("mball.hide_metaelems",{"type": 'H', "value": 'PRESS', "shift": True},{"properties":[("unselected", True),],},),
            ("mball.delete_metaelems", {"type": 'BACK_SPACE', "value": 'PRESS'}, None),
            ("mball.delete_metaelems", {"type": 'DEL', "value": 'PRESS'}, None),
            ("mball.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("mball.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'SELECT'),],},),
            ("mball.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},{"properties":[("action", 'DESELECT'),],},),
            ("mball.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'INVERT'),],},),
            ("mball.select_similar", {"type": 'G', "value": 'PRESS', "shift": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_metaball_context_menu'),],},),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_MT_edit_metaball_context_menu'),],},),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS'},{"properties":[("data_path", 'tool_settings.use_proportional_edit'),],},),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties":[("name", 'builtin.select_box'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS'},{"properties":[("name", 'builtin.move'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS'},{"properties":[("name", 'builtin.rotate'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS'},{"properties":[("name", 'builtin.scale'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS'},{"properties":[("name", 'builtin.transform'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS'},{"properties":[("name", 'builtin.annotate'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS'},{"properties":[("name", 'builtin.measure'),("cycle", True),],},),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS'},{"properties":[("name", 'builtin.cursor'),("cycle", True),],},),],},),

##############
# NLA EDITOR #
##############
("NLA Channels",
    {"space_type": 'NLA_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("nla.channels_click",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),], },),
            ("nla.channels_click",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("nla.tracks_delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("nla.tracks_delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'NLA_MT_channel_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'NLA_MT_channel_context_menu'),], },),],},),

("NLA Editor",
    {"space_type": 'NLA_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("nla.click_select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),("deselect_all", True),], },),
            ("nla.click_select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("nla.select_leftright",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("mode", 'CHECK'),("extend", True),], },),
            ("nla.select_leftright",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'LEFT'),("extend", False),], },),
            ("nla.select_leftright",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'RIGHT'),("extend", False),], },),
            ("nla.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("nla.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("nla.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("nla.select_box",{"type": 'Q', "value": 'PRESS', "repeat": True},{"properties": [("axis_range", False),], },),
            ("nla.select_box",{"type": 'Q', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("axis_range", True),], },),
            ("nla.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("tweak", True),("mode", 'SET'),], },),
            ("nla.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("tweak", True),("mode", 'ADD'),], },),
            ("nla.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("tweak", True),("mode", 'SUB'),], },),
            ("nla.view_all", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("nla.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("nla.view_selected", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("nla.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS', "repeat": True}, None),
            ("nla.meta_add", {"type": 'G', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("nla.meta_remove", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True}, None),
            ("nla.duplicate",{"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("linked", False),], },),
            ("nla.duplicate",{"type": 'D', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True},{"properties": [("linked", True),], },),
            ("nla.make_single_user", {"type": 'U', "value": 'PRESS', "repeat": True}, None),
            ("nla.delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("nla.delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("nla.mute_toggle", {"type": 'M', "value": 'PRESS', "repeat": True}, None),
            ("nla.move_up", {"type": 'PAGE_UP', "value": 'PRESS', "repeat": True}, None),
            ("nla.move_down", {"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True}, None),
            ("transform.transform",{"type": 'W', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TRANSLATION'),], },),
            ("transform.transform",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'TRANSLATION'),], },),
            ("transform.transform",{"type": 'EVT_TWEAK_M', "value": 'ANY'},{"properties": [("mode", 'TRANSLATION'),], },),
            ("transform.transform",{"type": 'E', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TIME_EXTEND'),], },),
            ("transform.transform",{"type": 'R', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TIME_SCALE'),], },),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'NLA_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'NLA_MT_context_menu'),], },),
            ("wm.call_menu_pie",{"type": 'X', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("name", 'NLA_MT_snap_pie'),], },),
            ("marker.add", {"type": 'M', "value": 'PRESS', "repeat": True}, None),
            ("marker.rename", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),],},),

("NLA Generic",
    {"space_type": 'NLA_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("screen.frame_offset",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("delta", -1),], },),
            ("screen.frame_offset",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("delta", 1),], },),
            ("screen.frame_jump",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("end", True),], },),
            ("screen.frame_jump",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("end", False),], },),
            ("nla.tweakmode_enter", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
            ("nla.tweakmode_exit", {"type": 'ESC', "value": 'PRESS', "repeat": True}, None),
            ("anim.channels_find", {"type": 'F', "value": 'PRESS', "ctrl": True, "repeat": True}, None),],},),

###############
# NODE EDITOR #
###############
("Node Editor",
    {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("node.select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),("deselect_all", True),], },),
            ("node.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("extend", False),], },),
            ("node.links_cut", {"type": 'EVT_TWEAK_L', "value": 'ANY', "alt": True}, None),
            ("node.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},{"properties": [("extend", False),], },),
            ("node.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("node.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("extend", True),], },),
            ("node.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties": [("extend", True),], },),
            ("node.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},{"properties": [("extend", True),], },),
            ("node.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("tweak", True),], },),
            ("node.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True, "alt": True},{"properties": [("mode", 'ADD'),], },),
            ("node.select_lasso",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True, "ctrl": True, "alt": True},{"properties": [("mode", 'SUB'),], },),
            ("node.link",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("detach", False),], },),
            ("node.link",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("detach", True),], },),
            ("node.resize", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("node.add_node",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'},{"properties": [("type", 'NodeReroute'),("use_transform", True),], },),
            ("node.links_cut", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("node.select_link_viewer", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
            ("node.backimage_fit", {"type": 'A', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("node.backimage_sample", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'CLICK', "ctrl": True},{"properties": [("name", 'NODE_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'NODE_MT_context_menu'),], },),
            ("node.link_make",{"type": 'L', "value": 'PRESS', "repeat": True},{"properties": [("replace", False),], },),
            ("node.link_make",{"type": 'L', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("replace", True),], },),
            ("node.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.parent_set", {"type": 'P', "value": 'PRESS', "repeat": True}, None),
            ("blui.comment_box", {"type": 'C', "value": 'ANY'}, None),
            ("node.hide_toggle", {"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.mute_toggle", {"type": 'M', "value": 'PRESS', "repeat": True}, None),
            ("node.preview_toggle", {"type": 'H', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("node.hide_socket_toggle", {"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.view_all", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("node.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("node.view_selected", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("node.select_box",{"type": 'Q', "value": 'PRESS', "repeat": True},{"properties": [("tweak", False),], },),
            ("node.delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("node.delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("node.delete_reconnect", {"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.delete_reconnect", {"type": 'DEL', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("node.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("node.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("node.select_linked_to", {"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("node.select_linked_from", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True}, None),
            ("node.select_same_type_step",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("prev", False),], },),
            ("node.select_same_type_step",{"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("prev", True),], },),
            ("node.find_node", {"type": 'F', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.group_make", {"type": 'G', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.group_ungroup", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True}, None),
            ("node.group_edit",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'},{"properties": [("exit", False),], },),
            ("node.group_edit",{"type": 'ESC', "value": 'PRESS', "repeat": True},{"properties": [("exit", True),], },),
            ("node.clipboard_copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.clipboard_paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("node.viewer_border", {"type": 'Z', "value": 'PRESS', "repeat": True}, None),
            ("node.clear_viewer_border", {"type": 'Z', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("node.translate_attach", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("node.translate_attach", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("node.translate_attach", {"type": 'EVT_TWEAK_M', "value": 'ANY'}, None),
            ("transform.translate", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("transform.translate",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("release_confirm", True),], },),
            ("transform.rotate", {"type": 'E', "value": 'PRESS', "repeat": True}, None),
            ("transform.resize", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("node.move_detach_links_release", {"type": 'EVT_TWEAK_R', "value": 'ANY', "alt": True}, None),
            ("node.move_detach_links", {"type": 'EVT_TWEAK_L', "value": 'ANY', "alt": True}, None),
            ("wm.context_toggle",{"type": 'X', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_snap'),], },),
            ("node.add_search",{"type": 'RIGHTMOUSE', "value": 'RELEASE'},{"properties": [("use_transform", True),], },),
            ("node.add_node",{"type": 'LEFTMOUSE', "value": 'ANY', "key_modifier": 'S'},{"properties": [("type", 'ShaderNodeValue'),("use_transform", False),], },),
            ("node.add_node",{"type": 'LEFTMOUSE', "value": 'ANY', "key_modifier": 'M'},{"properties": [("type", 'ShaderNodeMath'),], },),
            ("node.add_node",{"type": 'LEFTMOUSE', "value": 'ANY', "key_modifier": 'U'},{"properties": [("type", 'ShaderNodeTexCoord'),], },),
            ("node.add_node",{"type": 'LEFTMOUSE', "value": 'ANY', "key_modifier": 'T'},{"properties": [("type", 'ShaderNodeTexImage'),("use_transform", True),], },),
            ("node.add_node",{"type": 'LEFTMOUSE', "value": 'ANY', "key_modifier": 'B'},{"properties": [("type", 'ShaderNodeBump'),], },),],},),

("Node Generic",
    {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("node.add_search",{"type": 'TAB', "value": 'PRESS', "repeat": True},{    "active":False, },),],},),

("Node Tool: Links Cut",
    {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("node.links_cut", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("node.links_cut", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),],},),

("Node Tool: Select Box",
    {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("node.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("tweak", True),], },),
            ("node.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("tweak", True),("mode", 'ADD'),], },),
            ("node.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("tweak", True),("mode", 'SUB'),], },),],},),

("Node Tool: Select Circle",
    {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("node.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("wait_for_input", False),], },),
            ("node.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("wait_for_input", False),("mode", 'ADD'),], },),
            ("node.select_circle",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("wait_for_input", False),("mode", 'SUB'),], },),],},),

("Node Tool: Select Lasso",
    {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("node.select_lasso",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("tweak", True),], },),
            ("node.select_lasso",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("tweak", True),("mode", 'ADD'),], },),
            ("node.select_lasso",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("tweak", True),("mode", 'SUB'),], },),],},),

("Node Tool: Tweak",
    {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("node.select",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),("deselect_all", True),], },),],},),

###############
# OBJECT MODE #
###############
("Object Mode",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("screen.frame_offset",{"type": 'LEFT_ARROW', "value": 'PRESS'},{"properties":[("delta", -1),],},),
            ("screen.frame_offset",{"type": 'RIGHT_ARROW', "value": 'PRESS'},{"properties":[("delta", 1),],},),
            ("screen.frame_jump",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True},{"properties":[("end", True),],},),
            ("screen.frame_jump",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True},{"properties":[("end", False),],},),
            ("object.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'SELECT'),],},),
            ("object.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},{"properties":[("action", 'DESELECT'),],},),
            ("object.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'INVERT'),],},),
            ("object.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("object.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("object.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS'}, None),
            ("object.select_hierarchy",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties":[("direction", 'PARENT'),("extend", False),],},),
            ("object.select_hierarchy",{"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True},{"properties":[("direction", 'PARENT'),("extend", True),],},),
            ("object.select_hierarchy",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties":[("direction", 'CHILD'),("extend", False),],},),
            ("object.select_hierarchy",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True},{"properties":[("direction", 'CHILD'),("extend", True),],},),
            ("object.parent_set", {"type": 'P', "value": 'PRESS'}, None),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS'},{"properties":[("data_path", 'tool_settings.use_proportional_edit_objects'),],},),
            ("object.parent_clear", {"type": 'P', "value": 'PRESS', "shift": True}, None),
            ("object.location_clear",{"type": 'W', "value": 'PRESS', "alt": True},{"properties":[("clear_delta", False),],},),
            ("object.rotation_clear",{"type": 'E', "value": 'PRESS', "alt": True},{"properties":[("clear_delta", False),],},),
            ("object.scale_clear",{"type": 'R', "value": 'PRESS', "alt": True},{"properties":[("clear_delta", False),],},),
            ("object.delete",{"type": 'BACK_SPACE', "value": 'PRESS'},{"properties":[("use_global", False),("confirm", False),],},),
            ("object.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "shift": True},{"properties":[("use_global", True),("confirm", False),], },),
            ("object.delete",{"type": 'DEL', "value": 'PRESS'},{"properties": [("use_global", False),("confirm", False),], },),
            ("object.delete",{"type": 'DEL', "value": 'PRESS', "shift": True},{"properties": [("use_global", True),("confirm", False),], },),
            ("object.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("anim.keyframe_insert_menu", {"type": 'S', "value": 'PRESS', "shift": True}, None),
            ("anim.keyframe_insert_by_name",{"type": 'S', "value": 'PRESS'},{"properties": [("type", 'LocRotScale'),], },),
            ("anim.keyframe_insert_by_name",{"type": 'W', "value": 'PRESS', "shift": True},{"properties": [("type", 'Location'),], },),
            ("anim.keyframe_insert_by_name",{"type": 'E', "value": 'PRESS', "shift": True},{"properties": [("type", 'Rotation'),], },),
            ("anim.keyframe_insert_by_name",{"type": 'R', "value": 'PRESS', "shift": True},{"properties": [("type", 'Scaling'),], },),
            ("anim.keyframe_delete_v3d", {"type": 'S', "value": 'PRESS', "alt": True}, None),
            ("anim.keying_set_active_set", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_object_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_object_context_menu'),], },),
            ("object.move_to_collection", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
            ("object.link_to_collection", {"type": 'G', "value": 'PRESS', "shift": True, "ctrl": True}, None),
            ("object.hide_view_clear", {"type": 'H', "value": 'PRESS', "alt": True}, None),
            ("object.hide_view_set",{"type": 'H', "value": 'PRESS', "ctrl": True},{"properties": [("unselected", False),], },),
            ("object.hide_view_set",{"type": 'H', "value": 'PRESS', "shift": True},{"properties": [("unselected", True),], },),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties": [("name", 'builtin.select_box'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS'},{"properties": [("name", 'builtin.move'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS'},{"properties": [("name", 'builtin.rotate'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS'},{"properties": [("name", 'builtin.scale'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS'},{"properties": [("name", 'builtin.transform'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS'},{"properties": [("name", 'builtin.annotate'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS'},{"properties": [("name", 'builtin.measure'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS'},{"properties": [("name", 'builtin.cursor'),  ("cycle", True),  ], },),],},),

("Object Non-modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("object.mode_set",{"type": 'ONE', "value": 'PRESS', "repeat": True},{    "active":False, },),
            ("object.mode_set",{"type": 'THREE', "value": 'PRESS', "repeat": True},{    "active":False, },),
            ("object.mode_set_with_submode",{"type": 'ONE', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'EDIT'),("mesh_select_mode", {'VERT'}),], },),
            ("object.mode_set_with_submode",{"type": 'TWO', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'EDIT'),("mesh_select_mode", {'EDGE'}),], },),
            ("object.mode_set_with_submode",{"type": 'THREE', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'EDIT'),("mesh_select_mode", {'FACE'}),], },),
            ("object.mode_set",{"type": 'ONE', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'EDIT'),], },),
            ("object.mode_set",{"type": 'FOUR', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'OBJECT'),], },),
            ("object.mode_set",{"type": 'FIVE', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'SCULPT'),], },),
            ("object.mode_set",{"type": 'SIX', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'VERTEX_PAINT'),], },),
            ("object.mode_set",{"type": 'SEVEN', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'WEIGHT_PAINT'),], },),
            ("object.mode_set",{"type": 'EIGHT', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TEXTURE_PAINT'),], },),
            ("object.mode_set", {"type": 'TWO', "value": 'PRESS', "repeat": True}, None),
            ("object.mode_set", {"type": 'FIVE', "value": 'PRESS', "repeat": True}, None),
            ("object.mode_set", {"type": 'SIX', "value": 'PRESS', "repeat": True}, None),
            ("object.mode_set", {"type": 'SEVEN', "value": 'PRESS', "repeat": True}, None),],},),

############
# OUTLINER #
############
("Outliner",
    {"space_type": 'OUTLINER', "region_type": 'WINDOW'},
        {"items":
            [("outliner.item_rename", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
            ("outliner.item_rename", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("outliner.highlight_update", {"type": 'MOUSEMOVE', "value": 'ANY', "any": True}, None),
            ("outliner.item_activate",{"type": 'LEFTMOUSE', "value": 'CLICK'},{"properties": [("extend", False),("deselect_all", True),], },),
            ("outliner.item_activate",{"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},{"properties": [("extend", True),("deselect_all", True),], },),
            ("outliner.item_activate",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},{"properties": [("extend", False),("extend_range", True),("deselect_all", True),], },),
            ("outliner.item_activate",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},{"properties": [("extend", True),("extend_range", True),("deselect_all", True),], },),
            ("outliner.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("tweak", True),], },),
            ("outliner.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("tweak", True),("mode", 'ADD'),], },),
            ("outliner.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("tweak", True),("mode", 'SUB'),], },),
            ("outliner.select_walk",{"type": 'UP_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'UP'),], },),
            ("outliner.select_walk",{"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'UP'),("extend", True),],},),
            ("outliner.select_walk",{"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'DOWN'),], },),
            ("outliner.select_walk",{"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'DOWN'),("extend", True),], },),
            ("outliner.select_walk",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'LEFT'),], },),
            ("outliner.select_walk",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'LEFT'),("toggle_all", True),], },),
            ("outliner.select_walk",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'RIGHT'),], },),
            ("outliner.select_walk",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'RIGHT'),("toggle_all", True),], },),
            ("outliner.item_openclose",{"type": 'LEFTMOUSE', "value": 'CLICK'},{"properties": [("all", False),], },),
            ("outliner.item_openclose",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},{"properties": [("all", True),], },),
            ("outliner.item_openclose",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("all", False),], },),
            ("outliner.operation", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'OUTLINER_MT_context_menu'),], },),
            ("outliner.item_drag_drop", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("outliner.item_drag_drop", {"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True}, None),
            ("outliner.show_hierarchy", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("outliner.show_active", {"type": 'PERIOD', "value": 'PRESS', "repeat": True}, None),
            ("outliner.show_active", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("outliner.scroll_page",{"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True},{"properties": [("up", False),], },),
            ("outliner.scroll_page",{"type": 'PAGE_UP', "value": 'PRESS', "repeat": True},{"properties": [("up", True),], },),
            ("outliner.show_one_level", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True}, None),
            ("outliner.show_one_level",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True},{"properties": [("open", False),], },),
            ("outliner.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("outliner.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("outliner.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("outliner.keyingset_add_selected", {"type": 'K', "value": 'PRESS', "repeat": True}, None),
            ("outliner.keyingset_remove_selected", {"type": 'K', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("anim.keyframe_insert", {"type": 'S', "value": 'PRESS', "repeat": True}, None),
            ("anim.keyframe_delete", {"type": 'S', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("outliner.drivers_add_selected", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("outliner.drivers_delete_selected", {"type": 'D', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True}, None),
            ("outliner.delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("outliner.delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("object.move_to_collection", {"type": 'G', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("object.link_to_collection", {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
            ("outliner.collection_exclude_set", {"type": 'E', "value": 'PRESS', "repeat": True}, None),
            ("outliner.collection_exclude_clear", {"type": 'E', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("outliner.hide", {"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("outliner.unhide_all", {"type": 'H', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("outliner.id_copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("outliner.id_paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),],},),

#########
# PAINT #
#########
("Paint Curve",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("paintcurve.add_point_slide", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
            ("paintcurve.select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),], },),
            ("paintcurve.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("paintcurve.slide",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("align", False),], },),
            ("paintcurve.slide",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("align", True),], },),
            ("paintcurve.select",{"type": 'A', "value": 'PRESS', "repeat": True},{"properties": [("toggle", True),], },),
            ("paintcurve.cursor", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("paintcurve.delete_point", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("paintcurve.delete_point", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("paintcurve.draw", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),
            ("paintcurve.draw", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "repeat": True}, None),
            ("transform.translate", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("transform.rotate", {"type": 'E', "value": 'PRESS', "repeat": True}, None),
            ("transform.resize", {"type": 'R', "value": 'PRESS', "repeat": True}, None),],},),

("Paint Face Mask (Weight, Vertex, Texture)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("paint.face_select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("paint.face_select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("paint.face_select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("paint.face_select_hide",{"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("unselected", False),], },),
            ("paint.face_select_hide",{"type": 'H', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("unselected", True),], },),
            ("paint.face_select_reveal", {"type": 'H', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("paint.face_select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("paint.face_select_linked_pick",{"type": 'L', "value": 'PRESS', "repeat": True},{"properties": [("deselect", False),], },),
            ("paint.face_select_linked_pick",{"type": 'L', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("deselect", True),], },),],},),

("Paint Stroke Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),],},),

("Paint Vertex Selection (Weight, Vertex)",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("paint.vert_select_all", {"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True}, None),],},),

############
# PARTICLE #
############
("Particle",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("particle.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("particle.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("particle.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("particle.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("particle.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("particle.select_linked_pick",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("deselect", False),], },),
            ("particle.select_linked_pick",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("deselect", True),], },),
            ("particle.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("particle.delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("particle.delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("particle.reveal", {"type": 'H', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("particle.hide",{"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("unselected", False),], },),
            ("particle.hide",{"type": 'H', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("unselected", True),], },),
            ("particle.brush_edit", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("particle.brush_edit", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS', "repeat": True},{"properties": [("data_path_primary", 'tool_settings.particle_edit.brush.size'),], },),
            ("wm.radial_control",{"type": 'U', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("data_path_primary", 'tool_settings.particle_edit.brush.strength'),], },),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_proportional_edit'),], },),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_particle_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'VIEW3D_MT_particle_context_menu'),], },),],},),

########
# POSE #
########
("Pose",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("screen.frame_offset",{"type": 'LEFT_ARROW', "value": 'PRESS'},{"properties": [("delta", -1),], },),
            ("screen.frame_offset",{"type": 'RIGHT_ARROW', "value": 'PRESS'},{"properties": [("delta", 1),], },),
            ("screen.frame_jump",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True},{"properties": [("end", True),], },),
            ("screen.frame_jump",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True},{"properties": [("end", False),], },),
            ("object.parent_set", {"type": 'P', "value": 'PRESS'}, None),
            ("pose.hide",{"type": 'H', "value": 'PRESS', "ctrl": True},{"properties": [("unselected", False),], },),
            ("pose.hide",{"type": 'H', "value": 'PRESS', "shift": True},{"properties": [("unselected", True),], },),
            ("pose.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
            ("pose.rot_clear", {"type": 'E', "value": 'PRESS', "alt": True}, None),
            ("pose.loc_clear", {"type": 'W', "value": 'PRESS', "alt": True}, None),
            ("pose.scale_clear", {"type": 'R', "value": 'PRESS', "alt": True}, None),
            ("pose.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
            ("pose.paste",{"type": 'V', "value": 'PRESS', "ctrl": True},{"properties": [("flipped", False),], },),
            ("pose.paste",{"type": 'V', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("flipped", True),], },),
            ("pose.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True},{"properties": [("action", 'SELECT'),], },),
            ("pose.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("action", 'DESELECT'),], },),
            ("pose.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties": [("action", 'INVERT'),], },),
            ("pose.select_parent", {"type": 'UP_ARROW', "value": 'PRESS', "ctrl": True}, None),
            ("pose.select_hierarchy",{"type": 'UP_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'PARENT'),("extend", False),], },),
            ("pose.select_hierarchy",{"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'PARENT'),("extend", True),], },),
            ("pose.select_hierarchy",{"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("direction", 'CHILD'),("extend", False),], },),
            ("pose.select_hierarchy",{"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("direction", 'CHILD'),("extend", True),], },),
            ("pose.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS'}, None),
            ("pose.bone_layers", {"type": 'G', "value": 'PRESS'}, None),
            ("anim.keyframe_insert_menu", {"type": 'S', "value": 'PRESS', "shift": True}, None),
            ("anim.keyframe_insert_by_name",{"type": 'S', "value": 'PRESS'},{"properties": [("type", 'LocRotScale'),], },),
            ("anim.keyframe_insert_by_name",{"type": 'W', "value": 'PRESS', "shift": True},{"properties": [("type", 'Location'),], },),
            ("anim.keyframe_insert_by_name",{"type": 'E', "value": 'PRESS', "shift": True},{"properties": [("type", 'Rotation'),], },),
            ("anim.keyframe_insert_by_name",{"type": 'R', "value": 'PRESS', "shift": True},{"properties": [("type", 'Scaling'),], },),
            ("anim.keyframe_delete_v3d", {"type": 'S', "value": 'PRESS', "alt": True}, None),
            ("anim.keying_set_active_set", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_pose_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_pose_context_menu'),], },),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties": [("name", 'builtin.select_box'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS'},{"properties": [("name", 'builtin.move'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS'},{"properties": [("name", 'builtin.rotate'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS'},{"properties": [("name", 'builtin.scale'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS'},{"properties": [("name", 'builtin.transform'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS'},{"properties": [("name", 'builtin.measure'),("cycle", True),], },),],},),

###################
# PROPERTY EDITOR #
###################
("Property Editor",
    {"space_type": 'PROPERTIES', "region_type": 'WINDOW'},
        {"items":
            [("wm.search_menu", {"type": 'TAB', "value": 'PRESS'}, None),
            ("buttons.context_menu", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
            ("screen.space_context_cycle",{"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("direction", 'PREV'),], },),
            ("screen.space_context_cycle",{"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("direction", 'NEXT'),], },),
            ("buttons.start_filter", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
            ("buttons.clear_filter", {"type": 'ESC', "value": 'PRESS'}, None),
            ("object.modifier_set_active", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("object.modifier_remove",{"type": 'BACK_SPACE', "value": 'PRESS'},{"properties": [("report", True),], },),
            ("object.modifier_remove",{"type": 'DEL', "value": 'PRESS'},{"properties": [("report", True),], },),
            ("object.modifier_copy", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("object.gpencil_modifier_remove",{"type": 'BACK_SPACE', "value": 'PRESS'},{"properties": [("report", True),], },),
            ("object.gpencil_modifier_remove",{"type": 'DEL', "value": 'PRESS'},{"properties": [("report", True),], },),
            ("object.gpencil_modifier_copy", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("object.shaderfx_remove",{"type": 'BACK_SPACE', "value": 'PRESS'},{"properties": [("report", True),], },),
            ("object.shaderfx_remove",{"type": 'DEL', "value": 'PRESS'},{"properties": [("report", True),], },),
            ("objectshaderfx_copy", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("constraint.delete",{"type": 'BACK_SPACE', "value": 'PRESS'},{"properties": [("report", True),], },),
            ("constraint.delete",{"type": 'DEL', "value": 'PRESS'},{"properties": [("report", True),], },),],},),

#######################
# REGION CONTEXT MENU #
#######################
("Region Context Menu",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("screen.region_context_menu", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),],},),

##########
# SCREEN #
##########
("Screen",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("screen.repeat_last", {"type": 'G', "value": 'PRESS', "repeat": True}, None),
            ("screen.userpref_show", {"type": 'COMMA', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("screen.animation_step", {"type": 'TIMER0', "value": 'ANY', "any": True}, None),
            ("screen.region_blend", {"type": 'TIMERREGION', "value": 'ANY', "any": True}, None),
            ("screen.space_context_cycle",{"type": 'TAB', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("direction", 'NEXT'),], },),
            ("screen.space_context_cycle",{"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("direction", 'PREV'),], },),
            ("screen.workspace_cycle",{"type": 'PAGE_DOWN', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("direction", 'NEXT'),], },),
            ("screen.workspace_cycle",{"type": 'PAGE_UP', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("direction", 'PREV'),], },),
            ("file.execute", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),
            ("file.execute", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "repeat": True}, None),
            ("file.cancel", {"type": 'ESC', "value": 'PRESS', "repeat": True}, None),
            ("ed.undo", {"type": 'Z', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("ed.redo", {"type": 'Z', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
            ("ed.undo_history", {"type": 'Z', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True}, None),
            ("render.view_cancel", {"type": 'ESC', "value": 'PRESS', "repeat": True}, None),
            ("screen.workspace_cycle",{"type": 'TAB', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("direction", 'NEXT'),], },),
            ("screen.workspace_cycle",{"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("direction", 'PREV'),], },),],}, ),

("Screen Editing",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("screen.actionzone",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("modifier", 0),], },),
            ("screen.actionzone",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("modifier", 1),], },),
            ("screen.actionzone",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("modifier", 2),], },),
            ("screen.area_split", {"type": 'ACTIONZONE_AREA', "value": 'ANY'}, None),
            ("screen.area_join", {"type": 'ACTIONZONE_AREA', "value": 'ANY'}, None),
            ("screen.area_dupli", {"type": 'ACTIONZONE_AREA', "value": 'ANY', "shift": True}, None),
            ("screen.area_swap", {"type": 'ACTIONZONE_AREA', "value": 'ANY', "ctrl": True}, None),
            ("screen.region_scale", {"type": 'ACTIONZONE_REGION', "value": 'ANY'}, None),
            ("screen.screen_full_area",{"type": 'ACTIONZONE_FULLSCREEN', "value": 'ANY'},{"properties": [("use_hide_panels", True),], },),
            ("screen.area_move", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("screen.area_options", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
            ("render.render",{"type": 'RET', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("use_viewport", True),], },),
            ("render.render",{"type": 'RET', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True},{"properties": [("animation", True),("use_viewport", True),], },),
            ("render.view_cancel", {"type": 'ESC', "value": 'PRESS', "repeat": True}, None),
            ("screen.screen_full_area",{"type": 'SPACE', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("use_hide_panels", True),], },),
            ("screen.screen_full_area", {"type": 'F11', "value": 'PRESS'}, None),],},),

##########
# SCULPT #
##########
("Sculpt",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("sculpt.brush_stroke",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties":[("mode", 'NORMAL'),],},),
            ("sculpt.brush_stroke",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties":[("mode", 'INVERT'),],},),
            ("sculpt.brush_stroke",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties":[("mode", 'SMOOTH'),],},),
            ("paint.hide_show",{"type": 'H', "value": 'PRESS', "shift": True},{"properties":[("action", 'SHOW'),("area", 'INSIDE'),],},),
            ("paint.hide_show",{"type": 'H', "value": 'PRESS', "ctrl": True},{"properties":[("action", 'HIDE'),("area", 'INSIDE'),],},),
            ("paint.hide_show",{"type": 'H', "value": 'PRESS', "alt": True},{"properties":[("action", 'SHOW'),("area", 'ALL'),],},),
            ("object.subdivision_set",{"type": 'ZERO', "value": 'PRESS', "ctrl": True},{"properties":[("level", 0),("relative", False),],},),
            ("object.subdivision_set",{"type": 'ONE', "value": 'PRESS', "ctrl": True},{"properties":[("level", 1),("relative", False),],},),
            ("object.subdivision_set",{"type": 'TWO', "value": 'PRESS', "ctrl": True},{"properties":[("level", 2),("relative", False),],},),
            ("object.subdivision_set",{"type": 'THREE', "value": 'PRESS', "ctrl": True},{"properties":[("level", 3),("relative", False),],},),
            ("object.subdivision_set",{"type": 'FOUR', "value": 'PRESS', "ctrl": True},{"properties":[("level", 4),("relative", False),],},),
            ("object.subdivision_set",{"type": 'FIVE', "value": 'PRESS', "ctrl": True},{"properties":[("level", 5),("relative", False),],},),
            ("object.subdivision_set",{"type": 'PAGE_UP', "value": 'PRESS', "repeat": True},{"properties":[("level", 1),("relative", True),],},),
            ("object.subdivision_set",{"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True},{"properties":[("level", -1),("relative", True),],},),
            ("paint.mask_flood_fill",{"type": 'A', "value": 'PRESS', "ctrl": True},{"properties":[("mode", 'VALUE'),("value", 0.0),],},),
            ("paint.mask_flood_fill",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},{"properties":[("mode", 'VALUE'),("value", 1.0),],},),
            ("paint.mask_flood_fill",{"type": 'I', "value": 'PRESS', "ctrl": True},{"properties":[("mode", 'INVERT'),],},),
            ("paint.mask_box_gesture",{"type": 'B', "value": 'PRESS'},{"properties":[("mode", 'VALUE'),("value", 0.0),],},),
            ("paint.mask_lasso_gesture", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
            ("wm.context_toggle",{"type": 'M', "value": 'PRESS', "ctrl": True},{"properties":[("data_path", 'scene.tool_settings.sculpt.show_mask'),],},),
            ("sculpt.dynamic_topology_toggle", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
            ("sculpt.dyntopo_detail_size_edit", {"type": 'D', "value": 'PRESS', "shift": True}, None),
            ("sculpt.set_detail_size", {"type": 'D', "value": 'PRESS', "shift": True, "alt": True}, None),
            ("object.voxel_remesh", {"type": 'R', "value": 'PRESS', "ctrl": True}, None),
            ("object.quadriflow_remesh", {"type": 'R', "value": 'PRESS', "ctrl": True, "alt": True}, None),
            ("object.voxel_remesh", {"type": 'R', "value": 'PRESS', "ctrl": True}, None),
            ("object.voxel_size_edit", {"type": 'R', "value": 'PRESS', "shift": True}, None),
            ("object.quadriflow_remesh", {"type": 'R', "value": 'PRESS', "ctrl": True, "alt": True}, None),
            ("brush.scale_size",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties":[("scalar", 0.9),],},),
            ("brush.scale_size",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties":[("scalar", 1.1111112),],},),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS'},{"properties":[("data_path_primary", 'tool_settings.sculpt.brush.size'),("data_path_secondary", 'tool_settings.unified_paint_settings.size'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),("rotation_path", 'tool_settings.sculpt.brush.texture_slot.angle'),("color_path", 'tool_settings.sculpt.brush.cursor_color_add'),("fill_color_path", ''),("fill_color_override_path", ''),("fill_color_override_test_path", ''),("zoom_path", ''),("image_id", 'tool_settings.sculpt.brush'),("secondary_tex", False),],},),
            ("wm.radial_control",{"type": 'U', "value": 'PRESS'},{"properties":[("data_path_primary", 'tool_settings.sculpt.brush.strength'),("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),("rotation_path", 'tool_settings.sculpt.brush.texture_slot.angle'),("color_path", 'tool_settings.sculpt.brush.cursor_color_add'),("fill_color_path", ''),("fill_color_override_path", ''),("fill_color_override_test_path", ''),("zoom_path", ''),("image_id", 'tool_settings.sculpt.brush'),("secondary_tex", False),],},),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "ctrl": True},{"properties":[("data_path_primary", 'tool_settings.sculpt.brush.texture_slot.angle'),("data_path_secondary", ''),("use_secondary", ''),("rotation_path", 'tool_settings.sculpt.brush.texture_slot.angle'),("color_path", 'tool_settings.sculpt.brush.cursor_color_add'),("fill_color_path", ''),("fill_color_override_path", ''),("fill_color_override_test_path", ''),("zoom_path", ''),("image_id", 'tool_settings.sculpt.brush'),("secondary_tex", False),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties":[("mode", 'TRANSLATION'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},{"properties":[("mode", 'SCALE'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},{"properties":[("mode", 'ROTATION'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},{"properties":[("mode", 'TRANSLATION'),("texmode", 'SECONDARY'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties":[("mode", 'SCALE'),("texmode", 'SECONDARY'),],},),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},{"properties":[("mode", 'ROTATION'),("texmode", 'SECONDARY'),],},),
            ("paint.brush_select",{"type": 'S', "value": 'PRESS'},{"properties":[("sculpt_tool", 'SMOOTH'),],},),
            ("paint.brush_select",{"type": 'P', "value": 'PRESS'},{"properties":[("sculpt_tool", 'PINCH'),],},),
            ("paint.brush_select",{"type": 'I', "value": 'PRESS'},{"properties":[("sculpt_tool", 'INFLATE'),],},),
            ("paint.brush_select",{"type": 'G', "value": 'PRESS'},{"properties":[("sculpt_tool", 'GRAB'),],},),
            ("paint.brush_select",{"type": 'L', "value": 'PRESS'},{"properties":[("sculpt_tool", 'LAYER'),],},),
            ("paint.brush_select",{"type": 'T', "value": 'PRESS', "shift": True},{"properties":[("sculpt_tool", 'FLATTEN'),],},),
            ("paint.brush_select",{"type": 'C', "value": 'PRESS'},{"properties":[("sculpt_tool", 'CLAY'),],},),
            ("paint.brush_select",{"type": 'C', "value": 'PRESS', "shift": True},{"properties":[("sculpt_tool", 'CREASE'),],},),
            ("paint.brush_select",{"type": 'M', "value": 'PRESS'},{"properties":[("sculpt_tool", 'MASK'),("toggle", True),("create_missing", True),],},),
            ("paint.brush_select",{"type": 'R', "value": 'PRESS'},{"properties":[("sculpt_tool", 'ROTATE'),],},),
            ("paint.brush_select",{"type": 'N', "value": 'PRESS'},{"properties":[("sculpt_tool", 'NUDGE'),],},),
            ("paint.brush_select",{"type": 'T', "value": 'PRESS'},{"properties":[("sculpt_tool", 'THUMB'),],},),
            ("paint.brush_select",{"type": 'H', "value": 'PRESS'},{"properties":[("sculpt_tool", 'SNAKE_HOOK'),],},),
            ("paint.brush_select",{"type": 'B', "value": 'PRESS'},{"properties":[("sculpt_tool", 'BLOB'),],},),
            ("paint.brush_select",{"type": 'D', "value": 'PRESS'},{"properties":[("sculpt_tool", 'DRAW'),],},),
            ("wm.call_panel",{"type": 'APP', "value": 'PRESS'},{"properties":[("name", 'VIEW3D_PT_sculpt_context_menu'),],},),],},),

("Sculpt Expand Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
            ("CONFIRM", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ("INVERT", {"type": 'F', "value": 'PRESS', "any": True}, None),
            ("PRESERVE", {"type": 'E', "value": 'PRESS', "any": True}, None),
            ("GRADIENT", {"type": 'G', "value": 'PRESS', "any": True}, None),
            ("RECURSION_STEP_GEODESIC", {"type": 'R', "value": 'PRESS'}, None),
            ("RECURSION_STEP_TOPOLOGY", {"type": 'R', "value": 'PRESS', "alt": True}, None),
            ("MOVE_TOGGLE", {"type": 'SPACE', "value": 'ANY', "any": True}, None),
            ("FALLOFF_GEODESICS", {"type": 'ONE', "value": 'PRESS', "any": True}, None),
            ("FALLOFF_TOPOLOGY", {"type": 'TWO', "value": 'PRESS', "any": True}, None),
            ("FALLOFF_TOPOLOGY_DIAGONALS", {"type": 'THREE', "value": 'PRESS', "any": True}, None),
            ("FALLOFF_SPHERICAL", {"type": 'FOUR', "value": 'PRESS', "any": True}, None),
            ("SNAP_TOGGLE", {"type": 'LEFT_CTRL', "value": 'ANY'}, None),
            ("LOOP_COUNT_INCREASE", {"type": 'W', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("LOOP_COUNT_DECREASE", {"type": 'Q', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("BRUSH_GRADIENT_TOGGLE", {"type": 'B', "value": 'PRESS', "any": True}, None),
            ("TEXTURE_DISTORTION_INCREASE", {"type": 'Y', "value": 'PRESS'}, None),
            ("TEXTURE_DISTORTION_DECREASE", {"type": 'T', "value": 'PRESS'}, None),],},),

#############
# SEQUENCER #
#############
("Sequencer",
    {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("screen.frame_offset",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("delta", -1),], },),
            ("screen.frame_offset",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("delta", 1),], },),
            ("screen.frame_jump",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("end", True),], },),
            ("screen.frame_jump",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("end", False),], },),
            ("sequencer.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),], },),
            ("sequencer.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),], },),
            ("sequencer.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),], },),
            ("sequencer.split",{"type": 'B', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'SOFT'),], },),
            ("sequencer.mute",{"type": 'M', "value": 'PRESS', "repeat": True},{"properties": [("unselected", False),], },),
            ("sequencer.mute",{"type": 'M', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("unselected", True),], },),
            ("sequencer.unmute",{"type": 'M', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("unselected", False),], },),
            ("sequencer.unmute",{"type": 'M', "value": 'PRESS', "shift": True, "alt": True, "repeat": True},{"properties": [("unselected", True),], },),
            ("sequencer.lock", {"type": 'L', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("sequencer.unlock", {"type": 'L', "value": 'PRESS', "shift": True, "alt": True, "repeat": True}, None),
            ("sequencer.reassign_inputs", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.reload", {"type": 'R', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("sequencer.reload",{"type": 'R', "value": 'PRESS', "shift": True, "alt": True, "repeat": True},{"properties": [("adjust_length", True),], },),
            ("sequencer.offset_clear", {"type": 'O', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("sequencer.duplicate_move", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("sequencer.delete", {"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.delete", {"type": 'DEL', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("sequencer.paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("sequencer.images_separate", {"type": 'Y', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.meta_toggle", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
            ("sequencer.meta_make", {"type": 'G', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("sequencer.meta_separate", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True}, None),
            ("sequencer.view_all", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("sequencer.view_selected", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.strip_jump",{"type": 'PAGE_UP', "value": 'PRESS', "repeat": True},{"properties": [("next", True),("center", False),], },),
            ("sequencer.strip_jump",{"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True},{"properties": [("next", False),("center", False),], },),
            ("sequencer.strip_jump",{"type": 'PAGE_UP', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("next", True),("center", True),], },),
            ("sequencer.strip_jump",{"type": 'PAGE_DOWN', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("next", False),("center", True),], },),
            ("sequencer.swap",{"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("side", 'LEFT'),], },),
            ("sequencer.swap",{"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("side", 'RIGHT'),], },),
            ("sequencer.gap_remove",{"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True},{"properties": [("all", False),], },),
            ("sequencer.gap_remove",{"type": 'BACK_SPACE', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("all", True),], },),
            ("sequencer.gap_insert", {"type": 'EQUAL', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("sequencer.snap", {"type": 'X', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.swap_inputs", {"type": 'S', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("sequencer.split_multicam",{"type": 'ONE', "value": 'PRESS', "repeat": True},{"properties": [("camera", 1),], },),
            ("sequencer.split_multicam",{"type": 'TWO', "value": 'PRESS', "repeat": True},{"properties": [("camera", 2),], },),
            ("sequencer.split_multicam",{"type": 'THREE', "value": 'PRESS', "repeat": True},{"properties": [("camera", 3),], },),
            ("sequencer.split_multicam",{"type": 'FOUR', "value": 'PRESS', "repeat": True},{"properties": [("camera", 4),], },),
            ("sequencer.split_multicam",{"type": 'FIVE', "value": 'PRESS', "repeat": True},{"properties": [("camera", 5),], },),
            ("sequencer.split_multicam",{"type": 'SIX', "value": 'PRESS', "repeat": True},{"properties": [("camera", 6),], },),
            ("sequencer.split_multicam",{"type": 'SEVEN', "value": 'PRESS', "repeat": True},{"properties": [("camera", 7),], },),
            ("sequencer.split_multicam",{"type": 'EIGHT', "value": 'PRESS', "repeat": True},{"properties": [("camera", 8),], },),
            ("sequencer.split_multicam",{"type": 'NINE', "value": 'PRESS', "repeat": True},{"properties": [("camera", 9),], },),
            ("sequencer.split_multicam",{"type": 'ZERO', "value": 'PRESS', "repeat": True},{"properties": [("camera", 10),], },),
            ("sequencer.select",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("deselect_all", True),], },),
            ("sequencer.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("extend", True),], },),
            ("sequencer.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True},{"properties": [("linked_handle", True),], },),
            ("sequencer.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties": [("extend", True),("linked_handle", True),], },),
            ("sequencer.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("linked_time", True),("side_of_frame", True),], },),
            ("sequencer.select",{"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},{"properties": [("extend", True),("linked_time", True),("side_of_frame", True),], },),
            ("sequencer.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.select_linked_pick",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("extend", False),], },),
            ("sequencer.select_linked_pick",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("extend", True),], },),
            ("sequencer.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("sequencer.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("mode", 'SET'),("tweak", True),], },),
            ("sequencer.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),("tweak", True),], },),
            ("sequencer.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),("tweak", True),], },),
            ("sequencer.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("sequencer.slip", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("wm.context_set_int",{"type": 'O', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'scene.sequence_editor.overlay_frame'),("value", 0),], },),
            ("transform.seq_slide", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("transform.seq_slide", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("transform.seq_slide", {"type": 'EVT_TWEAK_M', "value": 'ANY'}, None),
            ("transform.transform",{"type": 'E', "value": 'PRESS', "repeat": True},{"properties": [("mode", 'TIME_EXTEND'),], },),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'SEQUENCER_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'SEQUENCER_MT_context_menu'),], },),
            ("marker.add", {"type": 'M', "value": 'PRESS', "repeat": True}, None),
            ("marker.rename", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.select_box'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'B', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.blade'),("cycle", True),], },),],},),

("Sequencer Tool: Blade",
    {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("sequencer.split",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties": [("type", 'SOFT'),("use_cursor_position", True),("side", 'NO_CHANGE'),("ignore_selection", True),], },),
            ("sequencer.split",{"type": 'MIDDLEMOUSE', "value": 'PRESS'},{"properties": [("type", 'SOFT'),("use_cursor_position", True),("side", 'NO_CHANGE'),("ignore_selection", True),], },),],}, ),

("Sequencer Tool: Sample",
    {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("sequencer.sample", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("sequencer.sample", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),],},),

("Sequencer Tool: Select",
    {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("sequencer.select",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("extend", False),("deselect_all", True),], },),
            ("anim.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("anim.change_frame", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),],},),

("Sequencer Tool: Select Box",
    {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("sequencer.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY'},{"properties": [("tweak", False),], },),
            ("sequencer.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},{"properties": [("mode", 'ADD'),("tweak", False),], },),
            ("sequencer.select_box",{"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},{"properties": [("mode", 'SUB'),("tweak", False),], },),],},),

("SequencerCommon",
    {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("wm.context_toggle",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.show_region_ui'),], },),],},),

("SequencerPreview",
    {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.view_all_preview", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.view_all_preview", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ("sequencer.view_ghost_border", {"type": 'O', "value": 'PRESS', "repeat": True}, None),
            ("sequencer.view_zoom_ratio",{"type": 'NUMPAD_1', "value": 'PRESS', "repeat": True},{"properties": [("ratio", 1.0),], },),
            ("sequencer.sample", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),],},),

######################
# STANDARD MODAL MAP #
######################
("Standard Modal Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("APPLY", {"type": 'LEFTMOUSE', "value": 'ANY', "any": True}, None),
            ("APPLY", {"type": 'RET', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("APPLY", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("SNAP", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),],},),

########
# TEXT #
########
("Text",
    {"space_type": 'TEXT_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("text.move",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'LINE_BEGIN'),], },),
            ("text.move",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'LINE_END'),], },),
            ("text.move",{"type": 'UP_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'FILE_TOP'),], },),
            ("text.move",{"type": 'DOWN_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'FILE_BOTTOM'),], },),
            ("text.move",{"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),], },),
            ("text.move",{"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),], },),
            ("wm.context_cycle_int",{"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("data_path", 'space_data.font_size'),("reverse", False),], },),
            ("wm.context_cycle_int",{"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("data_path", 'space_data.font_size'),("reverse", True),], },),
            ("wm.context_cycle_int",{"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.font_size'),("reverse", False),], },),
            ("wm.context_cycle_int",{"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.font_size'),("reverse", True),], },),
            ("text.new", {"type": 'N', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.open", {"type": 'O', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("text.reload", {"type": 'R', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("text.save", {"type": 'S', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("text.save_as", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True, "repeat": True}, None),
            ("text.run_script", {"type": 'P', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("text.cut", {"type": 'X', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.copy", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.paste", {"type": 'V', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.cut", {"type": 'DEL', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("text.copy", {"type": 'INSERT', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.paste", {"type": 'INSERT', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("text.duplicate_line", {"type": 'D', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.select_all", {"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.select_line", {"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
            ("text.select_word", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
            ("text.move_lines",{"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("direction", 'UP'),], },),
            ("text.move_lines",{"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("direction", 'DOWN'),], },),
            ("text.indent_or_autocomplete", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("text.unindent", {"type": 'TAB', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("text.uncomment", {"type": 'D', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
            ("text.move",{"type": 'HOME', "value": 'PRESS', "repeat": True},{"properties": [("type", 'LINE_BEGIN'),], },),
            ("text.move",{"type": 'END', "value": 'PRESS', "repeat": True},{"properties": [("type", 'LINE_END'),], },),
            ("text.move",{"type": 'E', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'LINE_END'),], },),
            ("text.move",{"type": 'E', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("type", 'LINE_END'),], },),
            ("text.move",{"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("text.move",{"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_CHARACTER'),], },),
            ("text.move",{"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),], },),
            ("text.move",{"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),], },),
            ("text.move",{"type": 'UP_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_LINE'),], },),
            ("text.move",{"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_LINE'),], },),
            ("text.move",{"type": 'PAGE_UP', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_PAGE'),], },),
            ("text.move",{"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_PAGE'),], },),
            ("text.move",{"type": 'HOME', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'FILE_TOP'),], },),
            ("text.move",{"type": 'END', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'FILE_BOTTOM'),], },),
            ("text.move_select",{"type": 'HOME', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'LINE_BEGIN'),], },),
            ("text.move_select",{"type": 'END', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'LINE_END'),], },),
            ("text.move_select",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("text.move_select",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'NEXT_CHARACTER'),], },),
            ("text.move_select",{"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),], },),
            ("text.move_select",{"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),], },),
            ("text.move_select",{"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_LINE'),], },),
            ("text.move_select",{"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'NEXT_LINE'),], },),
            ("text.move_select",{"type": 'PAGE_UP', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_PAGE'),], },),
            ("text.move_select",{"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'NEXT_PAGE'),], },),
            ("text.move_select",{"type": 'HOME', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("type", 'FILE_TOP'),], },),
            ("text.move_select",{"type": 'END', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("type", 'FILE_BOTTOM'),], },),
            ("text.delete",{"type": 'DEL', "value": 'PRESS', "repeat": True},{"properties": [("type", 'NEXT_CHARACTER'),], },),
            ("text.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("text.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("type", 'PREVIOUS_CHARACTER'),], },),
            ("text.delete",{"type": 'DEL', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'NEXT_WORD'),], },),
            ("text.delete",{"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("type", 'PREVIOUS_WORD'),], },),
            ("text.overwrite_toggle", {"type": 'INSERT', "value": 'PRESS', "repeat": True}, None),
            ("text.scroll_bar", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("text.scroll_bar", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("text.scroll", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("text.scroll", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
            ("text.selection_set", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("text.cursor_set", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("text.selection_set", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
            ("text.scroll",{"type": 'WHEELUPMOUSE', "value": 'PRESS'},{"properties": [("lines", -1),], },),
            ("text.scroll",{"type": 'WHEELDOWNMOUSE', "value": 'PRESS'},{"properties": [("lines", 1),], },),
            ("text.line_break", {"type": 'RET', "value": 'PRESS', "repeat": True}, None),
            ("text.line_break", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "repeat": True}, None),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True},{"properties": [("name", 'TEXT_MT_context_menu'),], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TEXT_MT_context_menu'),], },),
            ("text.line_number", {"type": 'TEXTINPUT', "value": 'ANY', "any": True}, None),
            ("text.insert", {"type": 'TEXTINPUT', "value": 'ANY', "any": True}, None),],},),

("Text Generic",
    {"space_type": 'TEXT_EDITOR', "region_type": 'WINDOW'},
        {"items":
            [("text.intellisense", {"type": 'SPACE', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
            ("text.start_find", {"type": 'F', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.jump", {"type": 'J', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.find", {"type": 'G', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("text.replace", {"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.context_toggle",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("data_path", 'space_data.show_region_ui'),], },),],},),

##############
# TIME SCRUB #
##############
("Time Scrub",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("anim.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),],},),

#################
# TOOLBAR POPUP #
#################
("Toolbar Popup",
    {"space_type": 'EMPTY', "region_type": 'TEMPORARY'},
        {"items":
            [("wm.tool_set_by_id",{"type": 'SPACE', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.cursor'),], },),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.select'),], },),
            ("wm.tool_set_by_id",{"type": 'L', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.select_lasso'),], },),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.transform'),], },),
            ("wm.tool_set_by_id",{"type": 'M', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.measure'),], },),],},),

#######################
# TRANSFORM MODAL MAP #
#######################
("Transform Modal Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CONFIRM", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
            ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
            ("CONFIRM", {"type": 'SPACE', "value": 'PRESS', "any": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
            ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
            ("AXIS_X", {"type": 'X', "value": 'PRESS'}, None),
            ("AXIS_Y", {"type": 'Y', "value": 'PRESS'}, None),
            ("AXIS_Z", {"type": 'Z', "value": 'PRESS'}, None),
            ("PLANE_X", {"type": 'X', "value": 'PRESS', "shift": True}, None),
            ("PLANE_Y", {"type": 'Y', "value": 'PRESS', "shift": True}, None),
            ("PLANE_Z", {"type": 'Z', "value": 'PRESS', "shift": True}, None),
            ("CONS_OFF", {"type": 'C', "value": 'PRESS'}, None),
            ("TRANSLATE", {"type": 'G', "value": 'PRESS'}, None),
            ("ROTATE", {"type": 'R', "value": 'PRESS'}, None),
            ("RESIZE", {"type": 'S', "value": 'PRESS'}, None),
            ("SNAP_TOGGLE", {"type": 'TAB', "value": 'PRESS', "shift": True}, None),
            ("SNAP_INV_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
            ("SNAP_INV_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ("SNAP_INV_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
            ("SNAP_INV_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
            ("ADD_SNAP", {"type": 'A', "value": 'PRESS'}, None),
            ("ADD_SNAP", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
            ("REMOVE_SNAP", {"type": 'A', "value": 'PRESS', "alt": True}, None),
            ("PROPORTIONAL_SIZE_UP", {"type": 'PAGE_UP', "value": 'PRESS', "repeat": True}, None),
            ("PROPORTIONAL_SIZE_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True}, None),
            ("PROPORTIONAL_SIZE_UP", {"type": 'PAGE_UP', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("PROPORTIONAL_SIZE_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("PROPORTIONAL_SIZE_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
            ("PROPORTIONAL_SIZE_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
            ("PROPORTIONAL_SIZE_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True}, None),
            ("PROPORTIONAL_SIZE_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True}, None),
            ("PROPORTIONAL_SIZE", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
            ("EDGESLIDE_EDGE_NEXT", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "alt": True}, None),
            ("EDGESLIDE_PREV_NEXT", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "alt": True}, None),
            ("AUTOIK_CHAIN_LEN_UP", {"type": 'PAGE_UP', "value": 'PRESS', "repeat": True}, None),
            ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True}, None),
            ("AUTOIK_CHAIN_LEN_UP", {"type": 'PAGE_UP', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True, "repeat": True}, None),
            ("AUTOIK_CHAIN_LEN_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
            ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
            ("AUTOIK_CHAIN_LEN_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True}, None),
            ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True}, None),
            ("INSERTOFS_TOGGLE_DIR", {"type": 'T', "value": 'PRESS'}, None),
            ("AUTOCONSTRAIN", {"type": 'MIDDLEMOUSE', "value": 'ANY'}, None),
            ("AUTOCONSTRAINPLANE", {"type": 'MIDDLEMOUSE', "value": 'ANY', "shift": True}, None),
            ("PRECISION", {"type": 'LEFT_SHIFT', "value": 'ANY', "any": True}, None),
            ("PRECISION", {"type": 'RIGHT_SHIFT', "value": 'ANY', "any": True}, None),],},),

#############
# UV EDITOR #
#############
("UV Editor",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_panel",{"type": 'RET', "value": 'PRESS', "repeat": True},{"properties": [("name", 'TOPBAR_PT_name'),("keep_open", False),], },),
            ("wm.search_menu", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("mesh.select_mode",{"type": 'ONE', "value": 'PRESS', "repeat": True},{"properties": [("type", 'VERT'),], },),
            ("mesh.select_mode",{"type": 'TWO', "value": 'PRESS', "repeat": True},{"properties": [("type", 'EDGE'),], },),
            ("mesh.select_mode",{"type": 'THREE', "value": 'PRESS', "repeat": True},{"properties": [("type", 'FACE'),], },),
            ("mesh.select_mode",{"type": 'ONE', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("use_extend", True),("type", 'VERT'),], },),
            ("mesh.select_mode",{"type": 'TWO', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("use_extend", True),("type", 'EDGE'),], },),
            ("mesh.select_mode",{"type": 'THREE', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("use_extend", True),("type", 'FACE'),], },),
            ("mesh.select_mode",{"type": 'ONE', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("use_expand", True),("type", 'VERT'),], },),
            ("mesh.select_mode",{"type": 'TWO', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("use_expand", True),("type", 'EDGE'),], },),
            ("mesh.select_mode",{"type": 'THREE', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("use_expand", True),("type", 'FACE'),], },),
            ("mesh.select_mode",{"type": 'ONE', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("use_extend", True),  ("use_expand", True),  ("type", 'VERT'),  ], },),
            ("mesh.select_mode",{"type": 'TWO', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("use_extend", True),  ("use_expand", True),  ("type", 'EDGE'),  ], },),
            ("mesh.select_mode",{"type": 'THREE', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("use_extend", True),  ("use_expand", True),  ("type", 'FACE'),  ], },),
            ("wm.context_set_enum",{"type": 'ONE', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.uv_select_mode'),  ("value", 'VERTEX'),  ], },),
            ("wm.context_set_enum",{"type": 'TWO', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.uv_select_mode'),  ("value", 'EDGE'),  ], },),
            ("wm.context_set_enum",{"type": 'THREE', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.uv_select_mode'),  ("value", 'FACE'),  ], },),
            ("wm.context_set_enum",{"type": 'FOUR', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.uv_select_mode'),  ("value", 'ISLAND'),  ], },),
            ("uv.select",{"type": 'LEFTMOUSE', "value": 'CLICK'},{"properties": [("extend", False),  ("deselect_all", True),  ], },),
            ("uv.select",{"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},{"properties": [("extend", True),  ("deselect_all", False),  ], },),
            ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
            ("uv.select_loop",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "shift": True},{"properties": [("extend", True),  ], },),
            ("uv.select_loop",{"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'},{"properties": [("extend", False),  ], },),
            ("uv.select_linked", {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True}, None),
            ("uv.select_more", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("uv.select_less", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("uv.select_all",{"type": 'A', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'SELECT'),  ], },),
            ("uv.select_all",{"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("action", 'DESELECT'),  ], },),
            ("uv.select_all",{"type": 'I', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("action", 'INVERT'),  ], },),
            ("uv.hide",{"type": 'H', "value": 'PRESS', "ctrl": True, "repeat": True},{"properties": [("unselected", False),  ], },),
            ("uv.hide",{"type": 'H', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("unselected", True),  ], },),
            ("uv.reveal", {"type": 'H', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("wm.call_menu_pie",{"type": 'X', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("name", 'IMAGE_MT_uvs_snap_pie'),  ], },),
            ("wm.call_menu",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("name", 'IMAGE_MT_uvs_context_menu'),  ], },),
            ("wm.call_menu",{"type": 'APP', "value": 'PRESS', "repeat": True},{"properties": [("name", 'IMAGE_MT_uvs_context_menu'),  ], },),
            ("wm.context_toggle",{"type": 'B', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_proportional_edit'),  ], },),
            ("wm.context_toggle",{"type": 'X', "value": 'PRESS', "repeat": True},{"properties": [("data_path", 'tool_settings.use_snap'),  ], },),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.select_box'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'W', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.move'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'E', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.rotate'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'R', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.scale'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'T', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.transform'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'C', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.cursor'),  ("cycle", True),  ], },),
            ("wm.tool_set_by_id",{"type": 'D', "value": 'PRESS', "repeat": True},{"properties": [("name", 'builtin.annotate'),  ("cycle", True),  ], },),],},),

##################
# USER INTERFACE #
##################
("User Interface",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("ui.eyedropper_color", {"type": 'I', "value": 'PRESS', "repeat": True}, None),
            ("ui.eyedropper_colorramp", {"type": 'I', "value": 'PRESS', "repeat": True}, None),
            ("ui.eyedropper_colorramp_point", {"type": 'I', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("ui.eyedropper_id", {"type": 'I', "value": 'PRESS', "repeat": True}, None),
            ("ui.eyedropper_depth", {"type": 'I', "value": 'PRESS', "repeat": True}, None),
            ("ui.copy_data_path_button", {"type": 'C', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("ui.copy_data_path_button",{"type": 'C', "value": 'PRESS', "ctrl": True, "alt": True, "repeat": True},{"properties": [("full_path", True),  ], },),
            ("anim.keyframe_insert_button", {"type": 'S', "value": 'PRESS', "repeat": True}, None),
            ("anim.keyframe_delete_button", {"type": 'S', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("anim.keyframe_clear_button", {"type": 'S', "value": 'PRESS', "shift": True, "alt": True, "repeat": True}, None),
            ("anim.driver_button_add", {"type": 'D', "value": 'PRESS', "repeat": True}, None),
            ("anim.driver_button_remove", {"type": 'D', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("anim.keyingset_button_add", {"type": 'K', "value": 'PRESS', "repeat": True}, None),
            ("anim.keyingset_button_remove", {"type": 'K', "value": 'PRESS', "alt": True, "repeat": True}, None),],},),

################
# VERTEX PAINT #
################
("Vertex Paint",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("paint.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS'},{"properties":[("mode", 'NORMAL'),],},),
            ("paint.vertex_paint",{"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},{"properties":[("mode", 'INVERT'),],},),
            ("paint.brush_colors_flip", {"type": 'X', "value": 'PRESS'}, None),
            ("brush.scale_size",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties":[("scalar", 0.9),],},),
            ("brush.scale_size",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties":[("scalar", 1.1111112),],},),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS'},{"properties":[("data_path_primary", 'tool_settings.vertex_paint.brush.size'),("data_path_secondary", 'tool_settings.unified_paint_settings.size'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),("rotation_path", 'tool_settings.vertex_paint.brush.texture_slot.angle'),("color_path", 'tool_settings.vertex_paint.brush.cursor_color_add'),("fill_color_path", 'tool_settings.vertex_paint.brush.color'),("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),("zoom_path", ''),("image_id", 'tool_settings.vertex_paint.brush'),("secondary_tex", False),],},),
            ("wm.radial_control",{"type": 'U', "value": 'PRESS'},{"properties":[("data_path_primary", 'tool_settings.vertex_paint.brush.strength'),("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),("rotation_path", 'tool_settings.vertex_paint.brush.texture_slot.angle'),("color_path", 'tool_settings.vertex_paint.brush.cursor_color_add'),("fill_color_path", 'tool_settings.vertex_paint.brush.color'),("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),("zoom_path", ''),("image_id", 'tool_settings.vertex_paint.brush'),("secondary_tex", False),],},),
            ("wm.radial_control",{"type": 'F', "value": 'PRESS', "ctrl": True},{"properties": [("data_path_primary", 'tool_settings.vertex_paint.brush.texture_slot.angle'),("data_path_secondary", ''),("use_secondary", ''),("rotation_path", 'tool_settings.vertex_paint.brush.texture_slot.angle'),("color_path", 'tool_settings.vertex_paint.brush.cursor_color_add'),("fill_color_path", 'tool_settings.vertex_paint.brush.color'),("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),("zoom_path", ''),("image_id", 'tool_settings.vertex_paint.brush'),("secondary_tex", False),], },),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS'},{"properties": [("mode", 'TRANSLATION'),], },),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},{"properties": [("mode", 'SCALE'),], },),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},{"properties": [("mode", 'ROTATION'),], },),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},{"properties": [("mode", 'TRANSLATION'),("texmode", 'SECONDARY'),], },),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},{"properties": [("mode", 'SCALE'),("texmode", 'SECONDARY'),], },),
            ("brush.stencil_control",{"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},{"properties": [("mode", 'ROTATION'),("texmode", 'SECONDARY'),], },),
            ("wm.context_toggle",{"type": 'M', "value": 'PRESS'},{"properties": [("data_path", 'vertex_paint_object.data.use_paint_mask'),], },),
            ("wm.context_toggle",{"type": 'S', "value": 'PRESS', "shift": True},{"properties": [("data_path", 'tool_settings.vertex_paint.brush.use_smooth_stroke'),], },),
            ("wm.call_menu",{"type": 'R', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_MT_angle_control'),], },),
            ("blui.right_mouse_navigation", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
            ("wm.call_panel",{"type": 'APP', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_PT_paint_vertex_context_menu'),], },),
            ("paint.brush_select",{"type": 'D', "value": 'PRESS'},{"properties": [("vertex_tool", 'DRAW'),], },),
            ("paint.brush_select",{"type": 'B', "value": 'PRESS'},{"properties": [("vertex_tool", 'BLUR'),], },),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties": [("name", 'builtin.select_box'),("cycle", True),], },),],},),

###########
# VIEW 2D #
###########
("View2D",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("view2d.scroller_activate", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("view2d.pan", {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG'}, None),
            ("view2d.scroll_right", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True}, None),
            ("view2d.scroll_left", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True}, None),
            ("view2d.scroll_down", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True}, None),
            ("view2d.scroll_up", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True}, None),
            ("view2d.ndof", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
            ("view2d.zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS'}, None),
            ("view2d.zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS'}, None),
            ("view2d.zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("view2d.zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS', "alt": True}, None),
            ("view2d.zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True}, None),
            ("view2d.zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True}, None),
            ("view2d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
            ("view2d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
            ("view2d.scroll_down", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
            ("view2d.scroll_up", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
            ("view2d.scroll_right", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
            ("view2d.scroll_left", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
            ("view2d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
            ("view2d.zoom_border", {"type": 'Z', "value": 'PRESS', "repeat": True}, None),],},),

("View2D Buttons List",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("view2d.scroller_activate", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("view2d.scroller_activate", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("view2d.pan", {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG'}, None),
            ("view2d.pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
            ("view2d.scroll_down", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
            ("view2d.scroll_up", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
            ("view2d.scroll_down",{"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True},{"properties": [("page", True),  ], },),
            ("view2d.scroll_up",{"type": 'PAGE_UP', "value": 'PRESS', "repeat": True},{"properties": [("page", True),  ], },),
            ("view2d.zoom", {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True}, None),
            ("view2d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
            ("view2d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
            ("view2d.zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True}, None),
            ("view2d.zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True}, None),
            ("view2d.reset", {"type": 'A', "value": 'PRESS', "repeat": True}, None),],},),

#################
# VIEW 3D MODAL #
#################
("View3D Dolly Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CONFIRM", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
            ("CONFIRM", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),],},),

("View3D Fly Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
            ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'LEFTMOUSE', "value": 'ANY', "any": True}, None),
            ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'SPACE', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("ACCELERATE", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("DECELERATE", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("ACCELERATE", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "any": True}, None),
            ("DECELERATE", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "any": True}, None),
            ("CONFIRM", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
            ("PAN_ENABLE", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "any": True}, None),
            ("PAN_DISABLE", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
            ("FORWARD", {"type": 'W', "value": 'PRESS', "repeat": True}, None),
            ("BACKWARD", {"type": 'S', "value": 'PRESS', "repeat": True}, None),
            ("LEFT", {"type": 'A', "value": 'PRESS', "repeat": True}, None),
            ("RIGHT", {"type": 'D', "value": 'PRESS', "repeat": True}, None),
            ("UP", {"type": 'E', "value": 'PRESS', "repeat": True}, None),
            ("DOWN", {"type": 'Q', "value": 'PRESS', "repeat": True}, None),
            ("UP", {"type": 'R', "value": 'PRESS', "repeat": True}, None),
            ("DOWN", {"type": 'F', "value": 'PRESS', "repeat": True}, None),
            ("FORWARD", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("BACKWARD", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("LEFT", {"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("RIGHT", {"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("AXIS_LOCK_X", {"type": 'X', "value": 'PRESS', "repeat": True}, None),
            ("AXIS_LOCK_Z", {"type": 'Z', "value": 'PRESS', "repeat": True}, None),
            ("PRECISION_ENABLE", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("PRECISION_DISABLE", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),
            ("PRECISION_ENABLE", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("PRECISION_DISABLE", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("FREELOOK_ENABLE", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("FREELOOK_DISABLE", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),],},),

("View3D Gesture Circle",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
            ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "repeat": True}, None),
            ("SELECT", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("DESELECT", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
            ("NOP", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),
            ("DESELECT", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
            ("NOP", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
            ("SUBTRACT", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
            ("SUBTRACT", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True}, None),
            ("ADD", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
            ("ADD", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True}, None),
            ("SIZE", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),],},),

("View3D Move Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CONFIRM", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
            ("CONFIRM", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),],},),

("View3D Placement Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("PIVOT_CENTER_ON", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True}, None),
            ("PIVOT_CENTER_OFF", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),
            ("PIVOT_CENTER_ON", {"type": 'RIGHT_ALT', "value": 'PRESS', "any": True}, None),
            ("PIVOT_CENTER_OFF", {"type": 'RIGHT_ALT', "value": 'RELEASE', "any": True}, None),
            ("FIXED_ASPECT_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
            ("FIXED_ASPECT_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("FIXED_ASPECT_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
            ("FIXED_ASPECT_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
            ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
            ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),],},),

("View3D Placement Modal Map",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("NONE", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("NONE", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),
            ("NONE", {"type": 'RIGHT_ALT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("NONE", {"type": 'RIGHT_ALT', "value": 'RELEASE', "any": True}, None),
            ("NONE", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("NONE", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("NONE", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("NONE", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("NONE", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("NONE", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ("NONE", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("NONE", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),],},),

("View3D Rotate Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CONFIRM", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
            ("CONFIRM", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("AXIS_SNAP_ENABLE", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("AXIS_SNAP_DISABLE", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),],},),

("View3D Walk Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CONFIRM", {"type": 'RIGHTMOUSE', "value": 'RELEASE', "any": True}, None),
            ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("FAST_ENABLE", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("FAST_DISABLE", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
            ("SLOW_ENABLE", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("SLOW_DISABLE", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),
            ("FORWARD", {"type": 'W', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("BACKWARD", {"type": 'S', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("LEFT", {"type": 'A', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("RIGHT", {"type": 'D', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("UP", {"type": 'E', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("DOWN", {"type": 'Q', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("FORWARD_STOP", {"type": 'W', "value": 'RELEASE', "any": True}, None),
            ("BACKWARD_STOP", {"type": 'S', "value": 'RELEASE', "any": True}, None),
            ("LEFT_STOP", {"type": 'A', "value": 'RELEASE', "any": True}, None),
            ("RIGHT_STOP", {"type": 'D', "value": 'RELEASE', "any": True}, None),
            ("UP_STOP", {"type": 'E', "value": 'RELEASE', "any": True}, None),
            ("DOWN_STOP", {"type": 'Q', "value": 'RELEASE', "any": True}, None),
            ("FORWARD", {"type": 'UP_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("BACKWARD", {"type": 'DOWN_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("LEFT", {"type": 'LEFT_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("RIGHT", {"type": 'RIGHT_ARROW', "value": 'PRESS', "repeat": True}, None),
            ("FORWARD_STOP", {"type": 'UP_ARROW', "value": 'RELEASE', "any": True}, None),
            ("BACKWARD_STOP", {"type": 'DOWN_ARROW', "value": 'RELEASE', "any": True}, None),
            ("LEFT_STOP", {"type": 'LEFT_ARROW', "value": 'RELEASE', "any": True}, None),
            ("RIGHT_STOP", {"type": 'RIGHT_ARROW', "value": 'RELEASE', "any": True}, None),
            ("GRAVITY_TOGGLE", {"type": 'TAB', "value": 'PRESS', "repeat": True}, None),
            ("GRAVITY_TOGGLE", {"type": 'G', "value": 'PRESS', "repeat": True}, None),
            ("JUMP", {"type": 'V', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("JUMP_STOP", {"type": 'V', "value": 'RELEASE', "any": True}, None),
            ("TELEPORT", {"type": 'SPACE', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("TELEPORT", {"type": 'MIDDLEMOUSE', "value": 'ANY', "any": True}, None),
            ("ACCELERATE", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("DECELERATE", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "any": True, "repeat": True}, None),
            ("ACCELERATE", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "any": True}, None),
            ("DECELERATE", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "any": True}, None),],},),

("View3D Zoom Modal",
    {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {"items":
            [("CONFIRM", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
            ("CONFIRM", {"type": 'ESC', "value": 'PRESS', "any": True, "repeat": True}, None),],},),

################
# WEIGHT PAINT #
################
("Weight Paint",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("paint.weight_paint", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
            ("paint.weight_sample_group", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
            ("brush.scale_size",{"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("scalar", 0.9),], },),
            ("brush.scale_size",{"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},{"properties": [("scalar", 1.1111112),],},),
            ("wm.radial_control",{"type": 'S', "value": 'PRESS'},{"properties": [("data_path_primary", 'tool_settings.weight_paint.brush.size'),("data_path_secondary", 'tool_settings.unified_paint_settings.size'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),("rotation_path", 'tool_settings.weight_paint.brush.texture_slot.angle'),("color_path", 'tool_settings.weight_paint.brush.cursor_color_add'),("fill_color_path", ''),("fill_color_override_path", ''),("fill_color_override_test_path", ''),("zoom_path", ''),("image_id", 'tool_settings.weight_paint.brush'),("secondary_tex", False),], },),
            ("wm.radial_control",{"type": 'U', "value": 'PRESS'},{"properties": [("data_path_primary", 'tool_settings.weight_paint.brush.strength'),("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),("rotation_path", 'tool_settings.weight_paint.brush.texture_slot.angle'),("color_path", 'tool_settings.weight_paint.brush.cursor_color_add'),("fill_color_path", ''),("fill_color_override_path", ''),("fill_color_override_test_path", ''),("zoom_path", ''),("image_id", 'tool_settings.weight_paint.brush'),("secondary_tex", False),], },),
            ("wm.context_toggle",{"type": 'M', "value": 'PRESS'},{"properties": [("data_path", 'weight_paint_object.data.use_paint_mask'),], },),
            ("wm.context_toggle",{"type": 'S', "value": 'PRESS', "shift": True},{"properties": [("data_path", 'tool_settings.weight_paint.brush.use_smooth_stroke'),], },),
            ("blui.right_mouse_navigation", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
            ("wm.call_panel",{"type": 'APP', "value": 'PRESS'},{"properties": [("name", 'VIEW3D_PT_paint_weight_context_menu'),], },),
            ("view3d.select", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
            ("paint.brush_select",{"type": 'D', "value": 'PRESS'},{"properties": [("weight_tool", 'DRAW'),], },),
            ("paint.brush_select",{"type": 'B', "value": 'PRESS'},{"properties": [("weight_tool", 'BLUR'),], },),
            ("wm.tool_set_by_id",{"type": 'I', "value": 'PRESS'},{"properties": [("name", 'builtin.sample_weight'),("cycle", True),], },),
            ("wm.tool_set_by_id",{"type": 'Q', "value": 'PRESS'},{"properties": [("name", 'builtin.select_box'),("cycle", True),], },),],},),

##########
# WINDOW #
##########
("Window",
    {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("wm.batch_rename", {"type": 'RET', "value": 'PRESS', "alt": True, "repeat": True}, None),
            ("wm.read_homefile", {"type": 'N', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.call_menu",{"type": 'O', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},{"properties": [("name", 'TOPBAR_MT_file_open_recent'),  ], },),
            ("wm.open_mainfile", {"type": 'O', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.save_mainfile", {"type": 'S', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.save_as_mainfile", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
            ("wm.quit_blender", {"type": 'Q', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
            ("wm.call_menu",{"type": 'TAB', "value": 'PRESS', "shift": True, "repeat": True},{"properties": [("name", 'SCREEN_MT_user_menu'),  ], },),
            ("wm.call_panel",{"type": 'NDOF_BUTTON_MENU', "value": 'PRESS'},{"properties": [("name", 'USERPREF_PT_ndof_settings'),  ], },),
            ("wm.context_scale_float",{"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS'},{"properties": [("data_path", 'preferences.inputs.ndof_sensitivity'),  ("value", 1.1),  ], },),
            ("wm.context_scale_float",{"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS'},{"properties": [("data_path", 'preferences.inputs.ndof_sensitivity'),  ("value", 0.90909094),  ], },),
            ("wm.context_scale_float",{"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS', "shift": True},{"properties": [("data_path", 'preferences.inputs.ndof_sensitivity'),  ("value", 1.5),  ],},),
            ("wm.context_scale_float",{"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS', "shift": True},{"properties":[("data_path", 'preferences.inputs.ndof_sensitivity'),("value", 0.6666667),],},),
            ("info.reports_display_update", {"type": 'TIMER_REPORT', "value": 'ANY', "any": True}, None),
            ("wm.console_toggle", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "repeat": True}, None),],},),
]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
