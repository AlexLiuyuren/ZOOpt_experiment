from hyperopt import fmin, tpe, hp
import numpy as np
from objective_function.ordinary_function import ackley_log, clear_noisy_global, get_all_epoch
from objective_function.base_function import set_optimal_position

if __name__ == '__main__':
    set_optimal_position("/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/objective_function/optimal_position/ackley_20.txt")
    repeat = 10
    for _ in range(repeat):
        x = fmin(ackley_log, space=[hp.uniform(str(dim), -1, 1) for dim in range(20)], algo=tpe.suggest, max_evals=2000)
        clear_noisy_global()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('hyperopt_exp/log/ackley_noisy.txt', all_epoch)
    print(all_epoch.shape)

