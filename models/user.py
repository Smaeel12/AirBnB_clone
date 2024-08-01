#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that inherits from BaseModel
        - Update FileStorage to manage correctly serialization and
        deserialization of User.
        - Update your command interpreter (console.py) to allow show,
        create, destroy, update and all used with User.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """The init method for the User class"""
        super().__init__(*args, **kwargs)
