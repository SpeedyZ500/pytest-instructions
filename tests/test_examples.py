import pytest
from example_code import add_a_and_b

def test_add_a_and_b_both_numeric():
    #Given
    a = 5
    b = 12.0
    expected = 17.0

    #Then
    result = add_a_and_b(a, b)
    assert result == expected

def test_add_a_and_b_not_numeric_reject():
    #Given
    a = [1,3,5]
    b = "whatever"

    #Then
    with pytest.raises(TypeError):
        add_a_and_b(a, b)