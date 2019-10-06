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
import re

from components import Entry
from torks import *
from microfilms import *
from settings import FILE
from settings import (
    date_search_menu,
    main_menu,
    search_menu
)



if __name__ == '__main__':

# -------------------------------------------------------------------------
# Initialize


    while True:

        try:

            wipe()

            main_view()

            main_menu.menu_choice()

        except KeyboardInterrupt:

            break


# -------------------------------------------------------------------------#
# Create entry.


        if main_menu.current_choice == '1':

            while True:

                try:

                    wipe()

                    create_entry_view()

                    create_entry(retrn='only_post')

                    success_entry_view()

                    input(' > ')

                    continue

                except Exception as err:

                    try:

                        catch_display(err)

                        continue

                    except KeyboardInterrupt:

                        continue

                except KeyboardInterrupt:

                    break


# -------------------------------------------------------------------------#
# SEARCH MENU


        elif main_menu.current_choice == '2':

            while True:

                try:

                    wipe()

                    search_view()
                    
                    search_menu.menu_choice()
                
                except KeyboardInterrupt:
                
                    break


#-------------------------------------------------------------------------#
# SEARCH BY NAME


                if search_menu.current_choice == '1':

                    while True:
                    
                        try:
                    
                            wipe()
                    
                            list_view(title='Name Search')
                    
                            name = string_field(required=True,
                                         place_holder='Entry name')
                    
                            ver_var(name, 'Invalid input.')
                    
                            entries = Entry.retreive(file=FILE)
                    
                            ver_var(entries, 'Lack of entries.')

                            matches = [ _ for _ in entries if name in _ ]
                    
                            ver_var(matches, 'No matches')

                            wipe()
                    
                            list_view(title='Name Search')
                    
                            ent_num = enumerate_matches(matches)
                    
                            paginate_entries(matches, ent_num)

                        except Exception as err:
                    
                            try:
                    
                                catch_display(err)
                    
                                continue
                    
                            except KeyboardInterrupt:
                    
                                continue

                        except KeyboardInterrupt:
                    
                            break


#--------------------------------------------------------------------------
# SEARCH BY DATE


                elif search_menu.current_choice == '2':
                    
                    while True:
                    
                        try:
                    
                            wipe()
                    
                            date_search_view()
                    
                            date_search_menu.menu_choice()
                    
                            if date_search_menu.current_choice == '1':
                    
                                wipe()
                    
                                date_search_only_view()
                    
                                matches = get_date_only(FILE)
                    
                                wipe()
                    
                                list_view(title='Date search')
                    
                                match_num = enumerate_matches(matches)
                    
                                paginate_entries(matches, match_num)
                    
                                continue

                            elif date_search_menu.current_choice == '2':
                    
                                wipe()
                    
                                date_search_range_dates_view()
                    
                                matches = get_range_dates_matches(FILE)
                    
                                wipe()
                    
                                list_view(title='Date Range Search')
                    
                                match_num = enumerate_matches(matches)
                    
                                paginate_entries(matches, match_num)
                    
                                continue

                            elif date_search_menu.current_choice == '3':
                    
                                break

                        except Exception as err:
                     
                            try:
                     
                                catch_display(err)
                     
                                continue
                     
                            except KeyboardInterrupt:
                     
                                continue

                        except KeyboardInterrupt:
                     
                            break


#-------------------------------------------------------------------------#
# SEARCH BY TIME


                elif search_menu.current_choice == '3':
                    
                    while True:
                    
                        wipe()
                    
                        try:
                    
                            list_view(title='Time Search',type='time')
                    
                            time = input(' Task time > ')
                    
                            ver_var(time, 'Invalid input')
                    
                            if not re.match(r'^\d*$', time):
                    
                                raise AttributeError(
                                        'Time is recorded as rounded minutes'
                                        ) from None
                    
                            else: pass
                    
                            entries = Entry.retreive(file=FILE)
                    
                            ver_var(entries, 'No entries')
                    
                            matches = [x for x in entries if time in x]
                    
                            ver_var(matches, 'No matches')
                    
                            wipe()
                    
                            list_view(title='Time Search')
                    
                            ent_num = enumerate_matches(matches)
                    
                            paginate_entries(matches, ent_num)

                        except Exception as err:
                    
                            try:
                    
                                catch_display(err)
                    
                                continue
                    
                            except KeyboardInterrupt:
                    
                                continue

                        except KeyboardInterrupt:
                    
                            break


#--------------------------------------------------------------------------
# SEARCH BY EXACT


                elif search_menu.current_choice == '4':
                    
                    while True:
                    
                        wipe()
                    
                        try:
                    
                            list_view(title='Exact Search')
                    
                            exact = string_field(
                                        required=True,
                                        place_holder='Exact match'
                            )
                    
                            ver_var(exact, 'Invalid entry')
                    
                            entries = Entry.retreive(file=FILE)
                    
                            ver_var(entries, 'No entries')

                            matches = [
                                x for x in entries if x[1].__contains__(exact)
                                ] + [
                                x for x in entries if x[3].__contains__(exact)
                                      ]

                            ver_var(matches, 'No entries.')

                            while True:
                    
                                wipe()
                    
                                list_view(title='Exact Search')
                    
                                ent_num = enumerate_matches(matches)
                    
                                paginate_entries(matches, ent_num)
                    
                                break

                        except Exception as err:
                    
                            try:
                    
                                catch_display(err)
                    
                                continue
                    
                            except KeyboardInterrupt:
                    
                                continue

                        except KeyboardInterrupt:
                    
                            break


#-------------------------------------------------------------------------#
# PATTERN SEARCH


                elif search_menu.current_choice == '5':
                    
                    while True:
                    
                        try:
                    
                            wipe()
                    
                            list_view(title='Pattern Search')
                    
                            matches = get_pattern_search(FILE)
                    
                            ver_var(matches, 'No matches')
                    
                            wipe()
                    
                            list_view(title='Pattern Search')
                    
                            match_num = enumerate_matches(matches)
                    
                            paginate_entries(matches, match_num)

                        except Exception as err:
                    
                            try:
                    
                                catch_display(err)
                    
                                continue
                    
                            except KeyboardInterrupt:
                    
                                continue

                        except KeyboardInterrupt:
                    
                            break


#-------------------------------------------------------------------------#
# Exit the menu.


                elif search_menu.current_choice == '6':
                
                    break

        elif main_menu.current_choice == '3':
            
            wipe()
            
            credits_view()
            
            try:
            
                choice = input(' >')
            
            except KeyboardInterrupt:
            
                continue

        elif main_menu.current_choice == '4':
            
            wipe()
            
            exit(0)
