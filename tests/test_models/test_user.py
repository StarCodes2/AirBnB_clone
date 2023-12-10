#!/usr/bin/python3
"""Defines test class(es) that tests the user module."""
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Defines tests for the User class's
        Inherited attributes: id, created_at, and updated_at
        Inherited methods: save() and to_dict()
        User attributes: email, password, first_name, and last_name
    """
    def test_inheritance(self):
        """Checks if instances of User inherit from BaseModel."""
        a = User()
        self.assertTrue(isinstance(a, BaseModel))

    def test_unique(self):
        """Checks if each instance of the User class have unique ids."""
        a = User()
        b = User()
        self.assertFalse(a.id == b.id)

    def test_datetime_values(self):
        """Tests if the inherited attributes created_at and updated_at contain
           datetime objects."""
        a = User()
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_save(self):
        """Tests if the inherited method save() updates updated_at's value."""
        a = User()
        old_time = a.updated_at
        a.save()
        new_time = a.updated_at
        self.assertFalse(old_time == new_time)

    def test_to_dict(self):
        """Tests if the inherited method to_dict() returns a dictionary contain
           all instance attributes, inherited attributes and the class name."""
        a = User()
        a.number = 50
        diction = a.to_dict()

        self.assertEqual(diction['id'], a.id)
        self.assertEqual(diction['number'], 50)
        self.assertEqual(diction['__class__'], a.__class__.__name__)
        self.assertEqual(diction['created_at'], a.created_at.isoformat())
        self.assertEqual(diction['updated_at'], a.updated_at.isoformat())

    def test_str(self):
        """Tests the __str__() method's output."""
        a = User()
        cmp_str = "[{}] ({}) {}".format(a.__class__.__name__,
                                        a.id, a.__dict__)
        self.assertEqual(str(a), cmp_str)

    def test_user_attr(self):
        """Tests the attributes that are not inherited."""
        a = User()
        self.assertEqual(a.email, "")
        self.assertEqual(a.password, "")
        self.assertEqual(a.first_name, "")
        self.assertEqual(a.last_name, "")
        a.email = "anu@gmail.com"
        a.password = "pass"
        a.first_name = "Ezekiel"
        a.last_name = "Anu"
        self.assertEqual(a.email, "anu@gmail.com")
        self.assertEqual(a.password, "pass")
        self.assertEqual(a.first_name, "Ezekiel")
        self.assertEqual(a.last_name, "Anu")


if __name__ == "__main__":
    unittest.main()
