# CS:GO Config

This repo is my personal todo list for how to configure CS:GO on a new machine.

## Installation

There's two ways to install the configs.
One is to copy files to your local Steam folder (recommended), the other one is to setup things manually in game.
The latter is useful at places like Internet cafés where you lack access to the file system.

### Method 1: Copy Files
1. Copy the files from the [cfg folder](cfg) to `C:\Program Files (x86)\Steam\userdata\<steam_id>\730\local\cfg`
  (Replace <steam_id> with your user's Steam id. It's often only one folder to choose from)
2. Set the launch opitions to the following:
   ```
   -console -w 1280 -h 960 -refresh 144 -novid -nojoy +exec autoexec
   ```
   These launch options will do the following:
      * Ensure console is enabled
      * Set the resolution to 1280x960 @ 144 Hz
      * Disable intro video to launch the game faster
      * Disable joystick support to reduce RAM usage
      * Run autoexec.cfg
3. Go to the Nvidia Control Panel -> Display -> Adjust desktop size and position -> 2. Apply the following settings -> Select Full-screen and ensure Refresh rate is 144 Hz
4. Launch the game
5. Enjoy!

### Method 2: In-game

1. Launch the game
2. Copy the content from [bundle.cfg](bundle.cfg), paste it in the in-game console, and hit Enter
3. Go to the video settings
   * Set all details to the highest value
   * Enable multi-core
   * Set MSAA to 8x
   * Disable FXAA
   * Set Texture Filtering Mode to Anisotropic 16x
   * Disable vsync
   * Disable Motion Blur
4. Enjoy!

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
python minify.py .\cfg\autoexec.cfg
```
