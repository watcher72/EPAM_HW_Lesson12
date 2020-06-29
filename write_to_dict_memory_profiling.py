from memory_profiler import profile

from dictionary.write_to_dict import write_to_dict_v1, write_to_dict_v2, write_to_dict_v3, write_to_dict_v4
from dictionary.write_to_dict import inline_keys, inline_values


@profile
def run_all():
    write_to_dict_v1(inline_keys, inline_values)
    write_to_dict_v2(inline_keys, inline_values)
    write_to_dict_v3(inline_keys, inline_values)
    write_to_dict_v4(inline_keys, inline_values)


if __name__ == '__main__':
    run_all()
