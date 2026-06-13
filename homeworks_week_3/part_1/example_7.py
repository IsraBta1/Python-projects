import math
from pytest import approx

def test_sqrt():
    assert math.sqrt(5) == approx(2.24, abs=0.01)