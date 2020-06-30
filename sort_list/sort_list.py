def standart_sort(data):
    return sorted(data)


def selection_sort(data):
    for i in range(len(data)):
        min_elem = min(data[i:])
        min_ind = data[i:].index(min_elem)
        data[i], data[min_ind + i] = min_elem, data[i]
    return data


def merge(left, right):
    left_len = len(left)
    right_len = len(right)
    left_pointer = 0
    right_pointer = 0
    result = []
    while left_pointer < left_len and right_pointer < right_len:
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    if left_pointer == left_len:
        result.extend(right[right_pointer:])
    if right_pointer == right_len:
        result.extend(left[left_pointer:])
    return result


def merge_sort(data):
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)
