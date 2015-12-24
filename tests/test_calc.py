from unittest import TestCase
from calculator.calculator import Calculator

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock


class CalcTestCase(TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_mock(self):
        mock_object = MagicMock()
        mock_object.__str__.return_value = 'hello'
        self.assertEqual(str(mock_object), 'hello')


class CalculatorTestCase(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_power(self):
        self.assertEqual(self.calculator.power(12), 144)
