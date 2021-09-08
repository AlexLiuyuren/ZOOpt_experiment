import numpy as np
import gc

global optimal_position, all_epoch, epoch, best_result
optimal_position = []
all_epoch = []
epoch = []
best_result = np.inf
best_sol = []
cnt = 0

def set_optimal_position(filename):
    global optimal_position
    with open(filename) as f:
        lines = f.readlines()
        optimal_position = eval(lines[0])
    return optimal_position

def get_optimal_position():
    global optimal_position
    return optimal_position

def get_cnt():
    global cnt
    return cnt

def sphere(x):
    """
        Sphere function.
    """
    # print(len(optimal_position))
    value = 0
    optimal_position = get_optimal_position()
    for i in range(len(x)):
        value += (x[i] - optimal_position[i]) * (x[i] - optimal_position[i])
    return value


def ackley(x):
    """
        ackley function
    """
    x_len = len(x)
    seq = 0
    cos = 0
    optimal_position = get_optimal_position()
    for i in range(x_len):
        seq += (x[i] - optimal_position[i]) * (x[i] - optimal_position[i])
        cos += np.cos(2.0 * np.pi * (x[i] - optimal_position[i]))
    ave_seq = seq / x_len
    ave_cos = cos / x_len
    value = -20 * np.exp(-0.2 * np.sqrt(ave_seq)) - np.exp(ave_cos) + 20.0 + np.e
    return value


def rastrigin(x):
    """
        rastrigin function
    """
    x_len = len(x)
    seq = 0
    cos = 0
    optimal_position = get_optimal_position()
    for i in range(x_len):
        seq += (x[i] - optimal_position[i]) * (x[i] - optimal_position[i])
        cos += np.cos(2.0 * np.pi * (x[i] - optimal_position[i]))
    value = 10 * x_len + seq - 10 * cos
    return value


def schwefel(x):
    """
        schwefel function
    """
    x_len = len(x)
    value = 0
    for i in range(x_len):
        value += x[i] * np.sin(np.sqrt(np.abs(x[i])))
    return 418.9829 * x_len - value

def griewank(x):
    """
        griewank function
    """
    x_len = len(x)
    seq = 0
    cos = 1
    optimal_position = get_optimal_position()
    for i in range(x_len):
        seq += (x[i] - optimal_position[i]) * (x[i] - optimal_position[i])
        cos *= np.cos((x[i] - optimal_position[i]) / np.sqrt(i+1))
    value = seq / 4000.0 - cos + 1
    return value

base_function_dict = {
    'sphere': sphere,
    'ackley': ackley,
    'rastrigin': rastrigin,
    'griewank': griewank,
    'schwefel': schwefel
}

def function_log(func, x):
    result = func(x)
    global cnt
    cnt += 1
    best_result = get_best_result()
    if result < best_result:
        append_epoch(result)
        update_best_result(x, result)
    else:
        append_epoch_with_last_item()
    return result

def func_for_cmaes(func, lim, x):
    x = np.where(x > lim, lim, x)
    x = np.where(x < -lim, -lim, x)
    return func(x)

def get_best_result():
    global best_result
    return best_result

def append_all_epoch():
    global all_epoch, epoch
    all_epoch.append(epoch)
    clear_epoch()

def append_epoch(result):
    global epoch
    epoch.append(result)

def append_epoch_with_last_item():
    global epoch
    assert len(epoch) > 0
    epoch.append(epoch[-1])

def update_best_result(sol, result):
    global best_result, best_sol
    best_sol = sol
    best_result = result

def get_all_epoch():
    global all_epoch
    return all_epoch
    
def clear_epoch():
    global epoch, best_result, best_sol, cnt
    epoch = []
    best_result = np.inf
    best_sol = []
    cnt =0

def get_epoch():
    global epoch
    return epoch

def epoch_first_items(num):
    global epoch
    epoch = epoch[:num]
    return  epoch

def clear_all_epoch():
    global epoch, best_result, all_epoch, cnt
    epoch = []
    all_epoch = []
    best_result = np.inf
    cnt = 0
    gc.collect()

def get_best_sol():
    global best_sol
    return best_sol

def set_best_sol(sol):
    global best_sol
    best_sol = sol