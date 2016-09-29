
from pytest import raises
from binsearch import binary_search

def test_binsearch():
    assert binary_search([5], 5) == 0

def test_char():
    with raises(TypeError):
        binary_search(['a',3])
    
def test_zero_value():
    with raises(ValueError):
        binary_search([0,0])
        