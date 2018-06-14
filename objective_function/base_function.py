import numpy as np
optimal_position = []


def set_optimal_position(filename):
    global optimal_position
    with open(filename) as f:
        lines = f.readlines()
        optimal_position = eval(lines[0])
    return optimal_position


def sphere(x):
    """
        Sphere function.
    """
    # print(len(optimal_position))
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


def rastrigin(x):
    """
        rastrigin function
    """
    x_len = len(x)
    seq = 0
    cos = 0
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
    for i in range(x_len):
        seq += (x[i] - optimal_position[i]) * (x[i] - optimal_position[i])
        cos *= np.cos((x[i] - optimal_position[i]) / np.sqrt(i+1))
    value = seq / 4000.0 - cos + 1
    return value


def function_high(func, x):
    """
        Variant of the func function. Dimensions except the first 10 ones have limited impact on the function value.
    """
    x1 = x[:10]
    x2 = x[10:]
    value1 = func(x1)
    value2 = 0
    for i in range(len(x2)):
        value2 += (x2[i] - optimal_position[i + 10]) * (x2[i] - optimal_position[i + 10])
    value2 /= len(x)
    return value1 + value2


def sphere_high(x):
    return function_high(sphere, x)


def ackley_high(x):
    return function_high(ackley, x)


def rastrigin_high(x):
    return function_high(rastrigin, x)


def griewank_high(x):
    return function_high(griewank, x)


def schwefel_high(x):
    x1 = x[:10]
    x2 = x[10:]
    value1 = schwefel(x1)
    value2 = 0
    for i in range(len(x2)):
        value2 += (x2[i] - optimal_position[i + 10]) * (x2[i] - optimal_position[i + 10])
    value2 /= len(x) * len(x)
    return value1 + value2
