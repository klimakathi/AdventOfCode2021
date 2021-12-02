import numpy as np

def measure_depth(data):
    count = 0
    for i in range(1, np.shape(data)[0]):
        if data[i] > data[i - 1]:
            count += 1
    return count


def measure_depth_advanced(data):
    count = 0
    sum_list = []
    for i in range(2, np.shape(data)[0]):
        sum_3 = data[i - 2] + data[i - 1] + data[i]
        sum_list.append(sum_3)
    for i in range(1, len(sum_list)):
        if sum_list[i] > sum_list[i - 1]:
            count += 1
    return count


