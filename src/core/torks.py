from collections import namedtuple
import csv
from datetime import datetime
from os import system
import re
import sys
sys.path.append("..")

from time import sleep

from creative.colors import (
    c,
    flecha,
    optional,
    required
)
from storages.droppers import Entry
from templates.views import (
    error_view,
    detail_view,
    create_entry_view,
    success_entry_view,
    update_entry_view,
    deleted_entry_view
)
from config.settings import FILE
from templates.templates import MARGIN
from validators.validators import validate_date


DATE_RE = r"(\d{2})/(\d{2})/(\d{4})"
DATE_RANGE_RE = r"(\d{2})/(\d{2})/(\d{4})-(\d{2})/(\d{2})/(\d{4})"


def wipe():
    """Console screen clearer."""
    # if the platform is windows
    if sys.platform[:3] == 'win' or sys.platform.startswith('win'):
        # use cls to clear the command line screen
        system('cls')
    # otherwise
    else:
        # just clear
        system('clear')


def catch_display(err):
    """Takes in an error; passes it to error_view."""
    # wipe the screen
    wipe()
    # make the error
    error = str(err).capitalize()
    # pass it to the error view and call it
    error_view(error=error)
    # spot an input to hold execution
    input(f'{flecha} ')


def ver_var(var, err_m):
    """Check for a value; raise err_m if empty var."""
    # this functions sucks, send to the merovingian.
    if var:
        if var != '':
            pass
    else:
        raise Exception(err_m)


def date_field():
    """Get date; validate."""
    # format prompt message.
    out_text = '{} {}'.format(c("Date required", "under_white"), flecha)
    # get the input.
    field = input(out_text)
    # try to validate the input as a date
    try:
        validate_date(field)
    # except a date error.
    except ValueError as o_o:
        o_o = c(o_o, "lightr")
        print(o_o)
        date_field()
    # except a format error.
    except AttributeError as e_e:
        e_e = c(e_e, "lightr")
        print(e_e)
        date_field()

    

def string_field(required=True, place_holder=False):
    """Get a string sequence"""
    # if the field is required
    if required == True:
        # then, if there is a place holder for the prompt message.
        if place_holder:
            # color it white and
            place_holder = c(place_holder, "underwhite")
            # format it
            out_text = f'{place_holder} {required} {flecha} '
        # otherwise
        else:
            # just show required
            out_text = f"{required} {flecha} "
        # and ask for input.
        field = input(out_text)
        # If there is match for this search to the field.
        if re.search(r'[\w\d]+', field):
            # return the field
            return field
        # otherwise try again.
        return string_field(required=required, place_holder=place_holder)
    # if the field is not required
    elif required == False:
        # if there is a placeholder
        if place_holder:
            # color the text white
            place_holder = c(place_holder, "underwhite")
            out_text = f"{place_holder} {optional} {flecha}"
        # otherwise
        else:
            # show an optional field prompt
            out_text = f"{optional} {flecha}"
        # get input
        field = input(out_text)
        # if the input is not just space, return it
        if not re.match(r'^\s*$', field)
            return field
        # otherwise return a field empty string.
        return "<Field empty>"
    # if something else just return false.
    return False


def minutes_field():
    """Get minutes"""
    # get time from the command prompt
    minutes = input(f'Time (rounded minutes) {flecha} ').strip()
    # if minutes is not a sequence of digits
    if not re.match(r'^\d*$', minutes):
        # recursion
        minutes_field()
    # otherwise return minutes.
    return minutes


def create_entry_helper():
    """Asks for input and makes a context"""
    task_place_holder = c("Task", "under_white") + flecha
    note_place_holder = c("Notes", "under_white") + flecha
    date  = date_field()
    task  = string_field(required=True, place_holder=task_place_holder)
    time  = minutes_field()
    notes = string_field(required=False,place_holder=note_place_holder)
    return {'date' : date, 'task' : task, 'time' : time, 'notes' : notes}


def create_entry(**kwargs):
    contexto = {}
    # if there is a keyword in the arguments by the name of option
    if 'option' in kwargs:
        # then we set the configuration for how to return a value.
        return_option = kwargs['option']
    # otherwise
    else:
        # raise this to the error view.
        raise Exception("we need an option")
    # if the option is to only post, check for a file to post.
    if return_option == 'only_post':
        # if the file is not given as kwargs
        if 'file' not in kwargs:
            # raise that we need a file to post.
            contexto['file'] = FILE
    # create the entry.
    entry = create_entry_helper()
    # update the contexto with the entry.
    contexto.update(**entry)
    # if the return option is 'only_post'
    if return_option == 'only_post':
        # save the contexto and return True.
        Entry.save(**contexto)
        return True
    # otherwise if the return option is all
    elif return_option == "all":
        # then just return the contents of the context in a list.
        return [v for v in context.values()]
    # else just return false, something failed.
    return False


