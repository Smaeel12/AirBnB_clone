#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""
This module defines the BaseModel class, which serves as the base class
for other classes.
"""


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
        Args:
            *args: not used
            **kwargs: each value of this dictionary is the value of
            this attribute name
        """
        if kwargs:
            for key, val in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(val))
                else:
                    if key != '__class__':
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the BaseModel.

        Returns:
            str: A formatted string with class name, ID,
            and dictionary representation.
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """ Update the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing instance attributes
            with proper formatting.
        """
        new_dict = {**self.__dict__, '__class__': self.__class__.__name__}
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
