from collections import namedtuple
import csv
from datetime import datetime
from os import system
import re
import sys
sys.path.append("..")

from time import sleep


from colors import (
    c,
    flecha,
    optional,
    required
)
from components import Entry
from views import (
    error_view,
    detail_view,
    create_entry_view,
    success_entry_view,
    update_entry_view,
    deleted_entry_view
)
from settings import FILE
from templates import MARGIN


# Regex
DATE_RE = r"(\d{2})/(\d{2})/(\d{4})"
DATE_RANGE_RE = r"(\d{2})/(\d{2})/(\d{4})-(\d{2})/(\d{2})/(\d{4})"

def wipe():
    """Console screen clearer."""
    
    if sys.platform[:3] == 'win' or sys.platform.startswith('win'):
        system('cls')
    else:
        system('clear')


def catch_display(err):
    """Takes in an error; passes it to error_view."""
    wipe()
    error = str(err).capitalize()
    error_view(error=error)
    input(f'{flecha} ')


def ver_var(var, err_m):
    """
    Check for a value; raise err_m if empty var.
    """
    if var:
        if var != '':
            pass
    else:
        raise Exception(err_m) from None

def validate_date(date, regex):

    try:
        if re.match(DATE_RE, field):
            import pdb
            pdb.set_trace()
            date_group = re.match(DATE_RE, field).group()
            
            to_return  = date_group.split("/")
            
            # degroup
            month = date_group(1).__int__()
            day   = date_group(2).__int_()
            year  = date_group(3).__int__()
            date = datetime(year=year, month=month, day=day)
            
            return '/'.join()
        else:
            raise Exception('Wrong date format') from None
    except ValueError as err:
        raise Exception(err)
    except AttributeError as err:
        raise Exception(err)


def date_field():
    """Get date; validate."""
    out_text = '{} {}'.format(c("Date required", "under_white"), flecha)
    field = input(out_text)
    


def string_field(required=True, place_holder=False):
    """
    Get a string sequence
    """
    if required == True:
        
        if place_holder:
            place_holder = c(place_holder, "underwhite")
            out_text = f'{place_holder} {required} {flecha} '
        else:
            place_holder = c("String field")
            out_text = f"{place_holder} {required} {flecha} "
        
        field = input(out_text)
        try:
            if re.search(r'[\w\d]+', field).group():
                return field
        except AttributeError:
            return string_field(required=required, place_holder=place_holder)

    elif required == False:
        
        if place_holder:
            place_holder = c(place_holder, "underwhite")
            out_text = f'{place_holder} {optional} {flecha} '
        else:
            place_holder = c("String field", "under_white")
            out_text = f"{place_holder} {optional} {flecha}"
        
        field = input(out_text)
        try:
            if re.match(r'^\s*$', field).group():
                return field
        except AttributeError:
            return "<Field empty>"

    return False


def minutes_field():
    """
    Get minutes
    """
    minutes = input(f'Time (rounded minutes) {flecha} ')
    if not re.match(r'^\d*$', minutes.strip()):
        raise Exception(f'Rounded minutes only, e.g. {flecha} 20')
    return minutes


def create_entry(**kwargs):
    """
    create_entry(retrn='only_post') will only post context to csv
    create_entry(retrn='all') will return all without posting.
    """
    if 'return' in kwargs:
        
        return_option = kwargs['return']

        date = date_field()

        task = string_field(
            required=True,
            place_holder=c("Task", "under_white") + flecha
        )

        time = minutes_field()

        notes = string_field(
            required=False,
            place_holder=c("Notes", "under_white") + flecha
        )

        contexto = {
            'date' : date,
            'task' : task,
            'time' : time,
            'notes' : notes
        }

        if return_option == 'only_post':
            # Give the file to post only
            contexto['file'] = FILE
            # save the context
            Entry.save(**contexto)

            return True

        elif return_option == "all":
            return [v for v in context.values()]
        
        return False


def update_entry(file, to_update, trick):
    """ 
    Reads, iterates, makes one row update to a csv file
    """
    with open(file, 'r', newline='') as relayer:
        reader = csv.reader(relayer, delimiter=',')
        list_reader = [x for x in reader]
    target = list_reader.index(to_update)

    copy_list = list_reader.copy()
    to_replace = copy_list.pop(target)
    copy_list.insert(target, trick)
    
    with open(file, 'w', newline='') as deadrop:
        writer = csv.writer(deadrop, delimiter=',')
        for row in copy_list:
            writer.writerow(row)


