#!/usr/bin/python3
"""
Write a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""

import datetime
import json
import os


class FileStorage:
    """
    filestorage class helps us to store and manage
    our data using json
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets a key that is equal to class name + id
        and the value is an instane in our empty
        objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Helps us to store or save our data in json
        format"""
        with open(FileStorage.__file_path, "w") as file:
            data = {key: value.to_dict() for key,
                    value in FileStorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file:
            file_dict = json.load(file)
            file_dict = {k: self.classes()[v["__class__"]](**v)
                         for k, v in file_dict.items()}
            FileStorage.__objects = file_dict

    def classes(self):
        """Returns a dictionary of valid
        classes and their references"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}

        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
