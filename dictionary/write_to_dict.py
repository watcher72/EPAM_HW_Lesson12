import random


#prepare data
RANGE = 100000
ABC = 'abcdefghijklmnopqrstufwxyzABCDEFGHIJKLMNOPQRSTUFWXYZ'

inline_keys = [x for x in range(RANGE)]
inline_values = [''.join(random.sample(ABC, 8)) for _ in range(RANGE)]
random_keys = [random.randint(0, RANGE) for _ in range(RANGE)]
random_values = [''.join(random.sample(ABC, random.randint(8, 24))) for _ in range(RANGE)]


def write_to_dict_v1(keys, values):
    """
    Write items in dict with for-loop.
    The existing values will be overwritten.
    """
    result = {}
    for key, value in zip(keys, values):
        result[key] = value
    return result


def write_to_dict_v2(keys, values):
    """
    Write items in dictionary with method setdefault. 
    The existing items will not be overwritten.
    """
    result = {}
    for key, value in zip(keys, values):
        result.setdefault(key, value)
    return result


def write_to_dict_v3(keys, values):
    """
    Write items in dictionary with checking if the item just in the dictionary. 
    The existing items will not be overwritten.
    """
    result = {}
    for key, value in zip(keys, values):
        if key not in result:
            result[key] = value
    return result


def write_to_dict_v4(keys, values):
    """
    Write items in dictionary with dictionary comprehention. 
    The existing items will be overwritten.
    """
    return {key: value for key, value in zip(keys, values)}
