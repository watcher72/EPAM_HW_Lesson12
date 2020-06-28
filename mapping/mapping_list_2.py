import random

from memory_profiler import profile


ABC = 'abcdefghijklmnopqrstufwxyzABCDEFGHIJKLMNOPQRSTUFWXYZ'


def prepare_data(letters, words):
    return [''.join(random.sample(ABC, letters)) for _ in range(words)]


def to_upper_v1_to_list(data):
    return list(map(lambda x: x.upper(), data))


def to_upper_v2_to_list(data):
    return list((word.upper() for word in data))


def to_upper_v3(data):
    return [word.upper() for word in data]


def to_upper_v4(data):
    result = []
    for word in data:
        result.append(word.upper())
    return result
