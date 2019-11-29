import csv

class Entry:
 
    @classmethod
    def save(cls, **kwargs):
        """Save the entry to a given file via kwargs."""
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
            raise FileNotFoundError(f"File: {file} not found in cwd") from None


