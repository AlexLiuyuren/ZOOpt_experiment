import numpy as np
from objective_function.base_function import sphere, ackley, rastrigin, griewank, schwefel, set_optimal_position


# set_optimal_position('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/objective_function/optimal_position/sphere_100.txt')


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


############################################
# objective functions which records intermediate result.
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


def schwefel_noise_for_cmaes(x):
    for i in range(len(x)):
        if x[i] > 500:
            x[i] = 500
        elif x[i] < -500:
            x[i] = -500
    return schwefel_noise_log(x)


def clear_noisy_global():
    global epoch, pcount, epoch_cnt, true_epoch, best_result
    true_epoch = []
    best_result = np.inf
    pcount = 0
    epoch_cnt = 0
