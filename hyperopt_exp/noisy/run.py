import os, sys, random, argparse, cma, configparser, operator
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.noisy_function import function_dict
from objective_function.base_function import set_optimal_position, append_all_epoch, get_all_epoch, get_cnt, clear_epoch, epoch_first_items
from hyperopt import fmin, tpe, hp
import numpy as np


def minimize(func_name):
    config = configparser.ConfigParser()
    config_name = os.path.join(project_dir, 'objective_function/config/noisy.ini')
    config.read(config_name, encoding='utf-8')
    print(config.sections())

    optimal_position_address = os.path.join(project_dir,  config.get(obj_name, 'optimal_position_address'))
    dim_size = config.getint(obj_name, 'dim_size')
    dim_regs = eval(config.get(obj_name, 'dim_regs'))
    budget = config.getint(obj_name, 'budget')
    set_optimal_position(optimal_position_address)

    seed = 0
    random.seed(seed)
    np.random.seed(seed)
    repeat = 10
    for _ in range(repeat):
        x = fmin(function_dict[func_name], space=[hp.uniform(str(dim), dim_regs[0], dim_regs[1]) for dim in range(dim_size)], algo=tpe.suggest, max_evals=budget)
        epoch_first_items(budget)
        append_all_epoch()
    all_epoch = np.array(get_all_epoch())
    log_address = os.path.join(project_dir, 'hyperopt_exp/log/noisy/')
    file_name = os.path.join(log_address, '{}_{}.txt'.format(obj_name, dim_size))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, all_epoch)
    print(all_epoch.shape)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', default='ackley', help='only support ackley, sphere, rastrigin and schwefel')
    args = parser.parse_args()
    obj_name = args.objective
    minimize(obj_name)
    
    
