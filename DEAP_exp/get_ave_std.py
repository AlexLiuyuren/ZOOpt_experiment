import numpy as np


def get_ave_std(filename, line):
    data = np.loadtxt(filename)
    data = data[:line]
    data = data.T
    ave = []
    std = []
    for list in data:
        ave.append(np.mean(list))
        std.append(np.std(list))
    result = np.array([ave, std])
    return result


if __name__ == '__main__':
    line = 10
    # result_ackley = get_ave_std('DEAP_exp/log/ackley_noisy.txt', line)
    # np.savetxt('DEAP_exp/log/ackley_noisy_ave_std.txt', result_ackley)
    # result_sphere = get_ave_std('DEAP_exp/log/sphere_noisy.txt', line)
    # np.savetxt('DEAP_exp/log/sphere_noisy_ave_std.txt', result_sphere)

    result_ackley = get_ave_std('DEAP_exp/log/ackley_20.txt', line)
    np.savetxt('DEAP_exp/log/ackley_20_ave_std.txt', result_ackley)
    # result_sphere = get_ave_std('DEAP_exp/log/sphere_20.txt', line)
    # np.savetxt('DEAP_exp/log/sphere_20_ave_std.txt', result_sphere)
