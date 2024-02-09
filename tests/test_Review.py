#!/usr/bin/python3
import unittest
from models.Review import Review
import models
from datetime import datetime
from time import sleep


class TestReviewInstance(unittest.TestCase):
    def test_instance(self):
        instance = Review()
        self.assertTrue(isinstance(instance, Review))

    def test_new_instance(self):
        instance = Review()
        self.assertIn(instance, models.storage.all().values())

    def test_id_string(self):
        instance = Review()
        self.assertIsInstance(instance.id, str)

    def test_created_at_the_same_datetime(self):
        instance = Review()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_the_same_datetime(self):
        instance = Review()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_ids_unique(self):
        instance1 = Review()
        instance2 = Review()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_different(self):
        instance1 = Review()
        sleep(0.10)
        instance2 = Review()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_created_in_the_same(self):
        instance1 = Review()
        instance2 = Review()
        self.assertEqual(instance1.created_at, instance2.created_at)

    def test_updated_in_the_same(self):
        instance1 = Review()
        instance2 = Review()
        self.assertEqual(instance1.updated_at, instance2.updated_at)

    def test_updated_at_different(self):
        instance1 = Review()
        sleep(0.10)
        instance2 = Review()
        self.assertLess(instance1.updated_at, instance2.updated_at)

    def test_dict_type(self):
        instance = Review()
        self.assertTrue(isinstance(instance.to_dict(), dict))

    def test_dict_keys(self):
        instance = Review()
        self.assertIn("id", instance.to_dict())
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())

    def test_dict_attributes(self):
        instance = Review()
        instance.name = "REDAOUSSAMA"
        instance.my_number = 98
        self.assertIn("name", instance.to_dict())
        self.assertIn("my_number", instance.to_dict())

    def test_save(self):
        instance = Review()
        sleep(0.10)
        first_updated_at = instance.updated_at
        instance.save()
        self.assertLess(first_updated_at, instance.updated_at)


if __name__ == "__main__":
    unittest.main()
