import numpy as np
from objective_function.base_function import sphere_high, ackley_high, griewank_high, rastrigin_high, schwefel_high


all_epoch = []
epoch = []
epoch_cnt = 0
pcount = 0
epoch_len = 10000
best_result = np.inf


def set_epoch_len(l):
    global epoch_len
    epoch_len = l


def get_all_epoch():
    return all_epoch


def get_epoch_cnt():
    return epoch_cnt


def function_high_log(func_high, x):
    result = func_high(x)
    global all_epoch, epoch, pcount, epoch_cnt, best_result
    if result < best_result:
        epoch.append(result)
        best_result = result
    else:
        epoch.append(epoch[-1])
    pcount += 1
    if pcount == epoch_len:
        all_epoch.append(epoch[:epoch_len])
        epoch_cnt += 1
    return result


def sphere_high_log(x):
    return function_high_log(sphere_high, x)


def ackley_high_log(x):
    return function_high_log(ackley_high, x)


def rastrigin_high_log(x):
    return function_high_log(rastrigin_high, x)


def griewank_high_log(x):
    return function_high_log(griewank_high, x)


def schwefel_high_log(x):
    return function_high_log(schwefel_high, x)


def schwefel_high_for_cmaes(x):
    for i in range(len(x)):
        if x[i] > 500:
            x[i] = 500
        elif x[i] < -500:
            x[i] = -500
    return function_high_log(schwefel_high, x)


def clear_noisy_global():
    global epoch, pcount, epoch_cnt, best_result
    epoch = []
    best_result = np.inf
    pcount = 0
    epoch_cnt = 0
