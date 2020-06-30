import random
from memory_profiler import profile

from sort_list.sort_list import standart_sort, selection_sort, merge_sort


# Prepare data
RANGE = 1000
data = [random.randint(-1000, 1000) for _ in range(RANGE)]


@profile
def run_all(n=10):
    result1 = [standart_sort(data) for _ in range(n)]
    result2 = [selection_sort(data) for _ in range(n)]
    result3 = [merge_sort(data) for _ in range(n)]


if __name__ == '__main__':
    run_all(100)
