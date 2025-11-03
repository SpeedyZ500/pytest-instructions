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

class TestAddAB:
    def test_add_a_and_b_both_numeric(self):
        #Given
        a = 5
        b = 12.0
        expected = 17.0
        #Then
        result = add_a_and_b(a, b)
        assert result == expected

    def test_add_a_and_b_not_numeric_reject(self):
        #Given
        a = [1,3,5]
        b = "whatever"
        #Then
        with pytest.raises(TypeError):
            add_a_and_b(a, b)



class TestClassExample:
    value = 1
    def test_class_example_1(self):
        self.value = 2
        assert self.value == 2
    def test_class_example_2(self):
        assert self.value == 1