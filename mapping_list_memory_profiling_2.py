import random
from memory_profiler import profile

from mapping.mapping_list_2 import to_upper_v1_to_list, to_upper_v2_to_list, to_upper_v3, to_upper_v4


ABC = 'abcdefghijklmnopqrstufwxyzABCDEFGHIJKLMNOPQRSTUFWXYZ'


def prepare_data(letters, words):
    return [''.join(random.sample(ABC, letters)) for _ in range(words)]


@profile
def run_all(n):
    data = prepare_data(24, 10000)
    result1 = [to_upper_v1_to_list(data) for _ in range(n)]
    result2 = [to_upper_v2_to_list(data) for _ in range(n)]
    result3 = [to_upper_v3(data) for _ in range(n)]
    result4 = [to_upper_v4(data) for _ in range(n)]


if __name__ == '__main__':
    run_all(10)
