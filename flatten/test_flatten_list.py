import pytest

from flatten_list import flatten_with_recursion, flatten_with_whileloop


data = [1, [2, 3], 4, [5, [6, [7]], 8], 9]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_flatten_with_recursion():
    actual = flatten_with_recursion(data)
    assert actual == expected


def test_flatten_with_whileloop():
    actual = flatten_with_whileloop(data)
    assert actual == expected
