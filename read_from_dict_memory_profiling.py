import random
from memory_profiler import profile

from dictionary.read_from_dict import read_from_dict_v1, read_from_dict_v2, read_from_dict_v3


#prepare data
RANGE = 10000
ABC = 'abcdefghijklmnopqrstufwxyzABCDEFGHIJKLMNOPQRSTUFWXYZ'

random_keys = [random.randint(0, RANGE) for _ in range(RANGE)]
random_values = [''.join(random.sample(ABC, random.randint(8, 24))) for _ in range(RANGE)]

data_random = {k: v for k, v in zip(random_keys, random_values)}


@profile
def run_all(n):
    def loop(func):
        for i in range(RANGE):
            temp = func(data_random, i)

    result1 = [loop(read_from_dict_v1) for _ in range(n)]
    result2 = [loop(read_from_dict_v2) for _ in range(n)]
    result3 = [loop(read_from_dict_v3) for _ in range(n)]


if __name__ == '__main__':
    run_all(10)
