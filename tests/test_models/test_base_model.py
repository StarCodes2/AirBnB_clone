#!/usr/bin/python3
"""Defines test class(es) that tests the base_model module."""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Defines tests for the BaseModel class's
        Instance attributes: id, created_at, and updated_at
        Instance methods: save() and to_dict()
    """
    def test_unique(self):
        """Checks if each instance of the BaseModel class have unique ids."""
        a = BaseModel()
        b = BaseModel()
        self.assertFalse(a.id == b.id)

    def test_datetime_values(self):
        """Tests if the instance attributes created_at and updated_at contain
           datetime objects."""
        a = BaseModel()
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_save(self):
        """Tests if the instance method save() updates updated_at's value."""
        a = BaseModel()
        old_time = a.updated_at
        a.save()
        new_time = a.updated_at
        self.assertFalse(old_time == new_time)

    def test_to_dict(self):
        """Tests if the instance method to_dict() returns a dictionary contain
           all instance attributes and the class name."""
        a = BaseModel()
        a.number = 50
        diction = a.to_dict()

        self.assertEqual(diction['id'], a.id)
        self.assertEqual(diction['number'], 50)
        self.assertEqual(diction['__class__'], a.__class__.__name__)
        self.assertEqual(diction['created_at'], a.created_at.isoformat())
        self.assertEqual(diction['updated_at'], a.updated_at.isoformat())

    def test_str(self):
        """Tests the __str__() method's output."""
        a = BaseModel()
        cmp_str = "[{}] ({}) {}".format(a.__class__.__name__,
                                        a.id, a.__dict__)
        self.assertEqual(str(a), cmp_str)


if __name__ == "__main__":
    unittest.main()
