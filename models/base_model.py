#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
import uuid
from datetime import datetime
import models


class BaseModel:

    """
    A class BaseModel that defines all common attributes/methods
    for other classes.
        Public instance attributes:
            - id: string - assign with an uuid when an instance is
            created:
                * you can use uuid.uuid4() to generate unique id but
                    don't forget to convert to a string
                * the goal is to have unique id for each BaseModel
                    - created_at: datetime - assign with the current datetime
                    when an instance is created
            - created_at: datetime - assign with the current datetime
            when an instance is created
            - updated_at: datetime - assign with the current datetime when
            an instance is created and it will be updated every time you
            change your object
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        Public instance methods:
            - save(self): updates the public instance attribute updated_at
            with the current datetime
            - to_dict(self): returns a dictionary containing all keys/values
            of __dict__ of the instance:
                * by using self.__dict__, only instance attributes set will
                be returned
                * a key __class__ must be added to this dictionary with the
                class name of the object
                * created_at and updated_at must be converted to string
                object in ISO format:
                    _ format: %Y-%m-%dT%H:%M:%S.%f
                    (ex: 2017-06-14T22:31:03.285259)
                    _ you can use isoformat() of datetime object
                * This method will be the first piece of the serialization/
                deserialization process: create a dictionary representation
                with “simple object type” of our BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Method __init__ that initializes the attributes eather using
        kwargs if kwargs do exist or casual init.
        - time_format is to specify the format of date and time.
        - setattr to give the instance an attribute with a certain val.
        - strptime to set the format of datetime to the time_format.
        - uuid.uuid4 to give the id a unique uuid.
        - datetime.now() to make the created_at object's creation time.
        - updated_at object's update time.
        - kwargs used to initialize the attributes.
        """
        if kwargs:
            time_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(val, time_format))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """A string representation of an object using the method __str__"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """An update to the attribute updated_at using the method save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """A dictionary representation of an object using the method to_dict"""
        dictionnary = self.__dict__.copy()
        dictionnary["__class__"] = self.__class__.__name__
        dictionnary["created_at"] = self.created_at.isoformat()
        dictionnary["updated_at"] = self.updated_at.isoformat()
        return dictionnary
