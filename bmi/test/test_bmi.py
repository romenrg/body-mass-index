import unittest
from bmi import Bmi

class TestHello(unittest.TestCase):
    def test_hello(self):
        test_bmi = Bmi()
        self.assertEqual(test_bmi.hello(), "This util calculates the Body Mass Index", "Message should match")
    def test_calculate_equal_80_180(self):
        self.assertEqual(Bmi.calculate(80, 1.80), 24.7, "Body Mass Index for 80kg and 1.80m is 24.7")
    def test_calculate_equal_64_164(self):
        self.assertEqual(Bmi.calculate(64, 1.64), 23.8, "Body Mass Index for 64kg and 1.64m is 23.8")
    def test_calculate_obese_93_171(self):
        self.assertEqual(Bmi.calculate(93, 1.71), 31.8, "Body Mass Index for 93kg and 1.71m is 31.8")
    def test_calculate_thin_59_176(self):
        self.assertEqual(Bmi.calculate(59, 1.76), 19, "Body Mass Index for 59kg and 1.76m is 19")