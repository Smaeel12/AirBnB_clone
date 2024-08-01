import json
from models.base_model import BaseModel
from models.user import User
""" Serializes instances to a JSON file and deserializes JSON file to instances
"""


class FileStorage:
    """ A class that serializes instances to a JSON file and deserializes JSON
    file to instances
    Attributes:
        __file_path(string): path to the JSON file
        __objects(dictionary): Stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {} 
    __avaliable_classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """ Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects.setdefault(f"{obj.__class__.__name__}.{obj.id}",
                                         obj)

    def save(self):
        """ Serializes __objects to the JSON file
        """
        with open(self.__file_path, "w") as f:
            json.dump({key: value.to_dict() for key, value in
                       self.__objects.items()}, f)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = key.split('.')[0]
                    if cls_name in self.__available_classes:
                        self.__objects[key] = self.__available_classes[cls_name](**value)
        except Exception:
            pass
