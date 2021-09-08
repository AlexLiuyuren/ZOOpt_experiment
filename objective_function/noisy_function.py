import numpy as np
from objective_function.base_function import sphere, ackley, rastrigin, griewank, schwefel, set_optimal_position, func_for_cmaes, function_log, best_result, epoch

def func_noise_creator(func, mu, sigma):
    return lambda x: func(x) + np.random.normal(mu, sigma)

sphere_noisy = func_noise_creator(sphere, 0, 0.5)
ackley_noisy = func_noise_creator(ackley, 0, 0.5)
rastrigin_noisy = func_noise_creator(rastrigin, 0, 20)
griewank_noisy = func_noise_creator(griewank, 0, 0.5)
schwefel_noisy = func_noise_creator(schwefel, 0, 300)

# def func_noise_log(func_noisy, func, x):
#     result = func_noisy(x)
#     true_result = func(x)
#     global epoch, best_result
#     if result < best_result:
#         epoch.append(true_result)
#         best_result = result
#     else:
#         epoch.append(epoch[-1])
#     return result


def sphere_noise_log(x): return function_log(sphere_noisy, x)
def ackley_noise_log(x): return function_log(ackley_noisy, x)
def rastrigin_noise_log(x): return function_log(rastrigin_noisy, x)
def griewank_noise_log(x): return function_log(griewank_noisy, x)
def schwefel_noise_log(x): return function_log(schwefel_noisy, x)

noisy_function_dict = {
    'ackley': ackley_noise_log,
    'sphere': sphere_noise_log,
    'rastrigin': rastrigin_noise_log,
    'griewank': griewank_noise_log,
    'schwefel': schwefel_noise_log    
}

def sphere_noise_for_cmaes(x): return func_for_cmaes(sphere_noise_log, 1, x)
def ackley_noise_for_cmaes(x): return func_for_cmaes(ackley_noise_log, 1, x)
def griewank_noise_for_cmaes(x): return func_for_cmaes(griewank_noise_log, 10, x)
def rastrigin_noise_for_cmaes(x): return func_for_cmaes(rastrigin_noise_log, 5, x)
def schwefel_noise_for_cmaes(x): return func_for_cmaes(schwefel_noise_log, 500, x)

noisy_function_cmaes_dict = {
    'sphere': sphere_noise_for_cmaes,
    'ackley': ackley_noise_for_cmaes,
    'griewank': griewank_noise_for_cmaes,
    'rastrigin': rastrigin_noise_for_cmaes,
    'schwefel': schwefel_noise_for_cmaes
}