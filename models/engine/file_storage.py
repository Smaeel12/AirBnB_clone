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
    __file_path: str = 'file.json'
    __objects: dict = {}
    __classes: dict = {'BaseModel': BaseModel,
                       'User': User,
                       'State': State,
                       'City': City,
                       'Amenity': Amenity,
                       'Place': Place,
                       'Review': Review
                       }

    def all(self) -> None:
        """ Returns the dictionary with all objects of a specific class.
        """
        return self.__objects

    def new(self, obj) -> None:
        """ Sets in __objects the obj with key <obj class name>.id.
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self) -> None:
        """ Serializes __objects to the JSON file.
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({key: obj.to_dict()
                      for key, obj in self.__objects.items()}, f)

    def reload(self) -> None:
        """ Deserializes the JSON file to __object
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objs = json.load(f)
            for key, obj in objs.items():
                self.__objects[key] = self.__classes[key.split('.')[0]](**obj)
        except Exception:
            pass
