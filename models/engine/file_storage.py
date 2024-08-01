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
    __objects = dict()
    __avaliable_classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """ Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects.setdefault(f"{obj.__class__.__name__}.{obj.id}",
                                         obj)

    def save(self):
        """ Serializes __objects to the JSON file
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump({key: value.to_dict() for key, value in
                       FileStorage.__objects.items()}, f)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        try:
            f = open(FileStorage.__file_path, "r")
        except Exception:
            pass
        else:
            for key, value in json.load(f).items():
                if (key.split('.')[0] in FileStorage.__avaliable_classes.keys()):
                    FileStorage.__objects.setdefault(key, \
                    FileStorage.__avaliable_classes[key.split('.')[0]](**value))
