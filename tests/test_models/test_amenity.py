#!/usr/bin/python3
"""Defines test class(es) that tests the amenity module."""
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Defines tests for the Amenity class's
        Inherited attributes: id, created_at, and updated_at
        Inherited methods: save() and to_dict()
        State attributes: name
    """
    def test_amenity_inheritance(self):
        """Checks if instances of Amenity inherit from BaseModel."""
        a = Amenity()
        self.assertTrue(isinstance(a, BaseModel))

    def test_amenity_unique(self):
        """Checks if each instance of the Amenity class have unique ids."""
        a = Amenity()
        b = Amenity()
        self.assertFalse(a.id == b.id)

    def test_amenity_datetime_values(self):
        """Tests if the inherited attributes created_at and updated_at contain
           datetime objects."""
        a = Amenity()
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_Amenity_save(self):
        """Tests if the inherited method save() updates updated_at's value."""
        a = Amenity()
        old_time = a.updated_at
        a.save()
        new_time = a.updated_at
        self.assertFalse(old_time == new_time)

    def test_amenity_to_dict(self):
        """Tests if the inherited method to_dict() returns a dictionary contain
           all instance attributes, inherited attributes and the class name."""
        a = Amenity()
        a.number = 50
        diction = a.to_dict()

        self.assertEqual(diction['id'], a.id)
        self.assertEqual(diction['number'], 50)
        self.assertEqual(diction['__class__'], a.__class__.__name__)
        self.assertEqual(diction['created_at'], a.created_at.isoformat())
        self.assertEqual(diction['updated_at'], a.updated_at.isoformat())

    def test_amenity_str(self):
        """Tests the __str__() method's output."""
        a = Amenity()
        cmp_str = "[{}] ({}) {}".format(a.__class__.__name__,
                                        a.id, a.__dict__)
        self.assertEqual(str(a), cmp_str)

    def test_amenity_attr(self):
        """Tests the attributes that are not inherited."""
        a = Amenity()
        self.assertEqual(a.name, "")
        a.__class__.name = "Heat"
        self.assertEqual(a.name, "Heat")


if __name__ == "__main__":
    unittest.main()
