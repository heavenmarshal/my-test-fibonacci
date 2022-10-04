import pytest
from contextlib import nullcontext as does_not_raise
from my_fibonacci import fibonacci


@pytest.mark.parametrize(
    "n,expected,exception",
    [
        (1, 1, does_not_raise()),
        (2, 1, does_not_raise()),
        (10, 55, does_not_raise()),
        (14, 377, does_not_raise()),
        (-1, -1, pytest.raises(ValueError, match="expect non-negative input, get -1")),
        (1.2, -1, pytest.raises(TypeError, match="expect integer input, get 1.2")),
    ],
)
def test_fibonacci(n, expected, exception):
    with exception:
        assert fibonacci(n) == expected
