import numpy as np
from skopt import Optimizer
# from objective_function.base_function import sphere


def f(x):
    return sum(np.array(x) ** 2)


opt = Optimizer([(-1.0, 1.0), (-1, 1)])

for i in range(200):
    suggested = opt.ask()
    y = f(suggested)
    opt.tell(suggested, y)
    print('iteration:', i, suggested, y)