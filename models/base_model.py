#!/usr/bin/python3

"""
This module defines the BaseModel class, which serves as the base class
for other classes.
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
        Args:
            *args: not used
            **kwargs: each value of this dictionary is the value of
            this attribute name
        """
        if kwargs:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.fromisoformat(
                    kwargs["created_at"])
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.fromisoformat(
                    kwargs["updated_at"])
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel.

        Returns:
            str: A formatted string with class name, ID,
            and dictionary representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Update the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing instance attributes
            with proper formatting.
        """
        class_name = self.__class__.__name__
        data = self.__dict__.copy()
        data['__class__'] = class_name
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
