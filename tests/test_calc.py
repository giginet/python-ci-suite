from unittest import TestCase
from calculator.calculator import Calculator


class CalcTestCase(TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)


class CalculatorTestCase(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_power(self):
        self.assertEqual(self.calculator.power(12), 144)
