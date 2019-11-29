from sys import path
path.append("..")

from creative.colors import c


class Menu:

    def __init__(self, main_choices=None):
        # set the main choices.
        if main_choices and len(main_choices) >= 1:
            self.main_choices = main_choices
        # if no choices, there is none.
        else:
            self.main_choices = None


    def menu_choice(self):
        """Gets a menu choice for the given menu main_choices"""

        # set strings for messages.
        text    = c("Option number", "under_white")
        pointer = c(">", "pink")
        ticker  = c("<(:)>", "pink")
        error_ticker = c("<(!)>", "lightr")
        choices = ", ".join(self.main_choices)
        choice  = input(f"{ticker} {text} {pointer} ")
        # try to see if the choice is in the list of choices.
        try:
            if choice and choice in self.main_choices:
                self.current_choice = choice
            else:
                raise
        except Exception:
            # if not then error message and try again.
            error_message = f"\n{error_ticker} Choices available {choices}\n" 
            print(error_message)
            self.menu_choice()