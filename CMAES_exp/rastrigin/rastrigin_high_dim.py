from objective_function.high_dim_function import rastrigin_high_log, get_all_epoch, get_epoch_cnt, clear_noisy_global, set_epoch_len
from objective_function.base_function import set_optimal_position
import cma
import numpy as np

dim_size = 10000
dim_lim = 5


def minimize_rastrigin():
    init_pos = [np.random.uniform(-dim_lim, dim_lim) for _ in range(dim_size)]
    es = cma.CMAEvolutionStrategy(init_pos, 1.6)  # doctest: +ELLIPSIS
    while get_epoch_cnt() < 1:
        solutions = es.ask()
        es.tell(solutions, [rastrigin_high_log(x) for x in solutions])
        es.logger.add()
    clear_noisy_global()
    sol = es.result_pretty()
    return sol


if __name__ == '__main__':
    set_optimal_position(
        "objective_function/optimal_position/rastrigin/rastrigin_10000.txt")
    repeat = 10
    set_epoch_len(10000)
    for i in range(repeat):
        print('repeat', i)
        sol = minimize_rastrigin()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('CMAES_exp/log/rastrigin/rastrigin_10000.txt', all_epoch)
    print(all_epoch.shape)

