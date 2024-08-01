#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """The init method for the Review class"""
        super().__init__(*args, **kwargs)
