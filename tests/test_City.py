#!/usr/bin/python3
import unittest
from models.City import City
import models
from datetime import datetime
from time import sleep


class TestCityInstance(unittest.TestCase):
    def test_instance(self):
        instance = City()
        self.assertTrue(isinstance(instance, City))

    def test_new_instance(self):
        instance = City()
        self.assertIn(instance, models.storage.all().values())

    def test_id_string(self):
        instance = City()
        self.assertIsInstance(instance.id, str)

    def test_created_at_the_same_datetime(self):
        instance = City()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_the_same_datetime(self):
        instance = City()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_ids_unique(self):
        instance1 = City()
        instance2 = City()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_different(self):
        instance1 = City()
        sleep(0.10)
        instance2 = City()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_created_in_the_same(self):
        instance1 = City()
        instance2 = City()
        self.assertEqual(instance1.created_at, instance2.created_at)

    def test_updated_in_the_same(self):
        instance1 = City()
        instance2 = City()
        self.assertEqual(instance1.updated_at, instance2.updated_at)

    def test_updated_at_different(self):
        instance1 = City()
        sleep(0.10)
        instance2 = City()
        self.assertLess(instance1.updated_at, instance2.updated_at)

    def test_dict_type(self):
        instance = City()
        self.assertTrue(isinstance(instance.to_dict(), dict))

    def test_dict_keys(self):
        instance = City()
        self.assertIn("id", instance.to_dict())
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())

    def test_dict_attributes(self):
        instance = City()
        instance.name = "REDAOUSSAMA"
        instance.my_number = 98
        self.assertIn("name", instance.to_dict())
        self.assertIn("my_number", instance.to_dict())

    def test_save(self):
        instance = City()
        sleep(0.10)
        first_updated_at = instance.updated_at
        instance.save()
        self.assertLess(first_updated_at, instance.updated_at)


if __name__ == "__main__":
    unittest.main()
