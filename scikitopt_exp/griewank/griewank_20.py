import numpy as np
from objective_function.ordinary_function import ackley_log, get_all_epoch, set_epoch_len, clear_noisy_global
from objective_function.base_function import set_optimal_position
from skopt import Optimizer


if __name__ == '__main__':
    set_optimal_position(
        "/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/objective_function/optimal_position/ackley_20.txt")
    repeat = 10
    dim_size = 20
    set_epoch_len(dim_size * 100)
    for _ in range(repeat):
        opt = Optimizer([(-1.0, 1.0) for _ in range(dim_size)])
        for i in range(dim_size * 100):
            suggested = opt.ask()
            y = ackley_log(suggested)
            opt.tell(suggested, y)
            # print('iteration:', i, suggested, y)
        clear_noisy_global()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('scikitopt_exp/log/ackley_20.txt', all_epoch)
    print(all_epoch.shape)
