from hyperopt import fmin, tpe, hp
import numpy as np
from objective_function.ordinary_function import ackley_log, sphere_log, griewank_log, rastrigin_log, schwefel_log, \
    clear_noisy_global, get_all_epoch
from objective_function.base_function import set_optimal_position


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
    repeat = 10
    for i in range(repeat):
        print(i)
        x = fmin(func, space=[hp.uniform(str(dim), -search_lim, search_lim) for dim in range(dim_size)],
                 algo=tpe.suggest, max_evals=budget)
        clear_noisy_global()
    all_epoch = np.array(get_all_epoch())
    save_txt = get_save_txt(func_name, dim_size)
    np.savetxt(save_txt, all_epoch)


if __name__ == '__main__':
    # hyper_opt(ackley_log, 'ackley', 20, 1, 2000)
    # hyper_opt(sphere_log, 'sphere', 20, 1, 2000)
    hyper_opt(griewank_log, 'griewank', 20, 10, 2000)
    hyper_opt(rastrigin_log, 'rastrigin', 20, 5, 2000)
    hyper_opt(schwefel_log, 'schwefel', 20, 500, 2000)



