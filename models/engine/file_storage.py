#!/usr/bin/python3


import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = '{}.{}'.format(obj.to_dict()["__class__"], obj.to_dict()["id"])
        FileStorage.__objects.setdefault(key, obj)

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: value.to_dict() for key, value in FileStorage.__objects.items()}, f)


    def reload(self):
        try:
            f = open(FileStorage.__file_path, 'r')
        except:
            pass
        else:
            for key, value in json.load(f).items():
                FileStorage.__objects.setdefault(key, BaseModel(**value))
