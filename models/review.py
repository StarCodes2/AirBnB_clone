#!/usr/bin/python3
"""This script defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """This Represents a review.

    Attributes:
        place_id (str): The place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
