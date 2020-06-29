import pytest

from read_from_dict import read_from_dict_v1, read_from_dict_v2, read_from_dict_v3


test_data = {1: 'abc', 4: 'def', 6: 'hjik'}


def test_in_dict_v1():
    assert read_from_dict_v1(test_data, 4) == 'def'
    

def test_not_in_dict_v1():
    assert read_from_dict_v1(test_data, 2) is None


def test_in_dict_v2():
    assert read_from_dict_v1(test_data, 4) == 'def'
    

def test_not_in_dict_v2():
    assert read_from_dict_v1(test_data, 2) is None


def test_in_dict_v3():
    assert read_from_dict_v1(test_data, 4) == 'def'
    

def test_not_in_dict_v3():
    assert read_from_dict_v1(test_data, 2) is None
