#!/usr/bin/python3
"""Defines the class FileStorage that serializes instances to a JSON file
   and deserializes JSON file to instances."""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """Serialize instances to a JSON file amd deserialize JSON file to
       instances."""
    __file_path = "obj_storage.json"
    __objects = {}

    def all(self):
        """Returns the custom dictionary representation of the instances of
           class FileStorage."""
        return self.__class__.__objects

    def new(self, obj):
        """Add the dictionary representation of an object to the private class
           dictionary using <class name>.id as the key."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__class__.__objects[key] = obj

    def save(self):
        """Serializes the dictionary of objects in the class attribute
           __objects and save it in a JSON file."""
        with open(self.__class__.__file_path, 'w', encoding="utf-8") as jf:
            diction = {}
            for key, obj in self.__class__.__objects.items():
                diction[key] = obj.to_dict()
            json.dump(diction, jf)

    def reload(self):
        """Deserializes the JSON file at the path in '__file_path' and sets
           it to '__objects'."""
        if (os.path.exists(self.__class__.__file_path)):
            with open(self.__class__.__file_path, encoding="utf-8") as jf:
                obj_dict = {}
                diction = json.load(jf)
                for key, value in diction.items():
                    obj_dict[key] = eval("{}(**{})".format(value['__class__'],
                                                           value))
                self.__class__.__objects = obj_dict
