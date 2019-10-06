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
import csv

from colors import c


class Menu:

    """

    Menu class.

    Params
    ------

    main_choices       :: list of int choices for the instanciated menu
                           
    -----------------------------------------------------------------------

    Functions
    ---------

    menu_choice :: gets a menu choice from the user; if given choice is the-
    *main* self.choices, it procceds to set it up as the current choice.

    """

    def __init__(self, main_choices=None):

        if main_choices and len(main_choices) >= 1:

                self.main_choices = main_choices

        else:

            self.main_choices = None


    def menu_choice(self):
        ''' Gets a menu choice for the given menu main_choices '''

        ticker  = c("<(:)>", "pink")

        pointer = c(">", "pink")

        choice = input("{} Option number {} ".format(ticker, pointer))

        try:

            if choice and choice in self.main_choices:

                self.current_choice = choice

            else:

                raise

        except Exception:

            error_ticker = c("<(!)>", "lightr")
            print(
                '\n{} Choices available {} \n'.format(
                                                error_ticker,
                                                ', '.join(self.main_choices)
                                                )
                                            )
            # recursion
            self.menu_choice()



class Entry:

    """

    Entry Object to save and retreive from a storage.

    Functions:

    save                :: check the docstring for info.
    retreive            :: check the docstring for info.

    """

    @classmethod
    def save(cls, **kwargs):
        """
        Save the entry to a given file via kwargs.
        """

        if kwargs:

            field_names = []

        if "file" in kwargs and len(kwargs) > 2:

            file = kwargs.get('file')
            
            kwargs.__delitem__('file')

        for key in kwargs.keys():
            
            field_names.append(key)

        with open(file, 'a', newline='') as db:
            
            pincel = csv.DictWriter(db, fieldnames=field_names)
            
            pincel.writerow(kwargs)
            
            return True, '<Entry.create.save >> {}>'.format(file)


    @classmethod
    def retreive(cls, file=None, type='r'):

        """
        Retreives a reader from given file.
        """

        if file and file[-4:] == '.csv':
            
            pass

        else:
            
            raise Exception('Only csv files.') from None

        try:
            
            with open(file, type, newline='') as file:
            
                lector = csv.reader(file, delimiter=',')
            
                return [entry for entry in lector]

        except FileNotFoundError:
            
            raise FileNotFoundError(
                'File: %s not found in cwd' % (file)
            )


