from memory_profiler import profile

from mapping.mapping_list_2 import to_upper_v1_to_list, to_upper_v2_to_list, to_upper_v3, to_upper_v4, prepare_data


@profile
def run_all():
    data = prepare_data(24, 10000)
    result1 = to_upper_v1_to_list(data)
    result2 = to_upper_v2_to_list(data)
    result3 = to_upper_v3(data)
    result4 = to_upper_v4(data)

    
if __name__ == '__main__':
    run_all()
