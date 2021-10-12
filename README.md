# BLUi - Blender Unreal Interface

![BLUi Splash](https://github.com/SpectralVectors/BLUI/blob/main/splash.png)

## What is BLUi?

BLUi is an Application Template for Blender.

An App Template is a package that combines a theme, keymap, multiple addons, a splash screen, custom preferences and startup file, and more!

The idea is, when you want to move from one workflow into another: 2D Animation, 3D Animation, Game Asset Design, 3D Printing/CAD/CAM Design, Video Editing, Compositing etc, you may find that there are specific addons that work very well in one space, but create conflicts in others, or that you need to change unit scale, disable preferences etc.

With App Templates this becomes a one click operation.

So, what is BLUi? 

It's an App Template that seeks to recreate the ease of use, and general user experience of Unreal Engine, inside of Blender.

Aimed at those who know Unreal and other Industry Standard tools, BLUi adds features like Right Mouse Navigation, Comment Boxes, Unreal nomenclature, and a handful of community addons that immensely benefit the Blender > Unreal workflow.

A customized keymap, based on the Industry Standard, ensures that anyone who feels at home in Unreal Engine won't have to relearn all the basics just to fix a lightmap / UV Layout, navigate the 3D viewport, focus on the active object, pan / zoom / orbit, model, edit or rig a mesh etc. 

## How to Install

[![Install and Use](https://img.youtube.com/vi/fpmzPr1ENCs/0.jpg)](https://www.youtube.com/watch?v=fpmzPr1ENCs)

Download __BLUi.zip__ from the Releases section on the right.

Open __Blender__, and click on the __Blender__ logo in the top left corner.

Select __Install Application Template__.

Navigate to your __Downloads__ and select __BLUI.zip__, the click __Install...__.

To use the template, go to __File > New > BLUI__.

## NOTE

BLUi runs a startup script that will check for a number of community addons, and, if they're not found, download, install and activate them.

The total size is ~40mb, so, depending on the speed of your internet connection, Blender may appear to be frozen for a few minutes!

Please be patient, and, when the addons are all installed, the BLUI splashscreen will appear!

This will only happen if you don't already have the addons installed, and, once they are installed, startup is only a few seconds.

The full list of Community Addons is below:

- Jim Kroovy's Mr Mannequin's Tools
- BleuRaven's Blender for Unreal Engine
- Symstract's Modifier List
- SavMartin's TexTools
- and my own RightMouseNavigation, CommentBox

## Keyboard Shortcuts

![Keymap](/screenshots/BLUI_084_Keymap.png)
_(Courtesy of [Keyboard Layout Editor](http://www.keyboard-layout-editor.com/))_

### Modes
| <kbd>1</kbd> | **Vertex** Mode |
|---:|:---|
| <kbd>2</kbd> | **Edge** Mode |
| <kbd>3</kbd> | **Face** Mode |
| <kbd>4</kbd> | **Object** Mode |
| <kbd>5</kbd> | **Sculpt** Mode |
| <kbd>6</kbd> | **Vertex Paint** Mode |
| <kbd>7</kbd> | **Weight Paint** Mode |
| <kbd>8</kbd> | **Texture Paint** Mode|

### Workspaces

| <kbd>Tab</kbd> | **Search** Menu |
|---:|:---|
| <kbd>Ctrl</kbd>+<kbd>Tab</kbd> | Cycle Workspace Tab **Right** |
| <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Tab</kbd> | Cycle Workspace Tab **Left** |
| <kbd>`</kbd> | Toggle **System Console** |


### Tools - Object

| <kbd>Q</kbd> | Cycle **Select** Tools |
|---:|:---|
| <kbd>W</kbd> | **Move** Tool |
| <kbd>E</kbd> | **Rotate** Tool |
| <kbd>R</kbd> | Cycle **Scale** Tools |
| <kbd>T</kbd> | **Transform** Tool |
| <kbd>D</kbd> | Cycle **Annotation** Tools |
| <kbd>M</kbd> | **Measure** Tool |
| <kbd>C</kbd> | **3D Cursor** |

### Tools - Edit Mesh

| <kbd>Ctrl</kbd>+<kbd>E</kbd> | Cycle **Extrude** Tools |
|---:|:---|
| <kbd>I</kbd> | **Inset Faces** Tool |
| <kbd>Ctrl</kbd>+<kbd>B</kbd> | **Bevel** Tool |
| <kbd>Alt</kbd>+<kbd>C</kbd> | Cycle **Loop Cut** Tools |
| <kbd>K</kbd> | Cycle **Knife/Bisect** Tools |


### 3D Viewport

| <kbd>Right Mouse</kbd> | Viewport **Navigation** & Context Menus |
|---:|:---|
| <kbd>F</kbd> | **Focus** on Selected Object |
| <kbd>F11</kbd>or<kbd>Ctrl</kbd>+<kbd>Space<kbd> | **Maximize** Viewport |
| <kbd>Alt</kbd>+<kbd>Left Mouse</kbd> | **Rotate** View |
| <kbd>Alt</kbd>+<kbd>Middle Mouse</kbd> | **Pan** View |
| <kbd>Alt</kbd>+<kbd>Right Mouse</kbd> | **Zoom** View |
| <kbd>Numpad 5</kbd> | Toggle **Perspective/Orthographic** |
| <kbd>Numpad 0</kbd> | View **Camera** |
| <kbd>Numpad 1</kbd> | View **Front** |
| <kbd>Ctrl</kbd>+<kbd>Numpad 1</kbd> | View **Back** |
| <kbd>Numpad 3</kbd> | View **Right** |
| <kbd>Ctrl</kbd>+<kbd>Numpad 3</kbd> | View **Left** |
| <kbd>Numpad 7</kbd> | View **Top** |
| <kbd>Ctrl</kbd>+<kbd>Numpad 7</kbd> | View **Bottom** |
| <kbd>Numpad 4</kbd> | View **Orbit Left** |
| <kbd>Numpad 6</kbd> | View **Orbit Right** |
| <kbd>Numpad 8</kbd> | View **Orbit Up** |
| <kbd>Numpad 2</kbd> | View **Orbit Down** |
| <kbd>V</kbd> | **Views** Pie Menu |
| <kbd>,</kbd> | **Transform Orientation** Pie Menu |
| <kbd>.</kbd> | **Transform Pivot Point** Pie Menu |
| <kbd>Z</kbd> | Marquee Select **Zoom** |
| <kbd>X</kbd> | Toggle **Snapping** |
| <kbd>Shift</kbd>+<kbd>A</kbd> | **Add Mesh** Menu |
| <kbd>N</kbd> | Show/Hide **Properties Panel** |
  
### Node Editor

| <kbd>Right Mouse</kbd> | Pan View & **Search/Add Nodes** |
  |---:|:---|
| <kbd>Middle Mouse</kbd> | **Cut Connections** |
| <kbd>C</kbd> | **Comment Box** |
| <kbd>Left Mouse Double Click</kbd> | Add **Reroute** Node |
| <kbd>S</kbd>+<kbd>Left Mouse Click</kbd> | Add **Value** Node |
| <kbd>M</kbd>+<kbd>Left Mouse Click</kbd> | Add **Math** Node |
| <kbd>U</kbd>+<kbd>Left Mouse Click</kbd> | Add **Texture Coordinate** Node |
| <kbd>T</kbd>+<kbd>Left Mouse Click</kbd> | Add **Image Texture** Node |
| <kbd>B</kbd>+<kbd>Left Mouse Click</kbd> | Add **Bump** Node |

## Screenshots
### Layout
![1_Layout](/screenshots/1_Layout.png)
### Geometry
![2_Geometry](/screenshots/2_Geometry.png)
### Model / Sculpt
![3_ModelSculpt](/screenshots/3_ModelSculpt.png)
### UV / Texture
![4_UVTexture](/screenshots/4_UVTexture.png)
### Material / Shader
![5_MaterialShader](/screenshots/5_MaterialShader.png)
### Animation
![6_Animation](/screenshots/6_Animation.png)
### Script
![7_Script](/screenshots/7_Script.png)
### File Data
![8_FileData](/screenshots/8_FileData.png)
  
## Known Issues / Bugs
  
1 - If you switch between BLUi and regular Blender without closing Blender first, it can corrupt keymaps. I'm not sure what's causing it yet, it could be that the addons I'm using in my template aren't being unregistered before the Default scene gets loaded, but I haven't been able to fix it, and it's not present if you close Blender and reopen it. 
It can also be fixed by resetting to Factory / Saved Preferences, but of course, that only works if you've already saved your prefs!

2 - The first time you run BLUi, if you don't have the addons pre-installed, the installation process can take some time. Sometimes, if you click File > New > BLUi multiple times without closing Blender, after having performed the first time setup process, it will redownload and install the addons every time. This can be fixed by closing and reopening Blender.

## Ackowledgements & Thanks:
  
Blender Org, Epic Games, Jim Kroovy, Jayanam, falola, RealityRig, deathclonic, Yughues, lateasusual, AnubisMaster, Michael McCann, Wayward Art Company, knekke, cgvirus, Bone Studio, Hellgate94, bandages, Blender Guru, sonnenbrillenbrauchenlicht, Dawid Huczynski, Campbell Barton, Daniel Engler, Wolfen420, NXGEN, WolfinWool, Gamemakin LLC, CG Matter, Royal Skies LLC, Sybren Stuvel, Pablo Vasquez, Darkfall, angjminer, SirSpence, batFinger and all the other contributors at Blender Stack Exchange, where I've spent countless hours, thank you!
  
Roboto-Regular.ttf by Christian Robertson was provided by Google Fonts, under the Apache license.
