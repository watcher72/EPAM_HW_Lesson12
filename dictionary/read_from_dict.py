import random


#prepare data
RANGE = 10000
ABC = 'abcdefghijklmnopqrstufwxyzABCDEFGHIJKLMNOPQRSTUFWXYZ'

inline_keys = [x for x in range(RANGE)]
inline_values = [''.join(random.sample(ABC, 8)) for _ in range(RANGE)]
random_keys = [random.randint(0, RANGE) for _ in range(RANGE)]
random_values = [''.join(random.sample(ABC, random.randint(8, 24))) for _ in range(RANGE)]

data = {k: v for k, v in zip(inline_keys, inline_values)}
data_random = {k: v for k, v in zip(random_keys, random_values)}


def read_from_dict_v1(dictionary, key):
    """
    Read items from the dictionary with method get.
    Return None if the key is not in dictionary.
    """
    return dictionary.get(key)


def read_from_dict_v2(dictionary, key):
    """
    Read items from the dictionary with checking if the key is in dictionary.
    Return None if the key is not in dictionary.
    """
    return dictionary[key] if key in dictionary else None


def read_from_dict_v3(dictionary, key):
    """
    Read items from the dictionary with interrupt handling.
    Return None if the key is not in dictionary.
    """
    try:
        value = dictionary[key]
    except KeyError:
        value = None
    return value
