from objective_function.noisy_function import schwefel_noise_log, clear_noisy_global, get_all_epoch, set_epoch_len
from objective_function.base_function import set_optimal_position
from zoopt import Opt, Objective, Dimension, Parameter
from zoopt.utils.zoo_global import gl
import numpy as np

if __name__ == '__main__':
    repeat_num = 10
    set_optimal_position(
        "objective_function/optimal_position/schwefel/schwefel_20.txt")
    budget = 40000
    set_epoch_len(budget)
    gl.set_seed(666)
    dim_lim = 500
    for i in range(repeat_num):
        dim_size = 20  # dimensions
        dim_regs = [[-1 * dim_lim, dim_lim]] * dim_size  # dimension range
        dim_tys = [True] * dim_size  # dimension type : real
        dim = Dimension(dim_size, dim_regs, dim_tys)  # form up the dimension object
        objective = Objective(lambda sol: schwefel_noise_log(sol.get_x()), dim)  # form up the objective function
        parameter = Parameter(budget=budget, noise_handling=True, suppression=True, non_update_allowed=200,
                              resample_times=50, balance_rate=0.5)

        # parameter = Parameter(budget=budget, noise_handling=True, resampling=True, resample_times=10)
        # parameter.set_positive_size(5)
        sol = Opt.min(objective, parameter)
        clear_noisy_global()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('ZOOpt_exp/log/schwefel/schwefel_noisy.txt', all_epoch)
    print(all_epoch.shape)

