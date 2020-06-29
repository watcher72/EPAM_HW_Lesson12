import random
from memory_profiler import profile

from dictionary.write_to_dict import write_to_dict_v1, write_to_dict_v2, write_to_dict_v3, write_to_dict_v4


#prepare data
RANGE = 10000
ABC = 'abcdefghijklmnopqrstufwxyzABCDEFGHIJKLMNOPQRSTUFWXYZ'

inline_keys = [x for x in range(RANGE)]
inline_values = [''.join(random.sample(ABC, 8)) for _ in range(RANGE)]
# random_keys = [random.randint(0, RANGE) for _ in range(RANGE)]
# random_values = [''.join(random.sample(ABC, random.randint(8, 24))) for _ in range(RANGE)]

inline_items = list(zip(inline_keys, inline_values))
# random_items = list(zip(random_keys, random_values))

@profile
def run_all(n):
    result1 = [write_to_dict_v1({}, inline_items) for _ in range(n)]
    result2 = [write_to_dict_v2({}, inline_items) for _ in range(n)]
    result3 = [write_to_dict_v3({}, inline_items) for _ in range(n)]
    result4 = [write_to_dict_v4({}, inline_items) for _ in range(n)]


if __name__ == '__main__':
    run_all(100)
