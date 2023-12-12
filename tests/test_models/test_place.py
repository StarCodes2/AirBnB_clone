#!/usr/bin/python3
"""Defines test class(es) that tests the place module."""
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Defines tests for the Place class's
        Inherited attributes: id, created_at, and updated_at
        Inherited methods: save() and to_dict()
        Place attributes: city_id, user_id, name, description, number_rooms,
                         number_bathrooms, max_guest, price_by_night, latitude,
                         longitude, and amenity_ids
    """
    def test_place_inheritance(self):
        """Checks if instances of User inherit from BaseModel."""
        a = Place()
        self.assertTrue(isinstance(a, BaseModel))

    def test_place_unique(self):
        """Checks if each instance of the Place class have unique ids."""
        a = Place()
        b = Place()
        self.assertFalse(a.id == b.id)

    def test_place_datetime_values(self):
        """Tests if the inherited attributes created_at and updated_at contain
           datetime objects."""
        a = Place()
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_place_save(self):
        """Tests if the inherited method save() updates updated_at's value."""
        a = Place()
        old_time = a.updated_at
        a.save()
        new_time = a.updated_at
        self.assertFalse(old_time == new_time)

    def test_place_to_dict(self):
        """Tests if the inherited method to_dict() returns a dictionary contain
           all instance attributes, inherited attributes and the class name."""
        a = Place()
        a.number = 50
        diction = a.to_dict()

        self.assertEqual(diction['id'], a.id)
        self.assertEqual(diction['number'], 50)
        self.assertEqual(diction['__class__'], a.__class__.__name__)
        self.assertEqual(diction['created_at'], a.created_at.isoformat())
        self.assertEqual(diction['updated_at'], a.updated_at.isoformat())

    def test_place_str(self):
        """Tests the __str__() method's output."""
        a = Place()
        cmp_str = "[{}] ({}) {}".format(a.__class__.__name__,
                                        a.id, a.__dict__)
        self.assertEqual(str(a), cmp_str)

    def test_place_attr(self):
        """Tests the attributes that are not inherited."""
        a = Place()
        self.assertEqual(type(a.city_id), str)
        self.assertEqual(type(a.user_id), str)
        self.assertEqual(type(a.name), str)
        self.assertEqual(type(a.description), str)
        self.assertEqual(type(a.number_rooms), int)
        self.assertEqual(type(a.number_bathrooms), int)
        self.assertEqual(type(a.max_guest), int)
        self.assertEqual(type(a.price_by_night), int)
        self.assertEqual(type(a.latitude), float)
        self.assertEqual(type(a.longitude), float)
        self.assertEqual(type(a.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
