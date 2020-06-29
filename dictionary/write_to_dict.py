def write_to_dict_v1(dictionary, items):
    """
    Write items in dict with for-loop and using __setitem__.
    The existing values will be overwritten.
    """
    for key, value in items:
        dictionary[key] = value
    return dictionary


def write_to_dict_v2(dictionary, items):
    """
    Write items in dictionary with method setdefault.
    The existing items will not be overwritten.
    """
    for key, value in items:
        dictionary.setdefault(key, value)
    return dictionary


def write_to_dict_v3(dictionary, items):
    """
    Write items in dictionary with checking if the item just in the dictionary.
    The existing items will not be overwritten.
    """
    for key, value in items:
        if key not in dictionary:
            dictionary[key] = value
    return dictionary


def write_to_dict_v4(dictionary, items):
    """
    Write items in dictionary with dictionary comprehension.
    The existing items will be overwritten.
    """
    dictionary.update(items)
    return dictionary
