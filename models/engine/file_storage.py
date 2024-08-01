import json
from models.base_model import BaseModel
from models.user import User

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

    def __init__(self):
        """init method for FileStorage class"""
        pass

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        s_obj = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(s_obj, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                d_obj = json.load(f)
        except FileNotFoundError:
            return
        for key, value in d_obj.items():
            class_name = key.split('.')[0]
            if class_name in FileStorage.__available_classes:
                obj = FileStorage.__available_classes[class_name](**value)
                FileStorage.new(obj)
