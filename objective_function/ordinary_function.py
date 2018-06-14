from objective_function.base_function import sphere, ackley, rastrigin, griewank, schwefel
import numpy as np


all_epoch = []
epoch = []
epoch_cnt = 0
pcount = 0
epoch_len = 2000
best_result = np.inf


def set_epoch_len(l):
    global epoch_len
    epoch_len = l


def get_all_epoch():
    return all_epoch


def get_epoch_cnt():
    return epoch_cnt


def function_log(func, x):
    result = func(x)
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


def sphere_log(x):
    return function_log(sphere, x)


def ackley_log(x):
    return function_log(ackley, x)


def rastrigin_log(x):
    return function_log(rastrigin, x)


def griewank_log(x):
    return function_log(griewank, x)


def schwefel_log(x):
    return function_log(schwefel, x)


def func_for_cmaes(func, x):
    for i in range(len(x)):
        if x[i] > 500:
            x[i] = 500
        elif x[i] < -500:
            x[i] = -500
    return function_log(schwefel, x)


def clear_noisy_global():
    global epoch, pcount, epoch_cnt, best_result
    epoch = []
    best_result = np.inf
    pcount = 0
    epoch_cnt = 0
