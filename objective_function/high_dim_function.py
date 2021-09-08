import numpy as np
import os, sys
project_dir = os.path.dirname(os.path.dirname(__file__))
print(project_dir)
sys.path.append(project_dir)
from objective_function.base_function import sphere, ackley, griewank, rastrigin, schwefel, function_log, get_optimal_position, func_for_cmaes

def function_high(func, x):
    """
        Variant of the func function. Dimensions except the first 10 ones have limited 
        impact on the function value.
    """
    x1 = x[:10]
    x2 = x[10:]
    value1 = func(x1)
    value2 = 0
    optimal_position = get_optimal_position()
    for i in range(len(x2)):
        value2 += (x2[i] - optimal_position[i + 10]) * (x2[i] - optimal_position[i + 10])
    value2 /= len(x)
    return value1 + value2


def sphere_high(x): return function_high(sphere, x)
def ackley_high(x): return function_high(ackley, x)
def rastrigin_high(x): return function_high(rastrigin, x)
def griewank_high(x): return function_high(griewank, x)

def schwefel_high(x):
    x1 = x[:10]
    x2 = x[10:]
    value1 = schwefel(x1)
    if value1 < 0:
        print(x1)
        value2 = 0
        for i in range(len(x2)):
            value2 += (x2[i] - 420.9687) * (x2[i] - 420.9687)
        print(value2)
    assert(value1 >= 0)
    value2 = 0
    for i in range(len(x2)):
        value2 += (x2[i] - 420.9687) * (x2[i] - 420.9687)
    assert(value2 > 0)
    value2 /= (len(x) * len(x))
    return value1 + value2

def high_dim_sphere_log(x): return function_log(sphere_high, x)
def high_dim_ackley_log(x): return function_log(ackley_high, x)
def high_dim_rastrigin_log(x): return function_log(rastrigin_high, x)
def high_dim_griewank_log(x): return function_log(griewank_high, x)
def high_dim_schwefel_log(x): return function_log(schwefel_high, x)

high_dim_function_dict = {
    'ackley': high_dim_ackley_log,
    'sphere': high_dim_sphere_log,
    'rastrigin': high_dim_rastrigin_log,
    'griewank': high_dim_griewank_log,
    'schwefel': high_dim_schwefel_log   
}

def high_dim_sphere_for_cmaes(x): return func_for_cmaes(high_dim_sphere_log, 1, x)
def high_dim_ackley_for_cmaes(x): return func_for_cmaes(high_dim_ackley_log, 1, x)
def high_dim_rastrigin_for_cmaes(x): return func_for_cmaes(high_dim_rastrigin_log, 5, x)
def high_dim_griewank_for_cmaes(x): return func_for_cmaes(high_dim_griewank_log, 10, x)
def high_dim_schwefel_for_cmaes(x): return func_for_cmaes(high_dim_schwefel_log, 500, x)

high_dim_function_cmaes_dict = {
    'sphere': high_dim_sphere_for_cmaes,
    'ackley': high_dim_ackley_for_cmaes,
    'griewank': high_dim_griewank_for_cmaes,
    'rastrigin': high_dim_rastrigin_for_cmaes,
    'schwefel': high_dim_schwefel_for_cmaes
}

if __name__ == '__main__':
    x =  [-0.8533454208895921, 484.1863579927998, -468.2074832322618, -466.0903303154482, 395.0905281703499, -336.8235319970066, -323.49042323914193, 32.316025340673036, 62.87115862180781, -453.5690082532268, -280.9948421336559]
    print(high_dim_function_dict['schwefel'](x))