#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.place import Place
from datetime import datetime
import pep8


class TestPlace(unittest.TestCase):
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
        instance = Place()
        self.assertEqual(Place, type(instance))

    def test_instance_id(self):
        "testing"
        instance = Place()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        "testing"
        instance = Place()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        "testing"
        instance_1 = Place()
        instance_2 = Place()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = Place()
        expected_str = f"[Place] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = Place()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = Place()
        instance.name = "My First Model"
        self.assertEqual(instance.name, "My First Model")

    def test_instance_init_none(self):
        """Testing none"""
        instance = Place()
        instance.city_id = None
        instance.user_id = None
        instance.name = None
        instance.description = None
        instance.number_rooms = None
        instance.number_bathrooms = None
        instance.max_guest = None
        instance.price_by_night = None
        instance.latitude = None
        instance.longitude = None
        instance.amenity_ids = None
        self.assertEqual(instance.city_id, None)
        self.assertEqual(instance.user_id, None)
        self.assertEqual(instance.name, None)
        self.assertEqual(instance.description, None)
        self.assertEqual(instance.number_rooms, None)
        self.assertEqual(instance.number_bathrooms, None)
        self.assertEqual(instance.max_guest, None)
        self.assertEqual(instance.price_by_night, None)
        self.assertEqual(instance.latitude, None)
        self.assertEqual(instance.longitude, None)
        self.assertEqual(instance.amenity_ids, None)
