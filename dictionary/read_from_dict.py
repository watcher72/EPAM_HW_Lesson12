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
