#!/usr/bin/python3
"""
Test case module for BaseModel class in base_model.py
"""
from models.base_model import BaseModel
from unittest import TestCase, main
from datetime import datetime


class TestBaseModel(TestCase):
    """Tests for class BaseModel"""

    def test_create_instance(self):
        """Tests if new instance of BaseModel is created successfully"""
        new_model = BaseModel()
        self.assertIsNotNone(new_model)

    def test_str_return(self):
        pass
