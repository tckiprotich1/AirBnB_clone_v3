#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine /'
                                    'test_db_storage.py'])

        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None, "DBStorage"
                         "class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1, "DBStorage"
                        "class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        # Create a new instance of a class
        obj = models.User()
        # Add the object to the database
        models.storage.new(obj)
        # Save the database to file
        models.storage.save()
        # Load the database from file
        with open(models.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
# Check that the object is in the loaded data
        obj_dict = obj.to_dict()
        self.assertIn(obj_dict['id'], data['User'].keys())
        self.assertEqual(data['User'][obj_dict['id']], obj_dict)
        storage_get_count
        self.assertEqual(data['User'][obj_dict['id']], obj_dict)

"""
 test objects  instance to the database, then call the get method with its ID, and expect to get back the same instance.
"""
    def test_get_method_with_valid_id(self):
        # Arrange
        db = Database()
        obj = MyObject(id=1, name="test")
        db.add(obj)

        # Act
        result = db.get(MyObject, 1)

        # Assert
        self.assertEqual(result, obj)

    def test_get_method_with_invalid_id(self):
        # Arrange
        db = Database()
        obj = MyObject(id=1, name="test")
        db.add(obj)

        # Act
        result = db.get(MyObject, 2)

        # Assert
        self.assertIsNone(result)

        def setUp(self):
        self.storage = FileStorage()

    def test_count_method_with_valid_class(self):
        # Arrange
        obj1 = MyObject(id=1, name="test1")
        obj2 = MyObject(id=2, name="test2")
        obj3 = MyOtherObject(id=3, name="test3")
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)

        # Act
        result = self.storage.count(MyObject)

        # Assert
        self.assertEqual(result, 2)

