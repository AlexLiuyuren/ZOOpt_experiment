from objective_function.objective_function import noisy_sphere_zoopt, noisy_ackley_zoopt
from zoopt import Opt, Objective, Dimension, Parameter
from zoopt.utils.zoo_global import gl


if __name__ == '__main__':
    repeat_num = 10
    gl.set_seed(666)
    with open('ZOOpt_exp/log/ackley_noisy.txt', 'w') as f:
        for i in range(repeat_num):
            dim_size = 100  # dimensions
            dim_regs = [[-1, 1]] * dim_size  # dimension range
            dim_tys = [True] * dim_size  # dimension type : real
            dim = Dimension(dim_size, dim_regs, dim_tys)  # form up the dimension object
            objective = Objective(noisy_ackley_zoopt, dim)  # form up the objective function
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
            history = objective.get_history_bestsofar()
            for i in range(len(history)):
                history[i] = float(history[i])
            f.write(str(history) + '\n')
