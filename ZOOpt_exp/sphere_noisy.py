from objective_function.noisy_function import sphere_noise_zoopt, clear_noisy_global, get_all_epoch
from zoopt import Opt, Objective, Dimension, Parameter
from zoopt.utils.zoo_global import gl
import numpy as np

if __name__ == '__main__':
    repeat_num = 10
    gl.set_seed(666)
    for i in range(repeat_num):
        dim_size = 100  # dimensions
        dim_regs = [[-1, 1]] * dim_size  # dimension range
        dim_tys = [True] * dim_size  # dimension type : real
        dim = Dimension(dim_size, dim_regs, dim_tys)  # form up the dimension object
        objective = Objective(sphere_noise_zoopt, dim)  # form up the objective function
        budget = 200000  # 20*dim_size  # number of calls to the objective function
        # suppression=True means optimize with value suppression, which is a noise handling method
        # resampling=True means optimize with re-sampling, which is another common used noise handling method
        # non_update_allowed=500 and resample_times=100 means if the best solution doesn't change for 500 budgets,
        # the best solution will be evaluated repeatedly for 100 times
        # balance_rate is a parameter for exponential weight average of several evaluations of one sample.
        parameter = Parameter(budget=budget, noise_handling=True, suppression=True, non_update_allowed=200,
                              resample_times=50, balance_rate=0.5)

        # parameter = Parameter(budget=budget, noise_handling=True, resampling=True, resample_times=10)
        parameter.set_positive_size(5)
        sol = Opt.min(objective, parameter)
        clear_noisy_global()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('ZOOpt_exp/log/sphere_noisy.txt', all_epoch)
    print(all_epoch.shape)

