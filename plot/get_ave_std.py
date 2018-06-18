import numpy as np
import sys


def get(filename, line):
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


def get_ave_std(package_name, func_name, append_name):
    filename = package_name + '/log/' + func_name + '/' + func_name + '_' + append_name + '.txt'
    result = get(filename, 10)
    save_name = package_name + '/log/' + func_name + '/ave_std/' + func_name + '_' + append_name + '.txt'
    with open(save_name, 'w') as f:
        f.truncate()
    np.savetxt(save_name, result)


def get_ave_std_scale(package_name, func_name):
    filename = package_name + '/log/' + func_name + '/' + func_name + '_scale.txt'
    result = get(filename, 5)
    save_name = package_name + '/log/' + func_name + '/ave_std/' + func_name + '_scale.txt'
    with open(save_name, 'w') as f:
        f.truncate()
    np.savetxt(save_name, result)


def ZOOpt_ave_std(func_name):
    # get_ave_std('ZOOpt_exp', func_name, '20')
    # get_ave_std('ZOOpt_exp', func_name, '10000')
    # get_ave_std('ZOOpt_exp', func_name, '10000_sre')
    get_ave_std('ZOOpt_exp', func_name, 'noisy')
    get_ave_std('ZOOpt_exp', func_name, 'noisy_without_nh')
    # get_ave_std_scale('ZOOpt_exp', func_name)


def CMAES_ave_std(func_name):
    # get_ave_std('CMAES_exp', func_name, '20')
    # get_ave_std('CMAES_exp', func_name, '10000')
    get_ave_std('CMAES_exp', func_name, 'noisy')
    get_ave_std('CMAES_exp', func_name, 'noisy_without_nh')
    # get_ave_std_scale('CMAES_exp', func_name)


def DEAP_ave_std(func_name):
    get_ave_std('DEAP_exp', func_name, '20')
    # get_ave_std('DEAP_exp', func_name, '10000')
    get_ave_std('DEAP_exp', func_name, 'noisy')
    # get_ave_std_scale('DEAP_exp', func_name)


def hyperopt_ave_std(func_name):
    get_ave_std('hyperopt_exp', func_name, '20')


if __name__ == '__main__':
    # ZOOpt_ave_std('griewank')
    # ZOOpt_ave_std('rastrigin')
    # ZOOpt_ave_std('schwefel')
    # ZOOpt_ave_std('ackley')
    # ZOOpt_ave_std('sphere')

    # CMAES_ave_std('griewank')
    CMAES_ave_std('rastrigin')
    CMAES_ave_std('schwefel')
    # CMAES_ave_std('ackley')
    # CMAES_ave_std('sphere')

    # DEAP_ave_std('griewank')
    # DEAP_ave_std('rastrigin')
    # DEAP_ave_std('schwefel')
    # DEAP_ave_std('ackley')
    # DEAP_ave_std('sphere')

    # hyperopt_ave_std('griewank')
    # hyperopt_ave_std('rastrigin')
    # hyperopt_ave_std('schwefel')
    # hyperopt_ave_std('ackley')
    # hyperopt_ave_std('sphere')



