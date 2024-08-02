#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class for serializing and deserializing instances to/from
    a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    __ab_classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def all(self):
        """ Returns the dictionary with all objects of a specific class.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id.
        """
        FileStorage.__objects.setdefault(f"{obj.__class__.__name__}.{obj.id}",
                                         obj)

    def save(self):
        """ Serializes __objects to the JSON file.
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump({key: value.to_dict() for key, value in
                      FileStorage.__objects.items()}, f)

    def reload(self):
        """ Deserializes the JSON file to __object
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                s_dict = json.load(f)
                for key, value in s_dict.items():
                    cls_name = key.split('.')[0]
                    if cls_name in FileStorage.__ab_classes:
                        obj = FileStorage.__ab_classes[cls_name](**value)
                        self.new(obj)
        except Exception:
            pass
