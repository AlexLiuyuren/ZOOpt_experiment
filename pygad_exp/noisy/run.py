import configparser, argparse, os, sys, pygad
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.noisy_function import noisy_function_dict
from objective_function.base_function import clear_epoch, set_optimal_position, get_all_epoch, get_epoch, base_function_dict, get_best_sol
from objective_function.low_dim_function import function_dict
from zoopt import Opt, Objective, Dimension2, ValueType, Parameter, Dimension

from zoopt.utils.zoo_global import gl
import numpy as np
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', default='ackley', help='only support ackley, sphere, rastrigin and schwefel')
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
    budget_list = np.arange(0, budget, budget/10) + budget/10
    real_value = np.zeros((repeat, budget_list.shape[0]))
    def fitness_func(solution, solution_idx):
        # Calculating the fitness value of each solution in the current population.
        output = -noisy_function_dict[obj_name](solution)
        return output

    sol_per_pop = 50 # Number of solutions in the population.
    num_parents_mating = 7
    
    num_genes = dim_size
    gene_space = [{'low': dim_regs[0], 'high': dim_regs[1]}] * dim_size

    for i in range(repeat):
        for j in range(len(budget_list)):
            num_generations = int(budget_list[j] // sol_per_pop) # Number of generations.
            ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop, 
                       gene_space=gene_space,
                       num_genes=num_genes)
            #   Running the GA to optimize the parameters of the function.
            ga_instance.run()
            real_value[i, j] = base_function_dict[args.objective](get_best_sol())
            clear_epoch()
            print(real_value)
    log_address = os.path.join(project_dir, 'pygad_exp/log/noisy/')
    file_name = os.path.join(log_address, '{}_{}.txt'.format(obj_name, dim_size))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, np.array(real_value))
    print(real_value.shape)
    
