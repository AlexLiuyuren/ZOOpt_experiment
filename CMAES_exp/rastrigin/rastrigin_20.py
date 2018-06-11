from objective_function.ordinary_function import rastrigin_log, get_all_epoch, get_epoch_cnt, clear_noisy_global, set_epoch_len
from objective_function.base_function import set_optimal_position
import cma, numpy as np


dim_size = 20
dim_lim = 5


def minimize_rastrigin():
    init_pos = [np.random.uniform(-dim_lim, dim_lim) for _ in range(dim_size)]
    es = cma.CMAEvolutionStrategy(init_pos, 0.3)  # doctest: +ELLIPSIS
    while get_epoch_cnt() < 1:
        solutions = es.ask()
        es.tell(solutions, [rastrigin_log(x) for x in solutions])
        es.logger.add()
        # es.disp()
    clear_noisy_global()
    sol = es.result_pretty()
    # nh = cma.NoiseHandler(es.N, maxevals=[1, 1, 30])
    # while get_epoch_cnt() < 1:
    #      X, fit_vals = es.ask_and_eval(rastrigin_log, evaluations=nh.evaluations)
    #      es.tell(X, fit_vals)  # prepare for next iteration
    #      es.sigma *= nh(X, fit_vals, rastrigin_noise_log, es.ask)  # see method __call__
    #      es.countevals += nh.evaluations_just_done  # this is a hack, not important though
    #      es.logger.add(more_data=[nh.evaluations, nh.noiseS])  # add a data point
    # clear_noisy_global()
    # sol=es.result[-2]
    return sol


if __name__ == '__main__':
    set_optimal_position(
        "objective_function/optimal_position/rastrigin/rastrigin_20.txt")
    repeat = 1
    set_epoch_len(10000)
    for i in range(repeat):
        sol = minimize_rastrigin()
    all_epoch = np.array(get_all_epoch())
    np.savetxt('CMAES_exp/log/rastrigin_20.txt', all_epoch)
    print(all_epoch.shape)

