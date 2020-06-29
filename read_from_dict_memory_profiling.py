from memory_profiler import profile

from dictionary.read_from_dict import read_from_dict_v1, read_from_dict_v2, read_from_dict_v3
from dictionary.read_from_dict import data, RANGE


@profile
def run_all():
    def loop(func):
        for i in range(RANGE):
            temp = func(data, i)

    loop(read_from_dict_v1)
    loop(read_from_dict_v2)
    loop(read_from_dict_v3)


if __name__ == '__main__':
    run_all()
