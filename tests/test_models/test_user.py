#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""

import unittest
from models.user import User
from datetime import datetime
import pep8


class TestUser(unittest.TestCase):
    """
    TESTING CLASS
    """

    def test_pep8_compliance(self):
        """ Test PEP8 compliance using pycodestyle"""
        pycodestyle = pep8.StyleGuide(quiet=True)
        file_paths = ["models/user.py"]
        result = pycodestyle.check_files(file_paths)
        error_message = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error_message)

    def test_instance_init_none(self):
        """Testing none"""
        instance = User()
        instance.email = None
        instance.password = None
        instance.first_name = None
        instance.last_name = None
        self.assertEqual(instance.email, None)
        self.assertEqual(instance.password, None)
        self.assertEqual(instance.first_name, None)
        self.assertEqual(instance.last_name, None)
