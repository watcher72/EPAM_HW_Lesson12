from mapping.mapping_list import to_upper_v1, to_upper_v2, to_upper_v3, to_upper_v4


def test_to_upper_v1():
    actual = list(to_upper_v1(['abc', 'deFgH', 'ijKL']))
    expected = ['ABC', 'DEFGH', 'IJKL']
    assert actual == expected


def test_to_upper_v2():
    actual = list(to_upper_v2(['abc', 'deFgH', 'ijKL']))
    expected = ['ABC', 'DEFGH', 'IJKL']
    assert actual == expected

    
def test_to_upper_v3():
    actual = to_upper_v3(['abc', 'deFgH', 'ijKL'])
    expected = ['ABC', 'DEFGH', 'IJKL']
    assert actual == expected


def test_to_upper_v4():
    actual = to_upper_v4(['abc', 'deFgH', 'ijKL'])
    expected = ['ABC', 'DEFGH', 'IJKL']
    assert actual == expected
