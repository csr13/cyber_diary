from sys import path
path.append("..")

from creative.colors import (
    c,
    pointer,
    menu_text,
    ticker,
)

# add this later.
from exceptions.menu_exceptions import (
    NoChoiceException,
    WrongChoiceException
)


class Menu:
    """This class represents a menu that has choices, sets choices, and gets choices
    The logic is left to the application class that is being made."""
    def __init__(self, main_choices=None):
        # if there are main choices, main choices is either an instance of a list
        # or a tuple, and the length of the choices is either one or greater than one
        if main_choices and isinstance(main_choices, (list, tuple)) and \
        len(main_choices) >= 1:
            # set confirgurations
            self.main_choices   = main_choices
            self.string_choices = ", ".join(self.main_choices)
            self.error_message  = "\n{} choices available {}\n".format(
                c("[!]", "red"),
                self.string_choices
            )
        # otherwise
        else:
            # no configurations
            self.main_choices   = None
            self.error_message  = None
            self.string_choices = None
        # the current choice is always none, by default
        self.current_choice     = None


    @property
    def get_current_choice(self):
        """Gets the current choice, useful for the engine"""
        # if there is a choice
        if self.current_choice:
            # return the current choice
            return self.current_choice


    @get_current_choice.setter
    def set_current_choice(self, choice):
        """Sets the current_choice"""
        # if the main choices have been set and the choice is in the choices
        if self.main_choices and choice in self.main_choices:
            # set the current choice
            self.current_choice = choice
        # This is for value checking
        else:
            self.current_choice = None


    def get_choice(self):
        """Get a choice from the user"""
        # prompt for a choice
        choice  = input(f"{ticker} {menu_text} {pointer} ")
        # return the choice
        return choice


    def pick(self):
        choice = self.get_choice()
        if self.current_choice == None:
            self.pick()
        self.set_current_choice(choice)