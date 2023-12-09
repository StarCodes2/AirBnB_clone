#!/usr/bin/python3
"""This script defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of user.
        first_name (str): The first name of the user.
        last_name (str): The last name of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
