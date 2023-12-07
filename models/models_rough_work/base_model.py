#!/usr/bin/python3
"""Defines the base class that all other classes in this project inherit from
directly or indirectly."""
import uuid
from datetime import datetime


class BaseModel():
    """Defines the attributes and methods used for serialisation and
    deserialisation of classes."""
    def __init__(self, *args, **kwargs):
        """Initialises the instance attributes.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v 

    def __str__(self):
        """Returns a string representation of an instance."""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance."""
        diction = self.__dict__.copy()
        diction['__class__'] = self.__class__.__name__
        diction['created_at'] = self.created_at.isoformat()
        diction['updated_at'] = self.updated_at.isoformat()

        return diction
