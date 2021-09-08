"""
Type the following command in the command line or terminal and  a file sphere_100_position.txt will be generated.
python get_optimal_position.py sphere 100.
100 means the dimension size is 100.
sphere means the optimal position is used by the sphere function.

"""

import numpy as np
import argparse, os, random

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
            x = np.random.uniform(0.2 * irange[0], 0.2 * irange[1])
            optimal_position.append(x)
        f.write(str(optimal_position) + '\n')
    return


if __name__ == '__main__':
    seed = 0
    np.random.seed(seed)
    random.seed(seed)
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', help="can only be sphere, ackley, rastrigin, griewank or schwefel", default='ackley')
    parser.add_argument('-d', '--dimension', type=int, default=20, help='the dimension size of the search space')
    args = parser.parse_args()
    dim_size = args.dimension
    search_region = {
        'sphere': [[-1, 1]] * dim_size,
        'ackley': [[-1, 1]] * dim_size,
        'rastrigin': [[-5, 5]] * dim_size,
        'griewank': [[-10, 10]] * dim_size,
        'schwefel': [[-500, 500]] * dim_size
    }
    dir_name = os.path.join('objective_function/optimal_position', args.objective)
    os.makedirs(dir_name, exist_ok=True)
    file_name = os.path.join(dir_name, "{}_{}.txt".format(args.objective, dim_size))
    get_optimal_position(search_region[args.objective], file_name)


