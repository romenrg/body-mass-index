import unittest
from bmi import Bmi

class TestHello(unittest.TestCase):
    def test_ranges(self):
        self.assertEqual(Bmi.boundaries, [0, 18.5, 25, 30, 35, 40])

    def test_range_info_under(self):
        self.assertEqual(Bmi.range_info(17), "Underweight")
    def test_range_info_healthy(self):
        self.assertEqual(Bmi.range_info(19), "Healthy")
    def test_range_info_over(self):
        self.assertEqual(Bmi.range_info(25.3), "Overweight")
    def test_range_info_obese1(self):
        self.assertEqual(Bmi.range_info(30.1), "Obese | Class I")
    def test_range_info_obese2(self):
        self.assertEqual(Bmi.range_info(36), "Obese | Class II")
    def test_range_info_obese3(self):
        self.assertEqual(Bmi.range_info(46), "Obese | Class III")

    def test_range_info_under_lang(self):
        self.assertEqual(Bmi.range_info(17, "es"), "Bajo peso")

    def test_ranges_with_info(self):
        self.assertEqual(Bmi.ranges_with_info(), [
            {'From': 0, 'To': 18.5, 'Info': 'Underweight'},
            {'From': 18.5, 'To': 25, 'Info': 'Healthy'},
            {'From': 25, 'To': 30, 'Info': 'Overweight'},
            {'From': 30, 'To': 35, 'Info': 'Obese | Class I'},
            {'From': 35, 'To': 40, 'Info': 'Obese | Class II'},
            {'From': 40, 'To': "", 'Info': 'Obese | Class III'},
        ])

    def test_ranges_with_info_lang(self):
        self.assertEqual(Bmi.ranges_with_info("es"), [
            {'From': 0, 'To': 18.5, 'Info': 'Bajo peso'},
            {'From': 18.5, 'To': 25, 'Info': 'Peso saludable'},
            {'From': 25, 'To': 30, 'Info': 'Sobrepeso'},
            {'From': 30, 'To': 35, 'Info': 'Obesidad | Clase I'},
            {'From': 35, 'To': 40, 'Info': 'Obesidad | Clase II'},
            {'From': 40, 'To': "", 'Info': 'Obesidad | Clase III'},
        ])

    # TODO: ranges_with_info_lang

    def test_calculate_equal_80_180(self):
        self.assertEqual(Bmi.calculate(80, 1.80), 24.7, "Body Mass Index for 80kg and 1.80m is 24.7")
    def test_calculate_equal_64_164(self):
        self.assertEqual(Bmi.calculate(64, 1.64), 23.8, "Body Mass Index for 64kg and 1.64m is 23.8")
    def test_calculate_obese_93_171(self):
        self.assertEqual(Bmi.calculate(93, 1.71), 31.8, "Body Mass Index for 93kg and 1.71m is 31.8")
    def test_calculate_thin_59_176(self):
        self.assertEqual(Bmi.calculate(59, 1.76), 19, "Body Mass Index for 59kg and 1.76m is 19")

    def test_calculate_bmi_with_info(self):
        self.assertEqual(Bmi.calculate_bmi_with_info(80, 1.80), (24.7, "Healthy"))
    def test_calculate_bmi_with_info_lang(self):
        self.assertEqual(Bmi.calculate_bmi_with_info(80, 1.80, "es"), (24.7, "Peso saludable"))

    def test_your_weight_boundaries(self):
        self.assertEqual(Bmi.your_weight_boundaries(1.80), [59.9, 81, 97.2, 113.4, 129.6])

    def test_your_healthy_weight(self):
        self.assertEqual(Bmi.your_healthy_weight(1.80), [59.9, 81])

    # TODO: your_weight_boundaries_with_info

    # TODO: your_weight_boundaries_with_info_lang

