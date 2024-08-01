""" This module contains the State class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)