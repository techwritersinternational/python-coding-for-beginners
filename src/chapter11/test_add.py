from addition import add
from addition import add_three

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_three():
    assert add_three(1, 2, 3) == 6
    assert add_three(5, -2, 1) == 4
    assert add_three(0, 0, 0) == 0

def test_add_strings():
    assert add("2", "3") == 5