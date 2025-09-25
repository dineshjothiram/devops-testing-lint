import pytest


from myapp.utils import add, divide




def test_add_positive_numbers():
assert add(2, 3) == 5




@pytest.mark.parametrize(
"a,b,expected",
[
(10, 2, 5.0),
(9, 3, 3.0),
(5, 2, 2.5),
],
)
def test_divide_various(a, b, expected):
assert divide(a, b) == expected




def test_divide_by_zero_raises():
with pytest.raises(ValueError):
divide(1, 0)