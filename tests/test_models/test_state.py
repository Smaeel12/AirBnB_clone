#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.state import State
from datetime import datetime
import pep8


class TestState(unittest.TestCase):
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

    def test_instance(self):
        """Testing a new created instance"""
        instance = State()
        self.assertEqual(State, type(instance))

    def test_instance_id(self):
        "testing"
        instance = State()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        "testing"
        instance = State()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        "testing"
        instance_1 = State()
        instance_2 = State()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = State()
        expected_str = f"[State] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = State()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = State()
        instance.name = "State"
        self.assertEqual(instance.name, "State")

    def test_instance_init_none(self):
        """Testing none"""
        instance = State()
        instance.name = None
        self.assertEqual(instance.name, None)