def update_entry(file, to_update, trick):
    """Reads replaces and writes."""
    # This is a sad story.
    with open(file, 'r', newline='') as relayer:
        # the reader reads the message,
        reader = csv.reader(relayer, delimiter=',')
        # copy from the reader
        list_reader = [x for x in reader]
    # the target is the index of the story to update, target is a number.
    target = list_reader.index(to_update)
    # make a copy of the first copy that the reader made.
    copy_list = list_reader.copy()
    # pop the target, using the number.
    copy_list.pop(target)
    # replace it using index number 'target'
    copy_list.insert(target, trick)
    # now open the file.
    with open(file, 'w', newline='') as deadrop:
        # write what just went down.
        writer = csv.writer(deadrop, delimiter=',')
        # read the copy list
        for row in copy_list:
            # write the row.
            writer.writerow(row)


def delete_entry(file, to_delete):
    """Deletes a to_delete row from a csv file."""
    # open this file and pass the message to the relayer
    with open(file, 'r', newline='') as relayer:
        # read the file
        reader = csv.reader(relayer, delimiter=',')
        # make a copy of the lines as rows inside an array.
        list_reader = [x for x in reader]
    # grab the index as a target of which to delete
    target = list_reader.index(to_delete)
    # copy the list.
    copy_list = list_reader.copy()
    # just pop it, don't save it.
    to_delete = copy_list.pop(target)
    # open to write.
    with open(file, 'w', newline='') as deadrop:
        # writer
        writer = csv.writer(deadrop, delimiter=',')
        # for each row in the list that got popped
        for row in copy_list:
            # write it to a file.
            writer.writerow(row)


def enumerate_matches(matches):
    """Takes a list of matches, enumerates it, returns a choice for the
    match.
    """
    # Represents a line option.
    Line = namedtuple("Line", ["date", "name"])
    # index for match in each of the matches.
    matches = [match[:2] for match in matches]
    # for each match.
    for each in enumerate(map(Line._make, matches)):
        # color the index blue
        index   = c(each[0], "blue")
        # color the name pink
        name    = c(each[1].name.capitalize(), "pink")
        # color the date red
        date    = c(each[1].date, "red") 
        # format the string
        line    = f"<{index}> <{name}> <{date}>"
        # print it.
        print(line + "\n")

    try:
        # print how to exit
        print("[*] [Ctrl] + [c] -> back")
        # prompt the user to enter a number for the corresponding match
        match_num = input(f'\nTask number {flecha} ')
        # if the input ia digit
        if re.match(r'^[0-9]*$', match_num):
            # if zero is less than the number and the number is less
            # than or equal to the len of the matches.
            if 0 <= int(match_num) <= len(matches): 
                # the input does not hit constraints.
                return match_num
            # raise an exeption if the number is invalid, this shoulde be a recusive message.
            raise Exception('Invalid entry number') from None
        # otherwise if the input is not a 
        else:
            raise Exception("Can't verify the input") from None


def paginate_entries(to_paginate, position):
    """Takes a list to paginate from, and a position
    (index), a list item to begin paginating from."""
    # this is where we start pagination
    index = int(position)
    # intialize loop
    while True:
        try:
            wipe()
            # get the entry to which we are going to begin paginating
            entry = to_paginate[index]
            # make a context from the entry to show.
            context = {
                'date' : entry[0],
                'task' : entry[1],
                'time' : entry[2],
                'notes' : entry[3],
                'entry_index' : index,
                'total_entries' : len(to_paginate) - 1
            }
            # pass that context to the detail view.
            detail_view(**context)
            # make a choice
            move = input(flecha + " ")
            # if the lowered version of move is 'u'
            if move.lower() == 'u':
                wipe()
                # call update entry view with the to_update as the name of the task to update.
                update_entry_view(to_update=context["task"])
                # to replace with is a create entry call that returns all in a context
                to_replace_with = create_entry('all')
                # we now update the entry so we pass the file, the entry to update, and what to replace it with.
                update_entry(FILE, to_paginate[index], to_replace_with)
                wipe()
                # success view is the 
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
    """Gets a range of dates, validates it."""
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
    
    if low > high:
        low, high = high, low
    
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
    """Gets one date only from the csv db."""
    date    = date_field()
    entries = Entry.retreive(file=file)
    matches = [x for x in entries if x[0].__contains__(date)]
    if matches:
        return matches
    raise Exception('No matches') from None


def get_pattern_search(file):
    """For every value of rows at joined cols:
    1 (title) and 3 (description) match the given pattern."""
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

