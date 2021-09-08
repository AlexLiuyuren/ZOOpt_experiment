import configparser
import argparse
import os, sys
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.noisy_function import noisy_function_dict
from objective_function.base_function import set_optimal_position, get_all_epoch, base_function_dict
from zoopt import Opt, Objective, Dimension2, ValueType, Parameter, Dimension

from zoopt.utils.zoo_global import gl
import numpy as np
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', default='ackley', help='only support ackley, sphere, rastrigin and schwefel')
    parser.add_argument('-n', '--noise_handling', action='store_true', help="use noise handling mechanism.")
    args = parser.parse_args()
    obj_name = args.objective

    config = configparser.ConfigParser()
    config_name = os.path.join(project_dir, 'objective_function/config/noisy.ini')
    config.read(config_name, encoding='utf-8')

    optimal_position_address = os.path.join(project_dir,  config.get(obj_name, 'optimal_position_address'))
    dim_size = config.getint(obj_name, 'dim_size')
    dim_regs = eval(config.get(obj_name, 'dim_regs'))
    budget = config.getint(obj_name, 'budget')

    repeat = 30
    set_optimal_position(optimal_position_address)
    gl.set_seed(0)
    budget_list = np.arange(0, budget, budget/10) + budget/10
    real_value = np.zeros((repeat, budget_list.shape[0]))
    for i in range(repeat):
        for j in range(len(budget_list)):
            dim = Dimension(dim_size, [dim_regs] * dim_size, [True] * dim_size)
            objective = Objective(lambda sol: noisy_function_dict[obj_name](sol.get_x()), dim)  # form the objective function
            if args.noise_handling:
                parameter = Parameter(budget=budget_list[j], noise_handling=True, suppression=True, non_update_allowed=100,
                                resample_times=20, balance_rate=0.5)
            else:            
                parameter = Parameter(budget=budget, intermediate_result=True, intermediate_freq=1000)
            parameter.set_positive_size(5)
            sol = Opt.min(objective, parameter)
            real_value[i][j] = base_function_dict[args.objective](sol.get_x())
    log_address = os.path.join(project_dir, 'ZOOpt_exp/log/noisy/')
    if args.noise_handling is True:
        file_name = os.path.join(log_address, '{}_nh_{}.txt'.format(obj_name, dim_size))
    else:
        file_name = os.path.join(log_address, '{}_{}.txt'.format(obj_name, dim_size))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, np.array(real_value))
    print(real_value.shape)
    
