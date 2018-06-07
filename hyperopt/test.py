from hyperopt import fmin, tpe, hp
import numpy as np


def sphere(x):
    return sum(np.array(x) ** 2)


x = fmin(sphere, space=[hp.uniform(str(dim), -1, 1) for dim in range(100)], algo=tpe.suggest, max_evals=200)
print(x)
