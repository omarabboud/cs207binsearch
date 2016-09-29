
from pytest import raises
from binsearch import binary_search

def test_binsearch():
    assert binary_search([5], 5) == 0

def test_notthere():
    assert binary_search([1,3,5], 2) == False

def test_char():
    with raises(TypeError):
        binary_search(['a',3])
    
def test_zero_value():
    with raises(ValueError):
        binary_search([0,0], 0)
        