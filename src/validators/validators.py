from datetime import datetime
import sys
import re
sys.path.append("..")

from creative.colors import c, flecha, robot


DATE_RE = r"(\d{2})/(\d{2})/(\d{4})"
DATE_RANGE_RE = r"(\d{2})/(\d{2})/(\d{4})-(\d{2})/(\d{2})/(\d{4})"


def validate_date(date):
    # the date does not match the regular expression.
    if not re.match(DATE_RE, date):
        # make an error
        error = c("[!]", "red") + c("invalid date format", "under_white") 
        # raise An attributeError with the message.
        raise AttributeError(error) from None
    # split the date by dash and make a list of integers, to verify
    # datetime wont take strings as parameters.
    month, day, year = list(map(int, date.split("/")))
    # try this.
    try:
        # verify that the date is actually a date.
        datetime(year=year, month=month, day=day)
        return date
    # the datetime throws Value errors with info of where the code went wrong,
    except ValueError as o_o:
        # raise it as o_o
        raise(o_o)
        
