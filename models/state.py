#!/usr/bin/python3
"""
create a class that handles
state object
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
