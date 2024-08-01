""" This model contain a class BaseModel that defines all common
attributes/methods for other classes:
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ A class that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ Initialize the class
        Attributes:
            id(str): unique id for each BaseModel instance
            created_at(datetime): Assign with the current datetime when an
            instance is created
            updated_at(datetime): Assign with the current datetime when an
            instance is created and it will be updated every time the object
            changed
        """
        if kwargs:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.fromisoformat(kwargs['created_at'])
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.fromisoformat(kwargs['updated_at'])
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
    
    def __str__(self):
        """ Representation to the class instance
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of the class
        dictionary
        """
        class_name = self.__class__.__name__
        dict_copy = self.__dict__.copy()
        dict_copy.update({'__class__': class_name,
                          'created_at': self.created_at.isoformat(),
                          'updated_at': self.updated_at.isoformat()})
        return dict_copy