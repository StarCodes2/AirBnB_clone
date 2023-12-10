#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """This class inherits from the BaseModel class and defines the attributes
       of a user.

       Class Attributes: email, password, first_name, and last_name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
