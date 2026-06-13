""" to do approx

def approx(expected_value, rel=None, abs=None, nan_ok=False):
    e = 7.135
    f = 7.128
def test_function():
    assert actual_value == approx(expected_value)  # pero no estan definidas las partes"""


from pytest import approx
import math

def test_sqrt():
    assert math.sqrt(5) == approx(2.24, rel=0.01)