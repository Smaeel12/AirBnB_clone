#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Class documentation -- TO BE ADDED --
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """The method all that returns the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """The method new that sets the key of the dictionary of the objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """The method save that saves the new objects as str in a file"""
        serialized = {}
        for key, val in FileStorage.__objects.items():
            serialized[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(serialized))

    def reload(self):
        """
        The method reload that reloads the dictionary from file and
        creates obj from it
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                loaded = json.loads(f.read())
                class_map = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "Amenity": Amenity,
                    "City": City,
                    "Place": Place,
                    "Review": Review,
                    "State": State
                }
            for key, val in loaded.items():
                cls = key.split('.')[0]
                if cls in class_map:
                    instance_class = class_map[cls]
                    instance = instance_class(**val)
                    self.new(instance)
