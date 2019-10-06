# -*- coding: utf-8 -*-
"""
Copyright 2019 C. S. R.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
from datetime import datetime
from time import time

from colors import c
from settings import NODE

TIME   = c(str(datetime.now())[:10], "pink")

TITLE  = "<({})> ".format(NODE)

MARGIN = c(('~=' * 25), "blue") + "\n" + "Date: %s" % (TIME)

main_menu_template = lambda: print('''
{title:}
{0:}

{1:}

{2:}

{3:}

{4:}
'''.format(
        MARGIN,
        '<(1)> Create entry',
        '<(2)> Search entries',
        '<(3)> Contribs',
        '<(4)> Quit | Ctl-c',
        title=TITLE,
    )
)


def main_view():
    
    template = main_menu_template
    
    template()

#---------------------------------------------------------#

create_entry_view_template = lambda: print('''
{view_title:}
{0:}

 * Date format MM/DD/YYYY.

 * Required means required.

 * Cancel operation with Ctrl-c
 '''.format(
        MARGIN,
        view_title='{} New entry'.format(TITLE),
    )
)


def create_entry_view():
    ''' Renders the create entry view '''
    render_template = create_entry_view_template
    render_template()

#---------------------------------------------------------#

success_up_template = lambda **black: print('''
{view_title}
{0:}

* Updated -> {old_entry_name} 
  New entry -> {new_entry_name}.
* Ctrl-c -> to exit this view.
'''.format(
        MARGIN,
        view_title='{} Success View'.format(TITLE),
        **black
    )
)


def success_update_view(**kwargs):
    ''' Renders the succes update view '''
    template = success_up_template
    template(**kwargs)

#---------------------------------------------------------#

success_entry_view_template = lambda : print('''
{view_title}
{0:}

Entry saved.

* Ctrl-c to exit view.
* Return | Enter to create another.
'''.format(
        MARGIN,
        view_title="{} Entry Created".format(TITLE)
    )
)


def success_entry_view():
    ''' Renders success entry view '''
    template = success_entry_view_template
    template()

#---------------------------------------------------------#

deleted_entry_template = lambda **glitter: print('''
{view_title}
{0:}

Task: {entry_name} deleted

* Ctrl-c to exit view.
'''.format(
    MARGIN,
    view_title='{} Success View'.format(TITLE),
    **glitter   
    )
)


def deleted_entry_view(**kwargs):
    ''' Renders the delete entry view '''
    template = deleted_entry_template
    template(**kwargs)

#---------------------------------------------------------#

detail_view_template = lambda **rock: print('''
{view_title:}
{0:}

<Date> {date}

<Task> {task}

<Time> {time}

<Notes> {notes}

Entry <({entry_index:})> of {total_entries}

Options:
* To update entry > "u"
* To delete entry > "d"
* To go to next entry > "n"
* To go to previous entry > "p"
* To go back > Ctrl-C
'''.format(
        MARGIN,
        view_title='{} Detail View'.format(TITLE),
        **rock
    )
)


def detail_view(**kwargs):
    ''' Renders the detail view of an entry '''
    template = detail_view_template
    template(**kwargs)

#---------------------------------------------------------#

search_view_template = lambda: print('''
{title:}
{0:}

{task:}

{date:}

{time:}

{exact:}

{pattern:}

{quit:}
 '''.format(
        MARGIN,
        title='{} Search'.format(TITLE),
        task='<(1)> Search by task name.',
        date='<(2)> Search by task date(s).',
        time='<(3)> Search by task time.',
        exact='<(4)> Search by exact search.',
        pattern='<(5)> Search by regex pattern.',
        quit='<(6)> Back | Ctrl-c.',
    )
)


def search_view():
    ''' Renders the search menu view '''
    template = search_view_template
    template()

#---------------------------------------------------------#

date_search_view_template = lambda: print('''
{title:}
{0:}

<(1)> Search by Date.

<(2)> Search by *Range of dates*

<(3)> Back or Ctrl-c
'''.format(
        MARGIN,
        title='{} Search'.format(TITLE),
    )
)


def date_search_view():
    ''' Renders the date search view '''
    template = date_search_view_template
    template()

#---------------------------------------------------------#
date_search_only_template = lambda: print('''
{view_title} Search by Date
{0:}

* Date format > MM/DD/YYYY
* e.g. 03/09/2019
* Ctrl-c exit choices.
'''.format(
    MARGIN,
    view_title=TITLE,
    )
)


def date_search_only_view():
    ''' Renders the date search date only view '''
    template = date_search_only_template
    template()

#---------------------------------------------------------#
date_search_range_dates_template = lambda: print('''
{view_title} Date Range Search
{0:}

* Date format > MM/DD/YYYY-MM/DD/YYYY.
* e.g. 03/09/2019-06/09/2019.
* Ctrl-c exit choices.
'''.format(
    MARGIN,
    view_title=TITLE
    )
)

def date_search_range_dates_view():
    ''' Renders the date search by range view '''
    template = date_search_range_dates_template
    template()

#---------------------------------------------------------#

list_view_template = lambda **kwargs: print('''
{view_title} {title}
{0:}

* Ctrl-c -> back
'''.format(
        MARGIN,
        view_title=TITLE,
        **kwargs,
    )
)


def list_view(**kwargs):
    ''' Renders the list view '''
    template = list_view_template
    template(**kwargs)

#---------------------------------------------------------#

update_entry_template = lambda : print('''
{view_title} Update Entry

{0:}
'''.format(
    MARGIN,
    view_title=TITLE
    )
)


def update_entry_view():
    ''' Renders the update entry view. '''
    template = update_entry_template
    template()

#---------------------------------------------------------#
error_view_template = lambda **kwargs: print('''
{1:}
{0:}

Error > {error}

[Ctrl] + [c] or hit [enter] to return.
'''.format(
        MARGIN,
        '{} Error'.format(TITLE),
        **kwargs,

    )
)


def error_view(**kwargs):
    ''' Renders the error view '''
    template = error_view_template
    template(**kwargs)

#---------------------------------------------------------#

credits_view_template = lambda: print('''
{view_title}
{0:}

* C. S. R.

Ctrl-c or enter -> back
'''.format(
        MARGIN,
        view_title='{} Contribs'.format(TITLE),
    )
)


def credits_view():
    ''' Renders the credits view '''
    template = credits_view_template
    template()
