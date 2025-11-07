import pytest
from .same_signs import same_signs

@pytest.mark.parametrize("a",["stuff", ["things", "nonsense"], (1,2)])
def test_same_signs_incompatible(a):
    with pytest.raises(TypeError):
        same_signs(a,a)

@pytest.mark.parametrize("a",[1, 2, 3, 5, 2.3])
@pytest.mark.parametrize("b",[0, 1, 2, 3, 5, 2.3, float('inf')])
def test_same_signs_positive_positive(a, b):
    assert same_signs(a, b)

@pytest.mark.parametrize("a",[-1, -2, -3, -5, -2.3])
@pytest.mark.parametrize("b",[ -1, -2, -3, -5, -2.3, -float('inf')])
def test_same_signs_negative_positive(a, b):
    assert same_signs(a, b)

@pytest.mark.parametrize("a",[1, 2, 3, 5, 2.3])
@pytest.mark.parametrize("b",[-1, -2, -3, -5, -2.3])
def test_same_signs_not_same_signs(a, b):
    assert not same_signs(a, b)