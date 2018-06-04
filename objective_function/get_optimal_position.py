"""
Type the following command in the command line or terminal and  a file sphere_100_position.txt will be generated.
python get_optimal_position.py sphere 100.
100 means the dimension size is 100.
sphere means the optimal position is used by the sphere function.

"""

import numpy as np
import sys


def get_optimal_position(search_space, f_out):
    """
    Randomly get the optimal position in search_space.
    :param search_space: search space has the form like [[-1, 1], [-1, 1], ...], each element in search_space means the
        search region of that dimension.
    :param f_out: output the optimal position to this file.
    :return:
    """
    optimal_position = []
    with open(f_out, 'w') as f:
        for irange in search_space:
            x = np.random.uniform(irange[0], irange[1])
            optimal_position.append(x)
        f.write(str(optimal_position) + '\n')
    return


if __name__ == '__main__':
    dim_size = eval(sys.argv[2])
    file_name = 'objective_function/optimal_position/' + sys.argv[1] + '_' + str(dim_size) + '.txt'
    search_space = [[-1, 1]] * dim_size
    get_optimal_position(search_space, file_name)


