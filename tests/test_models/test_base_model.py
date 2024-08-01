#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from datetime import datetime, timedelta
import pep8


class TestBaseModel(unittest.TestCase):
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
        instance = BaseModel()
        self.assertEqual(BaseModel, type(instance))

    def test_instance_id(self):
        "testing"
        instance = BaseModel()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        "testing"
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        "testing"
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        self.assertEqual(instance.name, "My First Model")
        self.assertEqual(instance.my_number, 89)

    def test_object_to_dict(self):
        """Testing To_dict method"""
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        dictionary = instance.to_dict()
        dictionary_cmp = {
            'my_number': 89,
            'name': 'My First Model',
            '__class__': 'BaseModel',
            'updated_at': instance.updated_at.isoformat(),
            'id': instance.id,
            'created_at': instance.created_at.isoformat()
        }

        # Define a tolerance for timestamp comparison (e.g., 1 second)
        timestamp_tolerance = timedelta(seconds=1)
