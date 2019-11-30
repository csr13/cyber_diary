import os
import sys
import subprocess
import unittest
sys.path.append("..")


from config import settings
from core import torks
from core import loaders


class TestLoadStorageLoader(unittest.TestCase):
    def setUp(self):
        self.test_location  = settings.TEST_STORAGE_PATH
        self.main_location  = settings.MAIN_STORAGE_PATH
        self.no_option      = ["spoof"]
        self.bad_option     = ["spoof", "blah"]
        self.default_option = ["spoof", "default"]
        self.custom_option  = ["spoof", "test.csv"]


    def test_not_csv(self):
        """Test storage given not csv"""
        self.assertFalse(loaders.load_storage(self.bad_option))


    def test_not_a_file_to_load(self):
        """Test not a parameter to the script as storage"""
        with self.assertRaises(UserWarning):
            loaders.load_storage(self.no_option)


    def test_default_load_file(self):
        """Test that the default storage is created."""
        x = "default.csv"
        y = self.main_location
        z = loaders.load_storage(self.default_option)
        self.assertEquals(y / x, z)
        with self.assertRaisesRegex(Exception, expected_regex=r"^is file$"):
            if z.is_file():
                raise Exception("is file")


    def test_custom_load_file(self):
        a = self.custom_option[1]
        b = self.main_location
        c = loaders.load_storage(self.custom_option)
        self.assertEqual(b / a, c)
        with self.assertRaises(Exception, expected_regex=r"^is file$"):
            if c.is_file():
                raise Exception("is file")


    def tearDown(self):
        """Destroy the sotrages that were created"""
        for storage in self.main_location.iterdir():
            if storage.is_file(): 
                subprocess.run(
                    ["rm", "-f", "-v", str(storage)], 
                    capture_output=True
                )
            else:
                st.rmdir()


if __name__ == "__main__":
    unittest.main()
        