import os
from collections import OrderedDict


colors = OrderedDict([
    ("black"  , '\033[30m'),
    ("red"    , '\033[31m'),
    ("green"  , '\033[32m'),
    ("orange" , '\033[33m'),
    ("blue"   , '\033[34m'),
    ("purple" , '\033[35m'),
    ("lightr" , '\033[91m'),
    ("lgreen" , '\033[92m'),
    ("yellow" , '\033[93m'),
    ("pink"   , '\033[95m'),
    ("reset"  , "\033[0m"),
])

underline_colors = OrderedDict([
    ("under_black"  , "\033[4;30m"),
    ("under_red"    , "\033[4;31m"),
    ("under_green"  , "\033[4;32m"),
    ("under_yellow" , "\033[4;33m"),
    ("under_blue"   , "\033[4;34m"),
    ("under_purple" , "\033[4;35m"),
    ("under_cyan"   , "\033[4;36m"),
    ("under_white"  , "\033[4;37m"),
])

colors.update(underline_colors)

class Palette():

    def __init__(
        self,
        colors=colors
    ):
        for key, value in colors.items():
            setattr(self, key, value)


class Pincel(Palette):

    @classmethod
    def pincelada(
        this,
        *args
    ):
        text, color = args
        _c = Pincel()
        reset = _c.reset
        if color in _c.__dict__.keys():
            color = _c.__dict__[color]
            return f"{color}{text}{reset}"
        return text


# el pincel
c = Pincel.pincelada

tic_left  = "<("
tic_right = ")>" 

flecha    =  c("> ", "purple")
optional  =  c(tic_left, "red")

robot     =  c("[", "pink")
robot     += c("*", "blue") + c("_", "red") + c("*", "blue")
robot     += c("]", "pink")

required  =  c(tic_left, "red")
required  += c("required", "under_yellow")
required  += c(tic_right, "red")




        


