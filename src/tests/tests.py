# -*- coding: utf-8 -*-
# c.s.r

import os
import sqlite3

import components
import torks
import microfilms

from settings import BASE_DIR, STOR_DIR
from torks import 

# This will go in the settings module.
TestStoragesDirectory = os.path.join(STOR_DIR, "test_storages")
TestDatabase = os.path.join(TestStorages, "c_diary_test_db.db")

connection = sqlite3.connect(TestStorage)

connection_curson = connection.cursor()

connection_curson.execute(
    ''' CREATE TABLE entry
        (date text, task text, time real, notes, text)
    ''')

if __name__ == "__main__":


print(connection.close())
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.db = TestDatabase
        self.con

    def cleanUp(self):
        pass 


class TestLoaders(BaseTest, unittest.TestCase):
    

class TestCrudMethods(BaseTest):

    def setUp(self):
        pass

class TestPincel(unittest.TestCase):

    def set