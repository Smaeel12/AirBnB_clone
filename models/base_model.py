#!/usr/bin/python3


import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            models.storage.new(self)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_cpy = self.__dict__.copy()
        dict_cpy.update({'__class__': type(self).__name__,
                         'created_at': self.created_at.isoformat(),
                         'updated_at': self.updated_at.isoformat()})
        return dict_cpy
