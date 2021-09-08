from objective_function.base_function import sphere, ackley, rastrigin, griewank, schwefel, function_log, func_for_cmaes
import numpy as np
import gc

def low_dim_sphere_log(x): return function_log(sphere, x)
def low_dim_ackley_log(x): return function_log(ackley, x)
def low_dim_rastrigin_log(x): return function_log(rastrigin, x)
def low_dim_griewank_log(x): return function_log(griewank, x)
def low_dim_schwefel_log(x): return function_log(schwefel, x)

function_dict = {
    'ackley': low_dim_ackley_log,
    'sphere': low_dim_sphere_log,
    'rastrigin': low_dim_rastrigin_log,
    'griewank': low_dim_griewank_log,
    'schwefel': low_dim_schwefel_log    
}

def low_dim_sphere_for_cmaes(x): return func_for_cmaes(low_dim_sphere_log, 1, x)
def low_dim_ackley_for_cmaes(x): return func_for_cmaes(low_dim_ackley_log, 1, x)
def low_dim_griewank_for_cmaes(x): return func_for_cmaes(low_dim_griewank_log, 10, x)
def low_dim_rastrigin_for_cmaes(x): return func_for_cmaes(low_dim_rastrigin_log, 5, x)
def low_dim_schwefel_for_cmaes(x): return func_for_cmaes(low_dim_schwefel_log, 500, x)

function_cmaes_dict = {
    'sphere': low_dim_sphere_for_cmaes,
    'ackley': low_dim_ackley_for_cmaes,
    'griewank': low_dim_griewank_for_cmaes,
    'rastrigin': low_dim_rastrigin_for_cmaes,
    'schwefel': low_dim_schwefel_for_cmaes
}
