# dumb code

import os
import pathlib
import sys
import warnings

sys.path.append("..")
from creative.colors import c
from creative.banners import usage_banner


def usage():
    print(usage_banner)


def load_login(): 
    """Handles getting the os login name."""   
    try:
        _name = os.uname().nodename
        _colored_name = c(os_name, "pink")
        return _colored_name
    except AttributeError:
        _name = os.getlogin()
        _colored_name = c(_name, "pink")
        return _colored_name
    else:
        _deafult = c("Be nice", "pink") 


def load_storage(argv):
    """Load a storage for the diary"""
    from config.settings import MAIN_STORAGE_DIR # avoid circular imports.
    try:
        _love = argv[1] # storage name.
        _heart_check = _love[:-4] # storage format.

        if not _love == "default" and not _heart_check == ".csv":
            _error = "[!] love story must be csv"
            _pretty_error = c(_error, "red")
            warnings.warn(_pretty_error)
            exit(1)
        elif love == "default":
            love_storage = os.path.join(MAIN_STORAGE_DIR, "default.csv")
        else:
            love_storage = os.path.join(MAIN_STORAGE_DIR, love)

        if not os.path.exists(love_storage):
            _error = f"[!] creating love story: {love_storage}"
            _pretty_error = c(_pretty_error, "pink")
            open(love_storage, "w").close()
            return love_storage

        return love_storage

    except IndexError:
        _error = "[!] usage: python<version> engine.py <storage>"
        _pretty_error = c(_error, "red")
        warnings.warn(_pretty_error)
        exit(0)
