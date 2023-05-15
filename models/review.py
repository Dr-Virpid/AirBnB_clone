#!/usr/bin/python3
"""
creates a class review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    create a class that inherits from
    Basemodell callec Review
    """
    place_id = ""
    user_id = ""
    text = ""
