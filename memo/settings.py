# -*- coding: utf-8
# csr

import os
from datetime import datetime
import sys
import time
import warnings

from components import Menu
from colors import c
import loaders

# Shortcuts
NODE = loaders.load_login()
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
STOR_DIR = os.path.join(BASE_DIR, 'storages')
FILE = loaders.load_storage(sys.argv)

# MENUS
main_menu = Menu(main_choices=['1', '2', '3', '4'])
date_search_menu = Menu(main_choices=['1', '2', '3'])
search_menu = Menu(main_choices=['1', '2', '3', '4', '5', '6'])
