#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines the User class."""


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
