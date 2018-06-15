import numpy as np
from objective_function.base_function import sphere, ackley, rastrigin, griewank, schwefel, set_optimal_position
from objective_function.ordinary_function import func_for_cmaes


def func_noise_creator(func, mu, sigma):
    return lambda x: func(x) + np.random.normal(mu, sigma)


sphere_noisy = func_noise_creator(sphere, 0, 1)
ackley_noisy = func_noise_creator(ackley, 0, 0.1)
rastrigin_noisy = func_noise_creator(rastrigin, 0, 1)
griewank_noisy = func_noise_creator(griewank, 0, 0.1)
schwefel_noisy = func_noise_creator(schwefel, 0, 1)


############################################
# For ZOOpt
def sphere_zoopt(solution):
    x = solution.get_x()
    return sphere(x)


def ackley_zoopt(solution):
    x = solution.get_x()
    return ackley(x)


def sphere_noise_zoopt(solution):
    x = solution.get_x()
    return sphere_noise_log(x)


def ackley_noise_zoopt(solution):
    x = solution.get_x()
    return ackley_noise_log(x)


all_epoch = []
true_epoch = []
epoch_cnt = 0
pcount = 0
epoch_len = 200000
best_result = np.inf


def set_epoch_len(l):
    global epoch_len
    epoch_len = l


def get_all_epoch():
    return all_epoch


def get_epoch_cnt():
    return epoch_cnt


def func_noise_log(func_noisy, func, x):
    result = func_noisy(x)
    true_result = func(x)
    global all_epoch, true_epoch, pcount, epoch_cnt, best_result
    if result < best_result:
        true_epoch.append(true_result)
        best_result = result
    else:
        true_epoch.append(true_epoch[-1])
    pcount += 1
    if pcount == epoch_len:
        all_epoch.append(true_epoch[:epoch_len])
        epoch_cnt += 1
    return result


def sphere_noise_log(x):
    return func_noise_log(sphere_noisy, sphere, x)


def ackley_noise_log(x):
    return func_noise_log(ackley_noisy, ackley, x)


def rastrigin_noise_log(x):
    return func_noise_log(rastrigin_noisy, rastrigin, x)


def griewank_noise_log(x):
    return func_noise_log(griewank_noisy, griewank, x)


def schwefel_noise_log(x):
    return func_noise_log(schwefel_noisy, schwefel, x)


def sphere_noise_for_cmaes(x):
    return func_for_cmaes(sphere_noise_log, 1, x)


def ackley_noise_for_cmaes(x):
    return func_for_cmaes(ackley_noise_log, 1, x)


def griewank_noise_for_cmaes(x):
    return func_for_cmaes(griewank_noise_log, 10, x)


def rastrigin_noise_for_cmaes(x):
    return func_for_cmaes(rastrigin_noise_log, 5, x)


def schwefel_noise_for_cmaes(x):
    return func_for_cmaes(schwefel_noise_log, 500, x)


def clear_noisy_global():
    global epoch, pcount, epoch_cnt, true_epoch, best_result
    true_epoch = []
    best_result = np.inf
    pcount = 0
    epoch_cnt = 0
