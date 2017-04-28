import unittest
from random import randint
from arithmetic_app.arithmetic import ArithmeticOperations


class TestArithmeticOperations(unittest.TestCase, ArithmeticOperations):

    def setUp(self):
        ArithmeticOperations.__init__(self)
        self.first_value = randint(0, 10)
        self.second_value = randint(0, 10)
        self.test_value = self.first_value + self.second_value + 1

    def test_addition(self):
        result = self.calculate('addition', self.first_value, self.second_value)
        self.assertEqual(result, self.first_value + self.second_value)

    def test_subtraction(self):
        result = self.calculate('subtraction', self.first_value, self.second_value)
        self.assertEqual(result, self.first_value - self.second_value)

    def test_multiplication(self):
        result = self.calculate('multiplication', self.first_value, self.second_value)
        self.assertEqual(result, self.first_value * self.second_value)

    def test_division(self):
        result = self.calculate('division', self.first_value, self.second_value)
        self.assertEqual(result, self.first_value / self.second_value)

    def test_zero_division(self):
        result = self.calculate('division', self.first_value, 0)
        self.assertEqual(result, "Cannot divide into zero.")

    def test_not_equal_addition(self):
        result = self.calculate('addition', self.first_value, self.second_value)
        self.assertNotEqual(result, self.test_value)

    def test_not_equal_subtraction(self):
        result = self.calculate('subtraction', self.first_value, self.second_value)
        self.assertNotEqual(result, self.test_value)

    def test_not_equal_multiplication(self):
        result = self.calculate('multiplication', self.first_value, self.second_value)
        self.assertNotEqual(result, self.test_value)

    def test_not_equal_division(self):
        result = self.calculate('division', self.first_value, self.second_value)
        self.assertNotEqual(result, self.test_value)
