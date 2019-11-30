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
        _colored_name = c(_name, "pink")
        return _colored_name
    except AttributeError:
        _name = os.getlogin()
        _colored_name = c(_name, "pink")
        return _colored_name
    else:
        _deafult = c("Be nice", "pink") 


def load_storage(argv):
    """Load a storage for the diary"""
    from config.settings import MAIN_STORAGE_DIR 
    try:
        _storage_path = pathlib.Path(MAIN_STORAGE_DIR)
        _name = argv[1] 
        _check = _name[-4:] 
        
        if not _name == "default" and not _check == ".csv":
            _error = "\n[!] storage must be csv"
            _pretty_error = c(_error, "red")
            warnings.warn(_pretty_error)
            return False
        elif _name == "default":
            _storage_file = _storage_path / "default.csv"
        else:
            _storage_file = _storage_path / _name

        if _storage_file.is_file():
            return _storage_file

        _error = f"\n[!] creating storage: {_storage_file}"
        _pretty_error = c(_error, "pink")
        open(_storage_file, "w").close()
        return _storage_path / _storage_file

    except IndexError:
        # this works and is tested
        _error = "\n[!] usage: python<version> engine.py <storage>"
        _pretty_error = c(_error, "red")
        raise UserWarning(_pretty_error)

