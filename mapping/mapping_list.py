def to_upper_v1(data):
    return map(lambda x: x.upper(), data)


def to_upper_v2(data):
    return (word.upper() for word in data)


def to_upper_v3(data):
    return [word.upper() for word in data]


def to_upper_v4(data):
    result = []
    for word in data:
        result.append(word.upper())
    return result
