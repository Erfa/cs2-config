# CS:GO Config

This repo is my personal todo list for how to configure CS:GO on a new machine.
It contains a few things:

* All the cfg files that should be placed in `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg`
* A list of launch options to use
* A todo list for configurations that have to be done in-game and can't be set in a config file
* A tool for creating a minimized version of the cfg files, that can be pasted directly into the console.
This is useful if you want to have your cfg working in some place where you don't have access to the CS:GO folder, like an Internet café.

## Launch Options

These launch options will do the following:
* Ensure console is enabled
* Run autoexec.cfg
* Set the resolution to 1270x960 @ 144 Hz
* Disable intro video to launch the game faster
* Disable joystick support to reduce RAM usage
* Disable preloading to enable faster map load times

```
-console +exec autoexec.cfg -w 1280 -h 960 -refresh 144 -novid -nojoy -nopreload
```

## Other configuration

Some things do not have an easy way to configure in config files.
This is a todo list of those items.

* Graphics cards settings
 - Nvidia Control Panel -> Display -> Adjuset desktop size and position -> 2. Apply the following settings -> Select Full-screen and ensure Refresh rate is 144 Hz

* In-Game Video Settings
 - Set all details to the highest value
 - Enable multi-core
 - Set MSAA to 8x
 - Disable FXAA
 - Set Texture Filtering Mode to Anisotropic 16x
 - Disable vsync
 - Disable Motion Blur

## minify.py

This tool parses your cfg file and outputs a shortened version that can be pasted in your console.

1. Install Python: https://www.python.org/downloads/
2. Open PowerShell:

```powershell
pip install --user virtualenv
python -m virtualenv env
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\env\Scripts\activate
pip install -r requirements.txt
python .\compile.py
```
