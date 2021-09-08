import configparser
import os, sys, random, argparse, cma
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.low_dim_function import function_cmaes_dict
from objective_function.base_function import set_optimal_position, append_all_epoch, get_all_epoch, get_cnt, clear_epoch, epoch_first_items
import numpy as np


def minimize(func_name):
    config = configparser.ConfigParser()
    config_name = os.path.join(project_dir, 'objective_function/config/low_dim.ini')
    config.read(config_name, encoding='utf-8')
    print(config.sections())

    optimal_position_address = os.path.join(project_dir,  config.get(func_name, 'optimal_position_address'))
    dim_size = config.getint(func_name, 'dim_size')
    dim_regs = eval(config.get(func_name, 'dim_regs'))
    budget = config.getint(func_name, 'budget')

    repeat = 30
    set_optimal_position(optimal_position_address)
    seed = 0
    random.seed(seed)
    np.random.seed(seed)
    for i in range(repeat):
        init_pos = [np.random.uniform(dim_regs[0], dim_regs[1]) for _ in range(dim_size)]
        es = cma.CMAEvolutionStrategy(init_pos, 0.5)  # doctest: +ELLIPSIS
        while get_cnt() < budget:
            solutions = es.ask()
            es.tell(solutions, [function_cmaes_dict[func_name](x) for x in solutions])
            es.logger.add()
        epoch_first_items(budget)
        append_all_epoch()
        sol = es.result_pretty()
        es.result_pretty()
    all_epoch = np.array(get_all_epoch())
    log_address = os.path.join(project_dir, 'pycma_exp/log/low_dim/')
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
    
    
