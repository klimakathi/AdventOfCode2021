import pandas as pd

input2 = pd.read_csv('input2.txt', sep=' ', header=None)


def wrong_position(data):
    directions = list(data[0])
    values = list(data[1])
    horizontal_count = 0
    vertical_count = 0
    for i in range(len(values)):
        if directions[i] == 'forward':
            horizontal_count += values[i]
        if directions[i] == 'up':
            vertical_count -= values[i]
        if directions[i] == 'down':
            vertical_count += values[i]
    print('horizontal position: ', horizontal_count)
    print('vertical position: ', vertical_count)

    return horizontal_count * vertical_count


def right_position(data):
    directions = list(data[0])
    values = list(data[1])
    horizontal_count = 0
    vertical_count = 0
    aim = 0
    for i in range(len(values)):
        if directions[i] == 'forward':
            horizontal_count += values[i]
            vertical_count += aim * values[i]
        if directions[i] == 'up':
            aim -= values[i]
        if directions[i] == 'down':
            aim += values[i]
    return horizontal_count * vertical_count


print(right_position(input2))
