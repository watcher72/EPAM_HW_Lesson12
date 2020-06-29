import pytest

from write_to_dict import write_to_dict_v1, write_to_dict_v2, write_to_dict_v3, write_to_dict_v4


keys = [1, 2, 3, 4, 2]
values = ['abc', 'def', 'ghj', 'ikl', 'mno']
expected = {1: 'abc', 2: 'def', 3: 'ghj', 4: 'ikl'}

def test_write_to_dict_v1():
    actual = write_to_dict_v1(keys, values)
    expected = {1: 'abc', 2: 'mno', 3: 'ghj', 4: 'ikl'}
    assert actual == expected


def test_write_to_dict_v2():
    actual = write_to_dict_v2(keys, values)
    expected = {1: 'abc', 2: 'def', 3: 'ghj', 4: 'ikl'}
    assert actual == expected

    
def test_write_to_dict_v3():
    actual = write_to_dict_v3(keys, values)
    expected = {1: 'abc', 2: 'def', 3: 'ghj', 4: 'ikl'}
    assert actual == expected


def test_write_to_dict_v4():
    actual = write_to_dict_v4(keys, values)
    expected = {1: 'abc', 2: 'mno', 3: 'ghj', 4: 'ikl'}
    assert actual == expected
