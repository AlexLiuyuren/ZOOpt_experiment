import numpy as np

budget = 200000


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
    # result_ackley = get_ave_std('ZOOpt_exp/log/ackley_20.txt', line)
    # np.savetxt('ZOOpt_exp/log/ackley_noisy_ave_std.txt', result_ackley)
    # result_sphere = get_ave_std('ZOOpt_exp/log/sphere_20.txt', line)
    # np.savetxt('ZOOpt_exp/log/sphere_noisy_ave_std.txt', result_sphere)
    # result_ackley = get_ave_std('ZOOpt_exp/log/ackley_noisy.txt', line)
    # np.savetxt('ZOOpt_exp/log/ackley_noisy_ave_std.txt', result_ackley)
    # result_sphere = get_ave_std('ZOOpt_exp/log/sphere_noisy.txt', line)
    # np.savetxt('ZOOpt_exp/log/sphere_noisy_ave_std.txt', result_sphere)
    result_ackley = get_ave_std('ZOOpt_exp/log/ackley_noisy_without_handling.txt', line)
    np.savetxt('ZOOpt_exp/log/ackley_noisy_no_ave_std.txt', result_ackley)
    result_sphere = get_ave_std('ZOOpt_exp/log/sphere_noisy_without_handling.txt', line)
    np.savetxt('ZOOpt_exp/log/sphere_noisy_no_ave_std.txt', result_sphere)
    # result_ackley = get_ave_std('ZOOpt_exp/log/ackley_high_dim.txt', line)
    # np.savetxt('ZOOpt_exp/log/ackley_high_dim_ave_std.txt', result_ackley)
    # result_sphere = get_ave_std('ZOOpt_exp/log/sphere_high_dim.txt', line)
    # np.savetxt('ZOOpt_exp/log/sphere_high_dim_ave_std.txt', result_sphere)
    # result_ackley = get_ave_std('ZOOpt_exp/log/ackley_high_dim_sre.txt', line)
    # np.savetxt('ZOOpt_exp/log/ackley_high_dim_sre_ave_std.txt', result_ackley)
    # result_sphere = get_ave_std('ZOOpt_exp/log/sphere_high_dim_sre.txt', line)
    # np.savetxt('ZOOpt_exp/log/sphere_high_dim_sre_ave_std.txt', result_sphere)

