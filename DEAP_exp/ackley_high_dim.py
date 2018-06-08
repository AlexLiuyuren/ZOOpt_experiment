import operator
import random

import numpy as np
from objective_function.high_dim_function import ackley_high_log, get_all_epoch, set_epoch_len, clear_noisy_global
from objective_function.base_function import set_optimal_position
from deap import base
from deap import benchmarks
from deap import creator
from deap import tools


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Particle", list, fitness=creator.FitnessMin, speed=list,
    smin=None, smax=None, best=None)
dim_size = 20


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


def minimize_ackley_continuous():
    toolbox = base.Toolbox()
    toolbox.register("particle", generate, size=dim_size, pmin=-1, pmax=1, smin=-0.3, smax=0.3)
    toolbox.register("population", tools.initRepeat, list, toolbox.particle)
    toolbox.register("update", updateParticle, phi1=2.0, phi2=2.0)
    toolbox.register("evaluate", lambda x: (ackley_high_log(x), ))
    fmin=[]
    generation = 20
    pop = toolbox.population(n=generation)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    logbook = tools.Logbook()
    logbook.header = ["gen", "evals"] + stats.fields

    GEN = int(10000 / generation)
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

        # Gather all the fitnesses in one list and print the stats
        logbook.record(gen=g, evals=len(pop), **stats.compile(pop))
        fmin.append(min(logbook.select("min")))
    clear_noisy_global()
    return min(fmin)


if __name__ == '__main__':
    set_optimal_position(
        "/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/objective_function/optimal_position/ackley_10000.txt")
    repeat = 10
    set_epoch_len(10000)
    for _ in range(repeat):
        minimize_ackley_continuous()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('DEAP_exp/log/ackley_high_dim.txt', all_epoch)
    print(all_epoch.shape)

