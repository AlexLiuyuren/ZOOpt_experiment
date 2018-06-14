from objective_function.base_function import sphere, ackley, griewank, rastrigin, schwefel, set_optimal_position
from zoopt.utils.zoo_global import gl
from zoopt import Dimension, Objective, Parameter, Opt
import numpy as np

dim_list = [20, 200, 400, 600, 800, 1000]
func_list = [sphere, ackley, griewank, rastrigin, schwefel]
func_name = ['sphere', 'ackley', 'griewank', 'rastrigin', 'schwefel']
search_list = [1, 1, 10, 5, 500]


def get_optimal_txt(func_no, dim_no):
    txt = "objective_function/optimal_position/" + func_name[func_no] + "/" + func_name[func_no] + '_' \
          + str(dim_list[dim_no]) + '.txt'
    return txt


def get_save_txt(func_no):
    txt = 'ZOOpt_exp/log/' + func_name[func_no] + "/" + func_name[func_no] + '_scale.txt'
    return txt


def exp(func_no, dim_no):
    set_optimal_position(get_optimal_txt(func_no, dim_no))
    dim_size = dim_list[dim_no]
    dim_regs = [[-search_list[func_no], search_list[func_no]]] * dim_size  # dimension range
    dim_tys = [True] * dim_size  # dimension type : real
    dim = Dimension(dim_size, dim_regs, dim_tys)  # form up the dimension object
    objective = Objective(lambda sol: func_list[func_no](sol.get_x()), dim)  # form up the objective function
    budget = dim_size * 100  # 20*dim_size  # number of calls to the objective function
    parameter = Parameter(budget=budget)
    sol = Opt.min(objective, parameter)
    return sol.get_value()


if __name__ == '__main__':
    repeat = 10
    for func_no in range(len(func_list)):
        print(get_save_txt(func_no))
        func_result = []
        for i in range(repeat):
            dim_result = []
            for j in range(len(dim_list)):
                dim_result.append(exp(func_no, j))
            func_result.append(dim_result)
            print(i)
        np.savetxt(get_save_txt(func_no), np.array(func_result))
