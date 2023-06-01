import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1 ) == 2

    def test_adding_subtraction(self):
        assert self.calculator.subtraction(self, 8, 3 ) == 5

    def test_zero_division(self):
        assert self.calculator.division(self, 21, 7) == 3

    def test_zero_multiply(self):
        assert self.calculator.multiply(self, 5, 5) == 25

    def teardown(self):
        print('Выполнен метод Teardown')