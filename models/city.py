#!/usr/bin/python3
"""
creates a class to handle
city objects
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    creates the city class
    """
    state_id = ""
    name = ""
