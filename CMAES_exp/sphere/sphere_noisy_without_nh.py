from objective_function.noisy_function import sphere_noise_for_cmaes, get_all_epoch, get_epoch_cnt, clear_noisy_global, set_epoch_len
from objective_function.base_function import set_optimal_position
import numpy as np
import cma

dim_size = 100
dim_lim = 1


def minimize_sphere():
    init_pos = [np.random.uniform(-dim_lim, dim_lim) for _ in range(dim_size)]
    es = cma.CMAEvolutionStrategy(init_pos, 0.3)  # doctest: +ELLIPSIS
    while get_epoch_cnt() < 1:
        solutions = es.ask()
        es.tell(solutions, [sphere_noise_for_cmaes(x) for x in solutions])
        es.logger.add()
    clear_noisy_global()
    sol = es.result_pretty()
    return sol


if __name__ == '__main__':
    set_optimal_position(
        "objective_function/optimal_position/sphere_100.txt")
    repeat = 10
    set_epoch_len(200000)
    for i in range(repeat):
        sol = minimize_sphere()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('CMAES_exp/log/sphere/sphere_noisy_without_nh.txt', all_epoch)
    print(all_epoch.shape)

