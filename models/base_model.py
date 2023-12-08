#!/usr/bin/python3
"""Defines the base class that all other classes in this project inherit from
directly or indirectly."""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Defines the attributes and methods used for serialisation and
    deserialisation of classes."""
    def __init__(self, *args, **kwargs):
        """Initialises the instance attributes with the arguments passed to
           the class during object creation or without."""
        if kwargs or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of an instance."""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance."""
        diction = self.__dict__.copy()
        diction['__class__'] = self.__class__.__name__
        diction['created_at'] = self.created_at.isoformat()
        diction['updated_at'] = self.updated_at.isoformat()

        return diction
