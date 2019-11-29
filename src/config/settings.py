import os
import pathlib
import pdb
import sys
sys.path.append("..")

from menu.menu import Menu
from core import loaders

# machine info.
NODE = loaders.load_login()

# Joins
MAIN_DIR         = os.getcwd()
STORAGE_DIR      = os.path.join(MAIN_DIR, "storages")
MAIN_STORAGE_DIR = os.path.join(STORAGE_DIR, "main_storages")
TEST_STORAGE_DIR = os.path.join(STORAGE_DIR, "test_storages")

# Paths
MAIN_PATH         = pathlib.Path(MAIN_DIR)
STORAGE_PATH      = pathlib.Path(STORAGE_DIR)
MAIN_STORAGE_PATH = pathlib.Path(MAIN_STORAGE_DIR)
TEST_STORAGE_PATH = pathlib.Path(TEST_STORAGE_DIR)

if not STORAGE_PATH.exists():
    STORAGE_PATH.mkdir()

if not MAIN_STORAGE_PATH.exists():
    MAIN_STORAGE_PATH.mkdir()

if not TEST_STORAGE_PATH.exists():
    TEST_STORAGE_PATH.mkdir()

FILE = loaders.load_storage(sys.argv)

# menus
main_menu = Menu(main_choices=['1', '2', '3', '4'])
date_search_menu = Menu(main_choices=['1', '2', '3'])
search_menu = Menu(main_choices=['1', '2', '3', '4', '5', '6'])
