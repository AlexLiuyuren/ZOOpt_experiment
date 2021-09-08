import os, sys, random, argparse, configparser, operator
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_dir)
sys.path.append(project_dir)
from objective_function.low_dim_function import function_dict
from objective_function.base_function import set_optimal_position, append_all_epoch, get_all_epoch, get_cnt, clear_epoch, epoch_first_items
from deap import base, benchmarks, creator, tools
import numpy as np


def generate(size, pmin, pmax, smin, smax):
    part = creator.Particle(random.uniform(pmin, pmax) for _ in range(size))
    part.speed = [random.uniform(smin, smax) for _ in range(size)]
    part.smin = smin
    part.smax = smax
    return part


def updateParticle(part, best, phi1, phi2):
    u1 = (random.uniform(0, phi1) for _ in range(len(part)))
    u2 = (random.uniform(0, phi2) for _ in range(len(part)))
    v_u1 = map(operator.mul, u1, map(operator.sub, part.best, part))
    v_u2 = map(operator.mul, u2, map(operator.sub, best, part))
    part.speed = list(map(operator.add, part.speed, map(operator.add, v_u1, v_u2)))
    for i, speed in enumerate(part.speed):
        if speed < part.smin:
            part.speed[i] = part.smin
        elif speed > part.smax:
            part.speed[i] = part.smax
    part[:] = list(map(operator.add, part, part.speed))



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
    speed_lim = dim_regs[1]/5

    for i in range(repeat):
        for j in range(len(dim_list)):
            dim_size = dim_list[j]
            creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
            creator.create("Particle", list, fitness=creator.FitnessMin, speed=list, smin=None, smax=None, best=None)
            toolbox = base.Toolbox()
            toolbox.register("particle", generate, size=dim_size, pmin=dim_regs[0], pmax=dim_regs[1], smin=-speed_lim, smax=speed_lim)
            toolbox.register("population", tools.initRepeat, list, toolbox.particle)
            toolbox.register("update", updateParticle, phi1=2.0, phi2=2.0)
            toolbox.register("evaluate", lambda x: (function_dict[func_name](x), ))

            optimal_position_address = os.path.join(optimal_position_address_dir, func_name, "{}_{}.txt".format(func_name, dim_size))
            budget = dim_size * 100
            set_optimal_position(optimal_position_address)
            population = 10
            pop = toolbox.population(n=population)

            best = None
            while get_cnt() < budget:
                for part in pop:
                    part.fitness.values = toolbox.evaluate(part)
                    if not part.best or part.best.fitness < part.fitness:
                        part.best = creator.Particle(part)
                        part.best.fitness.values = part.fitness.values
                    if not best or best.fitness < part.fitness:
                        best = creator.Particle(part)
                        best.fitness.values = part.fitness.values
                for part in pop:
                    toolbox.update(part, best)
            values[i, j] = best.fitness.values[0]
            clear_epoch()
            print("finist repeat: {}, dim: {}, best f: {}".format(i, dim_size, best.fitness.values))
    log_address = os.path.join(project_dir, 'DEAP_exp/log/scale/')
    file_name = os.path.join(log_address, '{}.txt'.format(obj_name))
    os.makedirs(log_address, exist_ok=True)
    np.savetxt(file_name, values)
    # print(values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--objective', default='ackley', help='only support ackley, sphere, rastrigin and schwefel')
    args = parser.parse_args()
    obj_name = args.objective
    minimize(obj_name)
    
    
