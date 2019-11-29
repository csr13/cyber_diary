import re


DATE_RE = r"(\d{2})/(\d{2})/(\d{4})"
DATE_RANGE_RE = r"(\d{2})/(\d{2})/(\d{4})-(\d{2})/(\d{2})/(\d{4})"

def validate_date(date, regex):

    try:
        if re.match(DATE_RE, date):
            import pdb
            date_group = re.match(DATE_RE, date).group()
            pdb.set_trace()
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
