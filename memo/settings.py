# -*- coding: utf-8
# c.s.

import os
from datetime import datetime
import sys
import time
import warnings

from components import Menu
from colors import c

try:

    NODE = c(os.uname().nodename, "pink")

except AttributeError:

    NODE = c(os.getlogin(), "pink")


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

STOR_DIR = os.path.join(BASE_DIR, 'storages')


# Storage settings

try:

    if sys.argv[1] == "default":

        FILE = os.path.join(STOR_DIR, "entries.csv")

    else:

        FILE = os.path.join(STOR_DIR, sys.argv[1])

    if not os.path.exists(FILE):

        raise FileNotFoundError() from None

except FileNotFoundError:

    error = "<(Error)> Storage ~> %s not found" % (FILE)

    time.sleep(1)

    print(c(error, "red"))

    fix   = "<(Fix)> Creating storage ~> %s" % (FILE)

    time.sleep(1)

    print(c(fix, "yellow"))

    open(FILE, "w").close()

    done  = "<(Success)> ! New storage created at~> %s" % (FILE)

    print(c(done, "green"))

    time.sleep(3)

    FILE = FILE

except IndexError:

    error = "\nUsage ~> python<version> engine.py <storage>\n"

    print(c(error, "red"))

    sys.exit(1)


# MENUS


main_menu = Menu(main_choices=['1', '2', '3', '4'])

date_search_menu = Menu(main_choices=['1', '2', '3'])

search_menu = Menu(main_choices=['1', '2', '3', '4', '5', '6'])
    
