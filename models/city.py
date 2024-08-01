#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """The init method for the City class"""
        super().__init__(*args, **kwargs)
