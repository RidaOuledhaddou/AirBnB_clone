#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime
from time import sleep


class TestBaseModelInstance(unittest.TestCase):
    def test_instance(self):
        instance = BaseModel()
        self.assertTrue(isinstance(instance, BaseModel))

    def test_new_instance(self):
        instance = BaseModel()
        self.assertIn(instance, models.storage.all().values())

    def test_id_string(self):
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)

    def test_created_at_the_same_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_the_same_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_ids_unique(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_different(self):
        instance1 = BaseModel()
        sleep(0.10)
        instance2 = BaseModel()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_created_in_the_same(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertEqual(instance1.created_at, instance2.created_at)

    def test_updated_in_the_same(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertEqual(instance1.updated_at, instance2.updated_at)

    def test_updated_at_different(self):
        instance1 = BaseModel()
        sleep(0.10)
        instance2 = BaseModel()
        self.assertLess(instance1.updated_at, instance2.updated_at)

    def test_dict_type(self):
        instance = BaseModel()
        self.assertIsInstance(instance.to_dict(), dict)

    def test_dict_keys(self):
        instance = BaseModel()
        self.assertIn("id", instance.to_dict())
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())

    def test_dict_attributes(self):
        instance = BaseModel()
        instance.name = "REDAOUSSAMA"
        instance.my_number = 98
        self.assertIn("name", instance.to_dict())
        self.assertIn("my_number", instance.to_dict())

    def test_save(self):
        instance = BaseModel()
        sleep(0.10)
        first_updated_at = instance.updated_at
        instance.save()
        self.assertLess(first_updated_at, instance.updated_at)


if __name__ == "__main__":
    unittest.main()
