import numpy as np
from day1 import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_day1 = np.loadtxt('input1.txt')
    print('Let\'s rock this...')
    print('The buggy way of measuring depth... ', measure_depth(input_day1))
    print('The really advanced way: ', measure_depth_advanced(input_day1))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
