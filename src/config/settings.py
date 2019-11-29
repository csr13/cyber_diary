import os
import sys
sys.path.append("..")

from menu.menu import Menu
from core import loaders

# machine info.
NODE = loaders.load_login()

# directories.
# = = = = = = = = = = = = = =

# this dir
# - - - - -
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

# storage directories.
# - - - - - - - - - - -
MAIN_STORAGE_DIR = os.path.join(BASE_DIR, 'storages', "diary")
if not os.path.exists(MAIN_STORAGE_DIR):
    os.mkdir(MAIN_STORAGE_DIR)

TEST_SOTRAGE_DIR = os.path.join(BASE_DIR, "test_storages")
if not os.path.exists(TEST_SOTRAGE_DIR):
    os.mkdir(TEST_SOTRAGE_DIR)

# file
# = = = =

# pass sys.argv, ir contains the storage to load the file from.
FILE = loaders.load_storage(sys.argv)

# menus
main_menu = Menu(main_choices=['1', '2', '3', '4'])
date_search_menu = Menu(main_choices=['1', '2', '3'])
search_menu = Menu(main_choices=['1', '2', '3', '4', '5', '6'])
