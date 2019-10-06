# -*- coding: utf-8 -*-
# c.s.r :)

import random

class Rainbow:

    def __init__(self):
        
        self.black   = '\033[30m'

        self.red     = '\033[31m'

        self.green   = '\033[32m'

        self.orange  = '\033[33m'

        self.blue    = '\033[34m'

        self.purple  = '\033[35m'

        self.lightr  = '\033[91m'

        self.lgreen  = '\033[92m'

        self.yellow  = '\033[93m'

        self.pink    = '\033[95m'
        
        self.reset   = "\033[0m"


    @classmethod
    def pincelada(cls, *args):
        
        text, color = args
        
        this_class = Rainbow()

        reset = this_class.reset
        
        if color in this_class.__dict__.keys():

            color = this_class.__dict__[color]

            return "%s%s%s" % (color, text, reset)
        
        return text

# The main brush

c = Rainbow.pincelada



        


