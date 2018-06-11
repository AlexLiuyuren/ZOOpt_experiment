from objective_function.ordinary_function import schwefel_log, clear_noisy_global, get_all_epoch, get_epoch_cnt, set_epoch_len
from objective_function.base_function import set_optimal_position
from zoopt import Opt, Objective, Dimension, Parameter
from zoopt.utils.zoo_global import gl
import numpy as np


if __name__ == '__main__':
    repeat_num = 10
    set_optimal_position(
        "/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/objective_function/optimal_position/schwefel/schwefel_20.txt")
    gl.set_seed(666)
    budget = 2000
    set_epoch_len(budget)
    dim_lim = 500
    for i in range(repeat_num):
        dim_size = 20  # dimensions
        dim_regs = [[-1 * dim_lim, dim_lim]] * dim_size  # dimension range
        dim_tys = [True] * dim_size  # dimension type : real
        dim = Dimension(dim_size, dim_regs, dim_tys)  # form up the dimension object
        objective = Objective(lambda sol: schwefel_log(sol.get_x()), dim)  # form up the objective function
        # 20*dim_size  # number of calls to the objective function
        # suppression=True means optimize with value suppression, which is a noise handling method
        # resampling=True means optimize with re-sampling, which is another common used noise handling method
        # non_update_allowed=500 and resample_times=100 means if the best solution doesn't change for 500 budgets,
        # the best solution will be evaluated repeatedly for 100 times
        # balance_rate is a parameter for exponential weight average of several evaluations of one sample.
        parameter = Parameter(budget=budget)

        # parameter = Parameter(budget=budget, noise_handling=True, resampling=True, resample_times=10)
        sol = Opt.min(objective, parameter)
        sol.print_solution()
        clear_noisy_global()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('ZOOpt_exp/log/schwefel/schwefel_20.txt', all_epoch)
    print(all_epoch.shape)
