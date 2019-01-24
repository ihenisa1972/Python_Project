"""
Unit tests for the calculator library
"""


def add(first_term, second_term):
    return first_term + second_term

def subtract(first_term, second_term):
    return first_term - second_term



class TestCalculator:

    def test_addition(self):
        assert 4 == add(2, 2)

    def test_subtraction(self):
        assert 2 == subtract(4, 2)




