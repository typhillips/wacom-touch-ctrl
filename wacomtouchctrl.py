# wacomtouchctrl.py
#
# Auto-detects Wacom tablet touch ID regardless of USB port and disables touch control
#
# Copyright 2018 Ty Phillips. All Rights Reserved.
# This program is free software. You can redistribute and/or modify it in
# accordance with the terms of the accompanying license agreement.

#!/usr/bin/env python

from builtins import str
import subprocess

sp_args = ["xsetwacom", "--list"]
info = str(subprocess.check_output(sp_args), 'ascii').splitlines(True)

found = False

for line in info:
	if line.find("touch") > 0 and line.find("id:") > 0:
		found = True
		id = line.split("id:")[1].split()[0]

if found:
	sp_args = ["xsetwacom", "--set", id, "Touch", "off"]
	subprocess.call(sp_args)
	print("Touch disabled (id = %s)" % id)
else:
	print("Error! Confirm tablet is connected and \'xsetwacom\' is installed")
