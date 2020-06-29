import pytest

from write_to_dict import write_to_dict_v1, write_to_dict_v2, write_to_dict_v3, write_to_dict_v4


items = list(zip([1, 2, 3, 4, 2], ['abc', 'def', 'ghj', 'ikl', 'mno']))


def test_write_to_dict_v1():
    actual = write_to_dict_v1({}, items)
    expected = {1: 'abc', 2: 'mno', 3: 'ghj', 4: 'ikl'}
    assert actual == expected


def test_write_to_dict_v2():
    actual = write_to_dict_v2({}, items)
    expected = {1: 'abc', 2: 'def', 3: 'ghj', 4: 'ikl'}
    assert actual == expected


def test_write_to_dict_v3():
    d = {}
    actual = write_to_dict_v3({}, items)
    expected = {1: 'abc', 2: 'def', 3: 'ghj', 4: 'ikl'}
    assert actual == expected


def test_write_to_dict_v4():
    actual = write_to_dict_v4({}, items)
    expected = {1: 'abc', 2: 'mno', 3: 'ghj', 4: 'ikl'}
    assert actual == expected
