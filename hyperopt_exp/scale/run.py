from objective_function.base_function import sphere, ackley, griewank, rastrigin, schwefel, set_optimal_position
from hyperopt import fmin, tpe, hp
import numpy as np

dim_list = [20, 200, 400, 600, 800, 1000]
func_list = [sphere, ackley, griewank, rastrigin, schwefel]
func_name = ['sphere', 'ackley', 'griewank', 'rastrigin', 'schwefel']
search_list = [1, 1, 10, 5, 500]
speed_list = [0.2, 0.2, 2, 1, 100]


def get_optimal_txt(func_name, dim_size):
    txt = "objective_function/optimal_position/" + func_name + "/" + func_name + '_' \
          + str(dim_size) + '.txt'
    return txt


def get_save_txt(func_name, dim_size):
    txt = 'hyperopt_exp/log/' + func_name + "/" + func_name + '_' + str(dim_size) + '.txt'
    return txt


def hyper_opt(func, func_name, dim_size, search_lim, budget):
    optimal_txt = get_optimal_txt(func_name, dim_size)
    set_optimal_position(optimal_txt)
    x = fmin(func, space=[hp.uniform(str(dim), -search_lim, search_lim) for dim in range(dim_size)],
             algo=tpe.suggest, max_evals=budget)
    return x


if __name__ == '__main__':
    x = hyper_opt(ackley, 'ackley', 20, 1, 2000)
    print(x)
    # hyper_opt(sphere_log, 'sphere', 20, 1, 2000)
    # x = hyper_opt(griewank_log, 'griewank', 20, 10, 2000)
    # hyper_opt(rastrigin_log, 'rastrigin', 20, 5, 2000)
    # hyper_opt(schwefel_log, 'schwefel', 20, 500, 2000)