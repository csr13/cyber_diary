# -*- coding: utf-8 -*-
# csr

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

from datetime import datetime

from colors import c 

A = c("<(", "red")
B = c(")>", "red") 
MARGIN = ((c("~", "purple") + c("=", "red")) * 25 ) 


main_menu_template = lambda **x: print("""
{title}
{margin:}
{node:}
{storage:}

{uno:}

{dos:}

{tres:}

{cuatro:}
""".format(**x))


create_entry_template = lambda **x: print("""
{title:}
{margin}

[*] Date format MM/DD/YYYY.

[*] Cancel operation with Ctrl-c
 """.format(**x))


success_up_template = lambda **x: print("""
{title}
{margin}

* Updated -> {old_entry_name} 
  New entry -> {new_entry_name}.
* Ctrl-c -> to exit this view.
""".format(**x))


success_entry_view_template = lambda **x: print("""
{title} Entry saved.
""".format(**x))


deleted_entry_template = lambda **x: print("""
{title}
{margin}

Task: {entry_name} deleted

* [Ctrl] + [c] to exit view.
""".format(**x))


detail_view_template = lambda **x: print("""
{title}
{margin}

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
* To go back > [Ctrl] + [c]
""".format(**x))


search_view_template = lambda **x: print("""
{title}
{margin}
 """.format(**x))


date_search_view_template = lambda **x: print("""
{title}
{margin}

<(1)> Search by Date.

<(2)> Search by *Range of dates*

<(3)> Back or Ctrl-c
""".format(**x))


date_search_only_template = lambda **x: print('''
{title} Search by Date
{margin}

[*] Date format > MM/DD/YYYY
[*] e.g. 03/09/2019
[*] [Ctrl] + [c] exit choices.
'''.format(**x))


date_search_range_dates_template = lambda **x: print("""
{title} Date Range Search
{margin}

* Date format > MM/DD/YYYY-MM/DD/YYYY.
* e.g. 03/09/2019-06/09/2019.
* Ctrl-c exit choices.
""".format(**x))


list_view_template = lambda **x: print("""
{title}
{margin}""".format(**x))


update_entry_template = lambda **x: print("""
{title}
{margin}
""".format(**x))


error_view_template = lambda **x: print("""
{title}
{margin}

Error > {error}

[Ctrl] + [c] or hit [enter] to return.
""".format(**x))


credits_view_template = lambda **x: print('''
{title}
{margin}

[*] csr

[Ctrl] + [c] or [enter] to exit
'''.format(**x))


