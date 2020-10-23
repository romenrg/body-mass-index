import unittest
from bmi import Bmi

class TestHello(unittest.TestCase):
    def test_hello(self):
        test_bmi = Bmi()
        self.assertEqual(test_bmi.hello(), "This util calculates the Body Mass Index", "Message should match")