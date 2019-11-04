# -*- coding: utf-8 -*-
# c.s.r

import os
import unittest

import components
import torks
import microfilms

from settings import BASE_DIR

TS = os.path.join(BASE_DIR, "storages", "test_storage.csv") 

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.ts = TS

    def cleanUp(self):
        pass 


class TestFields():

    def setUp(self):
        pass

    def test_a_string_field(self):
        pass

    def test_b_date_field(self):
        pass

    def test_c_time(self):
        pass


class TestCrudMethods(BaseTest):

    def setUp(self):
        pass

class TestPincel(unittest.TestCase):

    def set