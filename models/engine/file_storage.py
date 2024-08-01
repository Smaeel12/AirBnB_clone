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
    __available_classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """ Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file
        """
        s_obj = {key: value.to_dict() for key, value in
                              self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(s_obj, f)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        d_obj = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                d_obj = json.load(f)
        except FileNotFoundError:
            return
        for key, value in d_obj.items():
            class_name = key.split('.')[0]
            if class_name in self.__available_classes:
                obj = self.__available_classes[class_name](**value)
                self.new(obj)
