import numpy as np


def set_optimal_position(filename):
    with open(filename) as f:
        lines = f.readlines()
        optimal_position = eval(lines[0])
    return optimal_position


optimal_position = set_optimal_position('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/objective_function/optimal_position/sphere_100.txt')


def sphere(x):
    """
        Sphere function.
    """
    assert len(x) == len(optimal_position)
    value = 0
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

    for i in range(x_len):
        seq += (x[i] - optimal_position[i]) * (x[i] - optimal_position[i])
        cos += np.cos(2.0 * np.pi * (x[i] - optimal_position[i]))
    ave_seq = seq / x_len
    ave_cos = cos / x_len
    value = -20 * np.exp(-0.2 * np.sqrt(ave_seq)) - np.exp(ave_cos) + 20.0 + np.e
    return value


def sphere_noise_creator(mu, sigma):
    return lambda x: sphere(x) + np.random.normal(mu, sigma)


def ackley_noise_creator(mu, sigma):
    return lambda x: ackley(x) + np.random.normal(mu, sigma)


noisy_sphere = sphere_noise_creator(0, 1)
noisy_ackley = ackley_noise_creator(0, 0.1)


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


def get_all_epoch():
    return all_epoch


def get_epoch_cnt():
    return epoch_cnt


def sphere_noise_log(x):
    result = noisy_sphere(x)
    true_result = sphere(x)
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


def ackley_noise_log(x):
    result = noisy_ackley(x)
    true_result = ackley(x)
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


def clear_noisy_global():
    global epoch, pcount, epoch_cnt, true_epoch, best_result
    true_epoch = []
    best_result = np.inf
    pcount = 0
    epoch_cnt = 0