def delete_entry(file, to_delete):
    """
    Deletes a to_delete row from a csv file.
    """
    with open(file, 'r', newline='') as relayer:
        reader = csv.reader(relayer, delimiter=',')
        list_reader = [x for x in reader]

    target = list_reader.index(to_delete)
    copy_list = list_reader.copy()
    to_delete = copy_list.pop(target)

    with open(file, 'w', newline='') as deadrop:
        writer = csv.writer(deadrop, delimiter=',')
        for row in copy_list:
            writer.writerow(row)


def enumerate_matches(matches):
    """
    Takes a list of matches, enumerates it, returns a choice for the
    match.
    """
    try:
        Line = namedtuple("Line", ["date", "name"])

        matches = [match[:2] for match in matches]
        print(f"Number\tName\tDate\n{MARGIN}")
        for each in enumerate(map(Line._make, matches)):
            index   = c(each[0], "blue")
            name    = c(each[1].name.capitalize(), "pink")
            date    = c(each[1].date, "red") 
            line    = f"<{index}> <{name}> <{date}>"
            print(line + "\n")

        print("[*] [Ctrl] + [c] -> back")
        match_num = input(f'\nTask number {flecha} ')
        if re.match(r'^[0-9]*$', match_num).group():
            if 0 <= int(match_num) <= len(matches): 
                return match_num
            raise Exception('Invalid entry number') from None

    except AttributeError:
        raise Exception("Can't verify the input") from None


def paginate_entries(to_paginate, position):
    """
    Takes a list to paginate from, and a position
    (index), a list item to begin paginating from.
    """
    index = int(position)
    while True:
        try:
            wipe()
            entry = to_paginate[index]
            context = {
                'date' : entry[0],
                'task' : entry[1],
                'time' : entry[2],
                'notes' : entry[3],
                'entry_index' : index,
                'total_entries' : len(to_paginate) - 1
            }
            detail_view(**context)
            move = input(flecha + " ")
            if move.lower() == 'u':
                wipe()
                update_entry_view(to_update=context["task"])
                to_replace_with = create_entry('all')
                update_entry(FILE, to_paginate[index], to_replace_with)
                wipe()
                success_entry_view(task=context["task"])
                input(' > ')
                break
            if move.lower() == 'd':
                wipe()
                to_delete = [hop for hop in context.values()][:4]
                delete_entry(FILE, to_delete)
                deleted_entry_view(entry_name=to_delete[1])
                input(' > ')
                break
            if move.lower() == 'n':
                index += 1
                if index > len(to_paginate) - 1:
                    index = len(to_paginate) - 1
            elif move.lower() == 'p':
                index -= 1
                if index < 0:
                    index = 0
            else:
                print(' Invalid option.')
                sleep(0.5)
                pass
        except NameError as err:
            catch_display(err)
            break
        except IndexError as err:
            catch_display(err)
            break
        except KeyboardInterrupt:
            raise KeyboardInterrupt()


def get_range_dates_matches(file):
    """
    Gets a range of dates, validates it.
    """
    entries = Entry.retreive(file=file)
    
    if entries and len(entries) <= 0:
        raise Exception( 'No entries to display') from None
    
    search_range = input(' from date-to date <required> ')
    match = re.match(
            pattern=r'^\d{2}/\d{2}/\d{4}[-]\d{2}/\d{2}/\d{4}$',
            string=search_range
        ).group()
    
    if match:
        low, high = match.split('-')
        low_m, low_d, low_y = [int(_) for _ in low.split('/')]
        high_m, high_d, high_y = [int(_) for _ in high.split('/')]
    else:
        raise Exception('Regex, no match')
    
    low = datetime(year=low_y, month=low_m, day=low_d)
    high = datetime(year=high_y, month=high_m, day=high_d)
    
    if low > high: low, high = high, low
    
    matches = []
    for note in entries:
        month, day, year = note[0].split('/')
        month, day, year = int(month), int(day), int(year)
        date_to_evaluate = datetime(year=year, month=month, day=day)
        if low <= date_to_evaluate <= high:
            matches.append(note)

    if len(matches) >= 1:
        return matches
    raise Exception('No matches.') from None


def get_date_only(file):
    """
    Gets one date only from the csv db.
    """
    entries = Entry.retreive(file=file)
    date = date_field()
    matches = [x for x in entries if x[0].__contains__(date)]
    if matches:
        return matches        
    raise Exception('No matches') from None


def get_pattern_search(file):
    """
    For every value of rows at joined cols:
    1 (title) and 3 (description) match the given pattern.
    """
    target = input(
        ' * To match an empty field enter: Field empty\n\n'
        ' Pattern (case sensitive) > '
    )
    if not re.match(r'^\s*$', target):
        targets = Entry.retreive(file=file)
        hits = [
            x for x in targets if re.search(
            pattern=r'{}'.format(target), string=''.join(x[1]+x[3])
            )
        ]
        if hits: return hits

    raise Exception('No matches for pattern %s'%(target)) from None

