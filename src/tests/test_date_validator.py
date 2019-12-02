import sys
import unittest
sys.path.append("..")

from validators.validators import validate_date


class TestDateFieldValidator(unittest.TestCase):

    def setUp(self):
        """Set up intial values"""
        self.invalid_date_format   = "13/24/2019"
        self.incorrect_date_format = "1/24/2019"
        self.correct_date_format   = "09/24/2009"


    def test_date_field_with_ok_date_format_but_invalid_date(self):
        """Test the date field with an ok date format but an invalid date
        must raise value error at the time of datetime construction."""
        with self.assertRaises(ValueError):
            validate_date(self.invalid_date_format)


    def test_date_field_with_ok_date_format_and_valid_date(self):
        """Test the date with an ok date format and valid date"""
        valid_date = validate_date(self.correct_date_format)
        self.assertEquals(self.correct_date_format, valid_date)
        

    def test_date_field_with_not_ok_date_format(self):
        """Test the date field validator with not an ok date format."""
        with self.assertRaises(AttributeError):
            validate_date(self.incorrect_date_format)


if __name__ == "__main__":
    unittest.main()