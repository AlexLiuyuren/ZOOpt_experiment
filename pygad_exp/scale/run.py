import configparser, os, sys, random, argparse, pygad
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.low_dim_function import function_dict
from objective_function.base_function import set_optimal_position, append_all_epoch, get_all_epoch, get_cnt, clear_epoch, epoch_first_items, get_best_result, get_epoch

import numpy as np


def minimize(func_name):
    config = configparser.ConfigParser()
    config_name = os.path.join(project_dir, 'objective_function/config/scale.ini')
    config.read(config_name, encoding='utf-8')
    print(config.sections())

    optimal_position_address_dir = os.path.join(project_dir,  "objective_function/optimal_position")
    dim_list = eval(config.get(func_name, 'dim_list'))
    dim_regs = eval(config.get(func_name, 'dim_regs'))

    repeat = 30
    values = np.zeros((repeat, len(dim_list)))
    seed = 0
    random.seed(seed)
    np.random.seed(seed)
    def fitness_func(solution, solution_idx):
        # Calculating the fitness value of each solution in the current population.
        output = -function_dict[obj_name](solution)
        return output
    fitness_function = fitness_func

    for i in range(repeat):
        for j in range(len(dim_list)):
            num_genes = dim_size = dim_list[j]
            gene_space = [{'low': dim_regs[0], 'high': dim_regs[1]}] * dim_size
            if dim_list[j] == 20:
                sol_per_pop = 20
                num_parents_mating = 5
            else:
                sol_per_pop = 50
                num_parents_mating = 7
            budget = 100 * dim_size
            num_generations = int(budget // sol_per_pop)
            optimal_position_address = os.path.join(optimal_position_address_dir, func_name, "{}_{}.txt".format(func_name, dim_size))
            set_optimal_position(optimal_position_address)
            ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop, 
                       gene_space=gene_space,
                       num_genes=num_genes)
            ga_instance.run()
            result = get_best_result()
            clear_epoch()
            print("finist repeat: {}, dim: {}, best f: {}".format(i, dim_size, result))
            values[i, j] = result
    log_address = os.path.join(project_dir, 'pygad_exp/log/scale/')
    file_name = os.path.join(log_address, '{}.txt'.format(obj_name))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, values)
    print(values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', default='ackley', help='only support ackley, sphere, rastrigin and schwefel')
    args = parser.parse_args()
    obj_name = args.objective
    minimize(obj_name)
    
    
