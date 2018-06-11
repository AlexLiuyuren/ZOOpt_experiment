from objective_function.high_dim_function import rastrigin_high_log, clear_noisy_global, get_all_epoch, get_epoch_cnt, set_epoch_len
from objective_function.base_function import set_optimal_position
from zoopt import Opt, Objective, Dimension, Parameter
from zoopt.utils.zoo_global import gl
import numpy as np


if __name__ == '__main__':
    repeat_num = 10
    set_optimal_position(
        "/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/objective_function/optimal_position/rastrigin/rastrigin_10000.txt")
    gl.set_seed(666)
    budget = 10000
    set_epoch_len(budget)
    dim_lim = 5
    for i in range(repeat_num):
        dim_size = 10000  # dimensions
        dim_regs = [[-1 * dim_lim, dim_lim]] * dim_size  # dimension range
        dim_tys = [True] * dim_size  # dimension type : real
        dim = Dimension(dim_size, dim_regs, dim_tys)  # form up the dimension object
        objective = Objective(lambda sol: rastrigin_high_log(sol.get_x()), dim)  # form up the objective function
        parameter = Parameter(budget=budget)

        # parameter = Parameter(budget=budget, noise_handling=True, resampling=True, resample_times=10)
        # parameter.set_positive_size(5)
        sol = Opt.min(objective, parameter)
        clear_noisy_global()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('ZOOpt_exp/log/rastrigin/rastrigin_10000.txt', all_epoch)
    print(all_epoch.shape)
