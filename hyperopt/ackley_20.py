from hyperopt import fmin, tpe, hp
import numpy as np
from objective_function.ordinary_function import ackley_log


x = fmin(ackley_log, space=[hp.uniform(str(dim), -1, 1) for dim in range(100)], algo=tpe.suggest, max_evals=200)
print(x)
