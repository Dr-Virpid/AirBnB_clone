#!/usr/bin/python3
"""
Write a class BaseModel that defines all
common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Basemode class defines all our essetial attributes and method"""

    def __init__(self, *args, **kwargs):
        """this is a constructor of our basemodel class
           *args not used
           **kwargs is a dict
        """
        if kwargs is not None and kwargs != {}:
            for k in kwargs.item():
                if k == "created_at":
                    self.__dict__["craeted_at"] = datetime.strptime(kwargs["craeted_at"], '%d/%m/%y %H:%M:%S')
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], '%d/%m/%y %H:%M:%S')
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """return a valid string representation of our instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
