#!/usr/bin/python3
"""test for database storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from os import getenv

class TestDBStorage(unittest.TestCase):
    """fuck test"""
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.last_name = "Hg"
        cls.user.email = "qwerty@hotmail.com"
	cls.user.first_name = "Koa"
        cls.storage = DBStorage()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "Not using db")
    def test_all(self):
        storage = DBStorage()
        storage.reload()
        dict_len = len(storage.all())
        val = State(name="test_all_state")
        val.save()
        storage.save()
        self.assertIs(len(storage.all()), dict_len + 1)
