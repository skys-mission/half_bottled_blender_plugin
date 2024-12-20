# -*- coding: utf-8 -*-
# Copyright (c) 2024, https://github.com/skys-mission and SoyMilkWhisky
"""
...
"""
import os
import sys




def unload_pkg():
    """
    ...
    """
    addon_dir = os.path.abspath(os.path.dirname(__file__))
    plib_path = os.path.join(addon_dir, 'plib')
    if plib_path in sys.path:
        sys.path.remove(plib_path)
