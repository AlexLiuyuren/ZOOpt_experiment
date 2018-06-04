import numpy as np


def set_optimal_position(filename):
    with open(filename) as f:
        lines = f.readlines()
        optimal_position = eval(lines[0])
    return optimal_position


optimal_position = set_optimal_position('objective_function/optimal_position/sphere_100.txt')


# for ZOOpt
def sphere_zoopt(solution):
    x = solution.get_x()
    assert len(x) == len(optimal_position)
    value = 0
    for i in range(len(x)):
        value += (x[i] - optimal_position[i]) * (x[i] - [optimal_position[i]])
    return value


def sphere_noise_creator_zoopt(mu, sigma):
    return lambda solution: sphere_zoopt(solution) + np.random.normal(mu, sigma, 1)


def ackley_zoopt(solution):
    x = solution.get_x()
    bias = 0.2
    seq = 0
    cos = 0
    for i in range():
    ave_seq = sum([(i - bias) * (i - bias) for i in x]) / len(x)
    ave_cos = sum([np.cos(2.0*np.pi*(i-bias)) for i in x]) / len(x)
    value = -20 * np.exp(-0.2 * np.sqrt(ave_seq)) - np.exp(ave_cos) + 20.0 + np.e
    return value


def ackley_noise_creator_zoopt(mu, sigma):
    return lambda solution: ackley_zoopt(solution) + np.random.normal(mu, sigma, 1)


noisy_sphere_zoopt = sphere_noise_creator_zoopt(0, 1)
noisy_ackley_zoopt = ackley_noise_creator_zoopt(0, 0.1)

