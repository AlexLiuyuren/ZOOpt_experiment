from objective_function.noisy_function import griewank_noise_log, clear_noisy_global, get_all_epoch, set_epoch_len
from objective_function.base_function import set_optimal_position
from zoopt import Opt, Objective, Dimension, Parameter
from zoopt.utils.zoo_global import gl
import numpy as np

if __name__ == '__main__':
    repeat_num = 10
    set_optimal_position(
        "objective_function/optimal_position/griewank/griewank_100.txt")
    gl.set_seed(666)
    budget = 200000
    set_epoch_len(budget)
    dim_lim = 10
    for i in range(repeat_num):
        dim_size = 100  # dimensions
        dim_regs = [[-1 * dim_lim, dim_lim]] * dim_size  # dimension range
        dim_tys = [True] * dim_size  # dimension type : real
        dim = Dimension(dim_size, dim_regs, dim_tys)  # form up the dimension object
        objective = Objective(lambda sol: griewank_noise_log(sol.get_x()), dim)  # form up the objective function
        parameter = Parameter(budget=budget)
        sol = Opt.min(objective, parameter)
        clear_noisy_global()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('ZOOpt_exp/log/griewank/griewank_noisy_without_handling.txt', all_epoch)
    print(all_epoch.shape)

