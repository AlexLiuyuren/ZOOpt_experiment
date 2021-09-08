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
    config_name = os.path.join(project_dir, 'objective_function/config/scale.ini')
    config.read(config_name, encoding='utf-8')
    print(config.sections())

    optimal_position_address_dir = os.path.join(project_dir,  "objective_function/optimal_position")
    dim_list = eval(config.get(func_name, 'dim_list'))
    dim_regs = eval(config.get(func_name, 'dim_regs'))

    repeat = 20
    values = np.zeros((repeat, len(dim_list)))
    seed = 0
    random.seed(seed)
    np.random.seed(seed)
    for i in range(repeat):
        for j in range(len(dim_list)):
            dim_size = dim_list[j]
            optimal_position_address = os.path.join(optimal_position_address_dir, func_name, "{}_{}.txt".format(func_name, dim_size))
            budget = dim_size * 100
            set_optimal_position(optimal_position_address)
            init_pos = [np.random.uniform(dim_regs[0], dim_regs[1]) for _ in range(dim_size)]
            es = cma.CMAEvolutionStrategy(init_pos, 0.3)  # doctest: +ELLIPSIS
            while get_cnt() < budget:
                print(get_cnt())
                solutions = es.ask()
                es.tell(solutions, [function_cmaes_dict[func_name](x) for x in solutions])
                es.logger.add()
            clear_epoch()
            print("finist repeat: {}, dim: {}, best f: {}".format(i, dim_size, es.best.f))
            values[i, j] = es.best.f
    log_address = os.path.join(project_dir, 'pycma_exp/log/scale/')
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
    
    
