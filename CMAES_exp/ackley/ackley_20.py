from objective_function.ordinary_function import ackley_log, get_all_epoch, get_epoch_cnt, clear_noisy_global, set_epoch_len
from objective_function.base_function import set_optimal_position
import cma, numpy as np


dim_size = 20


def minimize_ackley():
    init_pos = [np.random.uniform(-1, 1) for _ in range(dim_size)]
    es = cma.CMAEvolutionStrategy(init_pos, 0.3)  # doctest: +ELLIPSIS
    while get_epoch_cnt() < 1:
        solutions = es.ask()
        es.tell(solutions, [ackley_log(x) for x in solutions])
        es.logger.add()
        # es.disp()
    clear_noisy_global()
    sol = es.result_pretty()
    return sol


if __name__ == '__main__':
    set_optimal_position(
        "/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/objective_function/optimal_position/ackley_20.txt")
    repeat = 10
    set_epoch_len(dim_size * 100)
    for i in range(repeat):
        sol = minimize_ackley()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('CMAES_exp/log/ackley_20.txt', all_epoch)
    print(all_epoch.shape)

