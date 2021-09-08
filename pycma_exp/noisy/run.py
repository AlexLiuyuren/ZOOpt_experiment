import configparser
import os, sys, random, argparse, cma
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.noisy_function import noisy_function_cmaes_dict
from objective_function.base_function import set_optimal_position, append_all_epoch, get_all_epoch, get_cnt, clear_epoch, epoch_first_items, base_function_dict
import numpy as np

def optimize_with_noise_handler(budget, func, dim_regs, dim_size):
    init_pos = [np.random.uniform(dim_regs[0], dim_regs[1]) for _ in range(dim_size)]
    es = cma.CMAEvolutionStrategy(init_pos, 0.5)  #doctest: +ELLIPSIS
    nh = cma.NoiseHandler(es.N, maxevals=[1, 1, 30])
    while get_cnt() < budget:
        print(get_cnt())
        X, fit_vals = es.ask_and_eval(func, evaluations=nh.evaluations)
        es.tell(X, fit_vals)  # prepare for next iteration
        es.sigma *= nh(X, fit_vals, func, es.ask)  # see method __call__
        es.countevals += nh.evaluations_just_done  # this is a hack, not important though
        es.logger.add(more_data=[nh.evaluations, nh.noiseS])  # add a data point
    print(es.best.f)
    clear_epoch()
    return es.best.x

def optimize_without_noise_handler(budget, func, dim_regs, dim_size):
    init_pos = [np.random.uniform(dim_regs[0], dim_regs[1]) for _ in range(dim_size)]
    es = cma.CMAEvolutionStrategy(init_pos, 0.3)  # doctest: +ELLIPSIS
    while get_cnt() < budget:
        print(get_cnt())
        solutions = es.ask()
        es.tell(solutions, [func(x) for x in solutions])
        es.logger.add()
    print(es.best.f)
    clear_epoch()
    return es.best.x


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', default='ackley', help='only support ackley, sphere, rastrigin and schwefel')
    parser.add_argument('-n', '--noise_handling', action='store_true', help="use noise handling mechanism.")
    args = parser.parse_args()
    obj_name = args.objective
    
    config = configparser.ConfigParser()
    config_name = os.path.join(project_dir, 'objective_function/config/noisy.ini')
    config.read(config_name, encoding='utf-8')
    print(config.sections())

    optimal_position_address = os.path.join(project_dir,  config.get(obj_name, 'optimal_position_address'))
    dim_size = config.getint(obj_name, 'dim_size')
    dim_regs = eval(config.get(obj_name, 'dim_regs'))
    budget = config.getint(obj_name, 'budget')

    repeat = 30
    set_optimal_position(optimal_position_address)
    seed = 0
    budget_list = np.arange(0, budget, budget/10) + budget/10
    random.seed(seed)
    np.random.seed(seed)
    real_value = np.zeros((repeat, budget_list.shape[0]))
    for i in range(repeat):
        for j in range(len(budget_list)):
            func = noisy_function_cmaes_dict[obj_name]
            if args.noise_handling is True:
                best_x = optimize_with_noise_handler(budget_list[j], func, dim_regs, dim_size)
            else:
                best_x = optimize_without_noise_handler(budget_list[j], func, dim_regs, dim_size)
            real_value[i][j] = base_function_dict[args.objective](best_x)
    log_address = os.path.join(project_dir, 'pycma_exp/log/noisy/')
    if args.noise_handling is True:
        file_name = os.path.join(log_address, '{}_nh_{}.txt'.format(obj_name, dim_size))
    else:
        file_name = os.path.join(log_address, '{}_{}.txt'.format(obj_name, dim_size))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, real_value)
    print(real_value.shape)
    
    
