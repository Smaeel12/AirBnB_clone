""" This module contains the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)