import sys
import re
sys.argv("..")

from creative.colors import c, flecha, robot



DATE_RE = r"(\d{2})/(\d{2})/(\d{4})"
DATE_RANGE_RE = r"(\d{2})/(\d{2})/(\d{4})-(\d{2})/(\d{2})/(\d{4})"

def validate_date(date):
    if not re.match(DATE_RE, date):
        error = c("[!]", "red") + c("invalid date format", "under_white") 
        raise AttributeError(error) from None
    to_return  = date_group.split("/")
    month = date_group(1).__int__()
    day   = date_group(2).__int_()
    year  = date_group(3).__int__()
    date = datetime(year=year, month=month, day=day) 
    return '/'.join()

def validate_date_range(date_range):