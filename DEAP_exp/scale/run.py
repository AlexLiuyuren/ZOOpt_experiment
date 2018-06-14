from objective_function.base_function import set_optimal_position, sphere, ackley, griewank, rastrigin, schwefel
import numpy as np
from deap import base
from deap import benchmarks
from deap import creator
from deap import tools
import random
import operator


dim_list = [20, 200, 400, 600, 800, 1000]
func_list = [sphere, ackley, griewank, rastrigin, schwefel]
func_name = ['sphere', 'ackley', 'griewank', 'rastrigin', 'schwefel']
search_list = [1, 1, 10, 5, 500]
speed_list = [0.2, 0.2, 2, 1, 100]

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Particle", list, fitness=creator.FitnessMin, speed=list,
    smin=None, smax=None, best=None)


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


def get_optimal_txt(func_no, dim_no):
    txt = "objective_function/optimal_position/" + func_name[func_no] + "/" + func_name[func_no] + '_' \
          + str(dim_list[dim_no]) + '.txt'
    return txt


def get_save_txt(func_no):
    txt = 'DEAP_exp/log/' + func_name[func_no] + "/" + func_name[func_no] + '_scale.txt'
    return txt


def exp(func_no, dim_no):
    set_optimal_position(get_optimal_txt(func_no, dim_no))
    init_pos = [np.random.uniform(-search_list[func_no], search_list[func_no]) for _ in range(dim_list[dim_no])]
    toolbox = base.Toolbox()
    toolbox.register("particle", generate, size=dim_list[dim_no], pmin=-search_list[func_no], pmax=search_list[func_no],
                     smin=-speed_list[func_no], smax=speed_list[func_no])
    toolbox.register("population", tools.initRepeat, list, toolbox.particle)
    toolbox.register("update", updateParticle, phi1=1.0, phi2=1.0)
    toolbox.register("evaluate", lambda x: (func_list[func_no](x),))
    fmin = []
    population = 20
    pop = toolbox.population(n=population)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    logbook = tools.Logbook()
    logbook.header = ["gen", "evals"] + stats.fields

    budget = dim_list[dim_no] * 100
    GEN = int(budget / population)
    best = None
    i = 0
    for g in range(GEN):
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
        logbook.record(gen=g, evals=len(pop), **stats.compile(pop))
        fmin.append(min(logbook.select("min")))
    return min(fmin)


if __name__ == '__main__':
    repeat = 10
    for func_no in range(len(func_list)):
        # print(get_save_txt(func_no))
        func_result = []
        for i in range(repeat):
            dim_result = []
            for j in range(len(dim_list)):
                value = exp(func_no, j)
                print(value)
                dim_result.append(value)
            func_result.append(dim_result)
        np.savetxt(get_save_txt(func_no), np.array(func_result))
