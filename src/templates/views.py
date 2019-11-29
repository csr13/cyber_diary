from datetime import datetime
from sys import path
path.append("..")

from core.colors import c, robot
from config.settings import NODE
from templates.templates import A, B, MARGIN
from templates.templates import (
    credits_view_template,
    create_entry_template,
    date_search_view_template,
    date_search_only_template,
    date_search_range_dates_template,
    deleted_entry_template,
    detail_view_template,
    error_view_template,
    list_view_template,
    main_menu_template,
    success_entry_view_template,
    success_up_template,
    search_view_template,
    update_entry_template
)


def credits_view():
    x = {
        "margin" : MARGIN,
        "title"  : "Manifesto"
    }
    credits_view_template(**x)


def create_entry_view():
    x = {
        "margin"    : MARGIN,
        "title" : f"{robot} Create new entry"
    }
    create_entry_template(**x)


def date_search_view():
    x = {
        "margin"    : MARGIN,
        "title" : f"{robot} Search by date"
    }
    date_search_view_template(**x)


def date_search_only_view():
    x = {
        "margin"    : MARGIN,
        "title" : f"{robot} Search by exact date"
    }
    date_search_only_template(**x)


def date_search_range_dates_view():
    x = {
        "margin" : MARGIN,
        "title"  : f"{robot} Search by range of dates"
    }
    date_search_range_dates_template(**x)
    

def deleted_entry_view(entry_name):
    x = {
        "margin" : MARGIN,
        "title"  : f"Entry [{entry_name}] deleted"
    }
    deleted_entry_template(**x)


def detail_view(**x):
    entry = x["task"]
    x.update({
        "margin" : MARGIN,
        "title" : f"{robot} Entry <{entry}>"
    })
    detail_view_template(**x)


def error_view(error):
    x = {
        "error" : error,
        "margin" : MARGIN,
        "title" : "Error [*_*]",
    }
    error_view_template(**x)


def list_view(title):
    x = {
        "margin" : MARGIN,
        "title" : title,
    }
    list_view_template(**x)


def main_view(current_storage):
    current_storage = current_storage.split("/")[-1]
    stor_mes = c("Loaded storage", "under_white")
    current_storage = c(current_storage, "pink")
    user = c("Username", "under_white")
    title = c("Diary", "under_white")
    
    x = {
        "margin" : MARGIN,
        "title"  : f"{robot} {title}",
        "node"   : f"{user} ~> {A}{NODE}{B}",
        "storage": f"{stor_mes} ~> {A}{current_storage}{B}",
        "uno"    : c('<(1)> ', "purple") + c('Create entry', "under_white"),
        "dos"    : c('<(2)> ', "purple") + c('Search entries', "under_white"),
        "tres"   : c('<(3)> ', "purple") + c('Notes', "under_white"),
        "cuatro" : c('<(4)> ', "purple") + c('Quit | Ctl-c', "under_white"),    
    }
    main_menu_template(**x)


def search_view():
    """
    Displays the search view. Composes a context menu.
    """
    x = {
        "title" : '%s %s' % (robot, c("Search Menu", "under_white")),
        "margin" : MARGIN
    }
    search_view_template(**x)
    x = {
        "task"    : '<(1)> Search by task name.',
        "date"    : '<(2)> Search by task date(s).',
        "time"    : '<(3)> Search by task time.',
        "exact"   : '<(4)> Search by exact search.',
        "pattern" : '<(5)> Search by regex pattern.',
        "quit"    : '<(6)> Back | [Ctrl] + [c]',
    }
    nums = [v[:5].strip() for v in x.values()]
    opts = [v[5:].strip() for v in x.values()]
    for i in range(len(nums)):
        num = c(nums[i], "pink")
        opt = c(opts[i], "under_white")
        line = f"{num} {opt}\n"
        print(line)


def success_entry_view():
    x = {
        "title"   : robot,
        "margin"  : MARGIN,
    }
    success_entry_view_template(**x)


def success_update_view(**x):
    x.update({"margin" : MARGIN, "title" : f"{TITLE}"})
    success_up_template(**x)


def update_entry_view(to_update):
    x = {
        "margin" : MARGIN,
        "title"  : f"Update entry {to_update}"
    }
    update_entry_template(**x)


