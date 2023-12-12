#!/usr/bin/python3
"""Defines test class(es) that tests the functionality of the file_storage
   module linked with the BaseModel class."""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """Defines tests that tests the FileStorage class's from an instance of
       BaseModel class and storage which is an instance of FileStorage.
       Instance methods: all(), new(), save(), and reload()
    """
    def test_same(self):
        """Checks if the instance of the BaseModel class when saved to and
           reloaded from storage remains the same."""
        a = BaseModel()
        store = FileStorage()
        a.save()
        b = store.all()
        key = "BaseModel." + a.id
        self.assertEqual(a.to_dict(), b[key].to_dict())
        self.assertEqual(str(a), str(b[key]))
        self.assertTrue(a is b[key])

    def test_persistence_storage(self):
        """Test the save and reload methods in FileStorage and save in
           BaseModel."""
        a = BaseModel()
        store = FileStorage()
        my_id = a.id
        store.save()
        store.reload()
        key = "BaseModel." + my_id
        objs = store.all()
        self.assertTrue(key in objs)

        b = BaseModel()
        b.name = "Ezekiel"
        b.save()
        store.reload()
        key = "BaseModel." + b.id
        objs = store.all()
        self.assertEqual(b.name, objs[key].name)


if __name__ == "__main__":
    unittest.main()
