import configparser
import os, sys, random, argparse, cma
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.low_dim_function import function_dict
from objective_function.base_function import set_optimal_position, append_all_epoch, get_all_epoch, get_cnt, clear_epoch, epoch_first_items, get_best_result
from zoopt import Opt, Objective, Dimension2, ValueType, Parameter, Dimension
from zoopt.utils.zoo_global import gl

import numpy as np


def minimize(func_name):
    config = configparser.ConfigParser()
    config_name = os.path.join(project_dir, 'objective_function/config/scale.ini')
    config.read(config_name, encoding='utf-8')
    print(config.sections())

    optimal_position_address_dir = os.path.join(project_dir,  "objective_function/optimal_position")
    dim_list = eval(config.get(func_name, 'dim_list'))
    dim_regs = eval(config.get(func_name, 'dim_regs'))

    repeat = 20
    values = np.zeros((repeat, len(dim_list)))
    seed = 0
    gl.set_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    for i in range(repeat):
        for j in range(len(dim_list)):
            dim_size = dim_list[j]
            optimal_position_address = os.path.join(optimal_position_address_dir, func_name, "{}_{}.txt".format(func_name, dim_size))
            set_optimal_position(optimal_position_address)
            budget = dim_size * 100
            dim = Dimension2([(ValueType.CONTINUOUS, dim_regs, 1e-6)]*dim_size)
            objective = Objective(lambda sol: function_dict[obj_name](sol.get_x()), dim)
            parameter = Parameter(budget=budget, intermediate_result=True, intermediate_freq=100)
            sol = Opt.min(objective, parameter)
            clear_epoch()
            print("finist repeat: {}, dim: {}, best f: {}".format(i, dim_size, sol.get_value()))
            values[i][j] = sol.get_value()
    log_address = os.path.join(project_dir, 'ZOOpt_exp/log/scale/')
    file_name = os.path.join(log_address, '{}_2.txt'.format(obj_name))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, values)
    print(values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', default='ackley', help='only support ackley, sphere, rastrigin and schwefel')
    args = parser.parse_args()
    obj_name = args.objective
    minimize(obj_name)
    
    
