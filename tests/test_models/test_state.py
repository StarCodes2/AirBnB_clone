#!/usr/bin/python3
"""Defines test class(es) that tests the state module."""
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Defines tests for the State class's
        Inherited attributes: id, created_at, and updated_at
        Inherited methods: save() and to_dict()
        State attributes: name
    """
    def test_state_inheritance(self):
        """Checks if instances of State inherit from BaseModel."""
        a = State()
        self.assertTrue(isinstance(a, BaseModel))

    def test_state_unique(self):
        """Checks if each instance of the State class have unique ids."""
        a = State()
        b = State()
        self.assertFalse(a.id == b.id)

    def test_state_datetime_values(self):
        """Tests if the inherited attributes created_at and updated_at contain
           datetime objects."""
        a = State()
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_state_save(self):
        """Tests if the inherited method save() updates updated_at's value."""
        a = State()
        old_time = a.updated_at
        a.save()
        new_time = a.updated_at
        self.assertFalse(old_time == new_time)

    def test_state_to_dict(self):
        """Tests if the inherited method to_dict() returns a dictionary contain
           all instance attributes, inherited attributes and the class name."""
        a = State()
        a.number = 50
        diction = a.to_dict()

        self.assertEqual(diction['id'], a.id)
        self.assertEqual(diction['number'], 50)
        self.assertEqual(diction['__class__'], a.__class__.__name__)
        self.assertEqual(diction['created_at'], a.created_at.isoformat())
        self.assertEqual(diction['updated_at'], a.updated_at.isoformat())

    def test_state_str(self):
        """Tests the __str__() method's output."""
        a = State()
        cmp_str = "[{}] ({}) {}".format(a.__class__.__name__,
                                        a.id, a.__dict__)
        self.assertEqual(str(a), cmp_str)

    def test_state_attr(self):
        """Tests the attributes that are not inherited."""
        a = State()
        self.assertEqual(a.name, "")
        a.__class__.name = "Anu"
        self.assertEqual(a.name, "Anu")


if __name__ == "__main__":
    unittest.main()
