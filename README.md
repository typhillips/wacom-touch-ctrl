# wacom-touch-ctrl
A simple Python program to disable touch control for Wacom tablets. Includes a bash script to launch it. The device ID for the 'Touch' parameter is automatically detected so the program works correctly regardless of the connected USB port.

Requirements:
* Python 2.7 or 3.x
* 'future' module: <http://python-future.org/>
* 'xsetwacom' package: <https://github.com/linuxwacom/xf86-input-wacom/wiki/xsetwacom>

Currently this has only been tested with a Wacom Bamboo Craft tablet but should theoretically work with any tablet supported by xsetwacom.
