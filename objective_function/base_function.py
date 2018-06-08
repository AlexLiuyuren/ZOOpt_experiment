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


def sphere_high(x):
    """
        Variant of the sphere function. Dimensions except the first 10 ones have limited impact on the function value.
    """
    x1 = x[:10]
    x2 = x[10:]
    j = 0
    value1 = 0
    for i in range(len(x1)):
        value1 += (x1[i] - optimal_position[i]) * (x1[i] - optimal_position[i])
    value2 = 0
    for i in range(len(x2)):
        value2 += (x2[i] - optimal_position[i + 10]) * (x2[i] - optimal_position[i + 10])
    value2 /= len(x)
    return value1 + value2


def ackley_high(x):
    """
        Variant of the ackley function. Dimensions except the first 10 ones have limited impact on the function value.
    """
    x1 = x[:10]
    x2 = x[10:]
    ave_seq = 0
    for i in range(len(x1)):
        ave_seq += (x1[i] - optimal_position[i]) * (x1[i] - optimal_position[i])
    ave_seq = ave_seq/len(x1)
    ave_cos = 0
    for i in range(len(x1)):
        ave_cos += np.cos(2.0 * np.pi * (x1[i] - optimal_position[i]))
    ave_cos = ave_cos / len(x1)
    value = -20 * np.exp(-0.2 * np.sqrt(ave_seq)) - np.exp(ave_cos) + 20.0 + np.e
    ave_seq2 = 0
    for i in range(len(x2)):
        ave_seq2 += (x2[i]-optimal_position[i + 10]) * (x2[i]-optimal_position[i + 10])
    ave_seq2 = ave_seq2 / len(x)
    value2 = ave_seq2
    return value + value2
