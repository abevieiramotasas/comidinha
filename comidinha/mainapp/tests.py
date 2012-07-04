"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import unittest


class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1, 2, "deu certo")


if __name__ == '__main__':
    unittest.main()