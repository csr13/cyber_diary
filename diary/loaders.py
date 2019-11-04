# -*- coding: utf-8 -*-
# csr

import os
import time
import warnings

from colors import c


def usage():
    pass


def load_login(): 
    """
    Handles getting the os login name.
    """   
    try:
        return c(os.uname().nodename, "pink")
    except AttributeError:
        return c(os.getlogin(), "pink")


def load_storage(argv):
    """
    Handles making or setting current storage
    """
    try:
        from settings import STOR_DIR
        if argv[1] == "default":
            storage = os.path.join(STOR_DIR, "entries.csv")
        else:
            storage = os.path.join(STOR_DIR, argv[1])
        if not os.path.exists(storage):
            warnings.warn(c(f"[Fix] Creating storage: {FILE}", "yellow"))
            raise FileNotFoundError() from None
        return storage
    except FileNotFoundError:
        open(storage, "w").close()
        return FILE
    except IndexError:
        print(c("[Usage] : python<version> engine.py <storage>", "red"))
        exit(0)
