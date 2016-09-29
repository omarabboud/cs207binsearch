
from pytest import raises
from binsearch import binary_search

def test_notthere():
    assert binary_search([1, 3, 5],2) == -1

def test_there():
    assert binary_search([1, 3, 5],3) == 0

def test_there():
    assert binary_search([1, 3, 5],3) == 0
    
def int_char():
    with raises(TypeError):
        binary_search([1,3,5,8],3,'a')