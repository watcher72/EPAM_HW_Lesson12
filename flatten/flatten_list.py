def flatten_with_recursion(data):
    """Make flat list from the given list with any nesting level."""
    result = []
    for item in data:
        result.append(item) if not isinstance(item, list) \
            else result.extend(flatten_with_recursion(item))
    return result


def flatten_with_whileloop(data):
    is_flat = True
    while is_flat:
        is_flat = False
        temp = []
        for item in data:
            if isinstance(item, list):
                temp.extend(item)
                is_flat = True
            else:
                temp.append(item)
        data = temp
    return data
