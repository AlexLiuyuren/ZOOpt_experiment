import configparser, argparse, pygad, os, sys
import numpy as np
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.low_dim_function import function_dict
from objective_function.base_function import clear_all_epoch, clear_epoch, set_optimal_position, append_all_epoch, get_all_epoch, epoch_first_items


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

    sol_per_pop = 20 # Number of solutions in the population.
    num_generations = budget // sol_per_pop # Number of generations.
    num_parents_mating = 5
    
    num_genes = dim_size
    for i in range(repeat):
        gene_space = [{'low': dim_regs[0], 'high': dim_regs[1]}] * dim_size
        def fitness_func(solution, solution_idx):
            # Calculating the fitness value of each solution in the current population.
            output = -function_dict[obj_name](solution)
            return output
        fitness_function = fitness_func
        ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop, 
                       gene_space= gene_space,
                       num_genes=num_genes)
        # Running the GA to optimize the parameters of the function.    
        ga_instance.run()
        epoch_first_items(budget)
        append_all_epoch()

    all_epoch = np.array(get_all_epoch())
    print(all_epoch[:, 0])
    log_address = os.path.join(project_dir, 'pygad_exp/log/low_dim/')
    file_name = os.path.join(log_address, '{}_{}.txt'.format(obj_name, dim_size))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, all_epoch)
    print(all_epoch.shape)
    
    
