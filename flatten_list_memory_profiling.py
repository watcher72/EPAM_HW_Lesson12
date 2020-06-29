from memory_profiler import profile

from flatten.flatten_list import flatten_with_recursion, flatten_with_whileloop


#Prepare data
import random

RANGE = 10
nested_list = []
for i in range(RANGE):
    items_num_2 = random.randint(1, 10)
    if items_num_2 == 1:
        nested_list.append(random.randint(-100, 100))
    else:
        temp = []
        for j in range(items_num_2):
            items_num_3 = random.randint(1, 10)
            if items_num_3 == 1:
                temp.append(random.randint(-100, 100))
            else:
                temp.append([random.randint(-100, 100) for k in range(items_num_3)])
        nested_list.append(temp)

        
@profile
def run_all(n):
    result_rec = [flatten_with_recursion(nested_list) for _ in range(n)]
    result_loop = [flatten_with_whileloop(nested_list) for _ in range(n)]

    
if __name__ == '__main__':
    run_all(1000)
