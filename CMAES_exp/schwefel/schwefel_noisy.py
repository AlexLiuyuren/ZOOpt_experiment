from objective_function.noisy_function import schwefel_noise_for_cmaes, get_all_epoch, get_epoch_cnt, clear_noisy_global, set_epoch_len
from objective_function.base_function import set_optimal_position
import cma
import numpy as np


dim_size = 100
dim_lim = 500


def minimize_schwefel_continuous_noisy():
    init_pos = [np.random.uniform(-dim_lim, dim_lim) for _ in range(dim_size)]
    print(init_pos)
    es = cma.CMAEvolutionStrategy(init_pos, 160)  # doctest: +ELLIPSsIS
    nh = cma.NoiseHandler(es.N, maxevals=[1, 1, 30])
    while get_epoch_cnt() < 1:
         X, fit_vals = es.ask_and_eval(schwefel_noise_for_cmaes, evaluations=nh.evaluations)
         es.tell(X, fit_vals)  # prepare for next iteration
         es.sigma *= nh(X, fit_vals, schwefel_noise_for_cmaes, es.ask)  # see method __call__
         es.countevals += nh.evaluations_just_done  # this is a hack, not important though
         es.logger.add(more_data=[nh.evaluations, nh.noiseS])  # add a data point
    clear_noisy_global()
    sol=es.result[-2]
    return sol


if __name__ == '__main__':
    repeat = 10
    set_optimal_position("objective_function/optimal_position/schwefel/schwefel_100.txt")
    set_epoch_len(200000)
    for i in range(repeat):
        sol = minimize_schwefel_continuous_noisy()
    all_epoch = np.array(get_all_epoch())
    with open('CMAES_exp/log/schwefel/schwefel_noisy.txt', 'w') as f:
        f.truncate()
    np.savetxt('CMAES_exp/log/schwefel/schwefel_noisy.txt', all_epoch)
    print(all_epoch.shape)

