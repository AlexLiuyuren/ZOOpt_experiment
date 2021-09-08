import configparser
import argparse
import os, sys
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.low_dim_function import function_dict
from objective_function.base_function import set_optimal_position, append_all_epoch, get_all_epoch
from zoopt import Opt, Objective, Dimension2, ValueType, Parameter, Dimension
# from zoopt import Opt, Objective, Parameter, Dimension

from zoopt.utils.zoo_global import gl
import numpy as np
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', default='ackley', help='only support ackley, sphere, rastrigin and schwefel')
    args = parser.parse_args()
    obj_name = args.objective

    config = configparser.ConfigParser()
    config_name = os.path.join(project_dir, 'objective_function/config/low_dim.ini')
    config.read(config_name, encoding='utf-8')
    print(config.sections())

    optimal_position_address = os.path.join(project_dir,  config.get(obj_name, 'optimal_position_address'))
    dim_size = config.getint(obj_name, 'dim_size')
    dim_regs = eval(config.get(obj_name, 'dim_regs'))
    budget = config.getint(obj_name, 'budget')

    repeat = 30
    set_optimal_position(optimal_position_address)
    seed = 0
    gl.set_seed(seed)
    for i in range(repeat):
        dim = Dimension2([(ValueType.CONTINUOUS, dim_regs, 1e-6)]*dim_size)
        # dim = Dimension(dim_size, [dim_regs] * dim_size, [True] * dim_size)
        objective = Objective(lambda sol: function_dict[obj_name](sol.get_x()), dim)  # form up the objective function
        parameter = Parameter(budget=budget, intermediate_result=True, intermediate_freq=100)
        sol = Opt.min(objective, parameter)
        append_all_epoch()
    all_epoch = np.array(get_all_epoch())
    log_address = os.path.join(project_dir, 'ZOOpt_exp/log/low_dim/')
    file_name = os.path.join(log_address, '{}_{}.txt'.format(obj_name, dim_size))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, all_epoch)
    print(all_epoch.shape)
    
    
