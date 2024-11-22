# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyMilkWhisky
"""
This module contains information about the Blender add-on "Whisky Helper".
It provides metadata such as the add-on name, author, version, Blender version compatibility,
location in the Blender UI, description, category, documentation URL, and issue tracker URL.

Attributes:
    addon_name (str): The name of the add-on.
    ADDON_INFO (dict): A dictionary containing detailed information about the add-on.

Functions:
    set_addon_name(name: str): Sets the name of the add-on.
"""

ADDON_INFO = {
    "name": "Whisky Helper",
    "author": "Soy Milk Whisky, github.com/skys-mission",
    "version": (0, 1, 1),
    "blender": (3, 6, 0),
    "location": "View3D > N-Panel  > Whisky Helper",
    "description": "Whisky Helper.",
    "category": "3D View",
    "doc_url": "https://whiskyai.xyz/doc/blender/addon/whisky_helper_for_blender",
    "tracker_url": "https://github.com/skys-mission/whisky_helper_for_blender/issues"
}
