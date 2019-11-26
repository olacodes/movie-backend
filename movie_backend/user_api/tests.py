from django.test import TestCase
import unittest

# Create your tests here.

class TravisTest(unittest.TestCase):
    def test_travis(self):
        self.assertEqual('sodiq'.upper(), 'SODIQ')


if __name__ == "__main__":
    unittest.main()