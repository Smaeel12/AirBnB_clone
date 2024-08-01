#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class State that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """The init method for the State class_"""
        super().__init__(*args, **kwargs)
