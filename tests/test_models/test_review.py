#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.review import Review
from datetime import datetime
import pep8


class TestReview(unittest.TestCase):
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
        instance = Review()
        self.assertEqual(Review, type(instance))

    def test_instance_id(self):
        "testing"
        instance = Review()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        "testing"
        instance = Review()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        "testing"
        instance_1 = Review()
        instance_2 = Review()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = Review()
        expected_str = f"[Review] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = Review()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = Review()
        instance.text = "This is a review"
        self.assertEqual(instance.text, "This is a review")

    def test_instance_init_none(self):
        """Testing none"""
        instance = Review()
        instance.place_id = None
        instance.user_id = None
        instance.text = None
        self.assertEqual(instance.place_id, None)
        self.assertEqual(instance.user_id, None)
        self.assertEqual(instance.text, None)
