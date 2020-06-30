import pytest

from sort_list import standart_sort, selection_sort, merge_sort


test_data = [2, 6, 47, 8, 45, 6, 53, 0, 19, 67, 93, 346, 116]
sorted_list = [0, 2, 6, 6, 8, 19, 45, 47, 53, 67, 93, 116, 346]


def test_standart_sort():
    assert standart_sort(test_data) == sorted_list


def test_selection_sort():
    assert selection_sort(test_data) == sorted_list


def test_merge_sort():
    assert merge_sort(test_data) == sorted_list

