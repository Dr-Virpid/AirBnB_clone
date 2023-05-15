#!/usr/bin/python3
"""Write a class User that inherits
 from BaseModel"""

from models.basee_model import BaseModel


class User(BaseModel):
    """create a user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
