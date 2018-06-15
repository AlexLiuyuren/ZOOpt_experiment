from objective_function.base_function import set_optimal_position
from objective_function.ordinary_function import sphere_for_cmaes, ackley_for_cmaes, griewank_for_cmaes, \
    rastrigin_for_cmaes, schwefel_for_cmaes, get_epoch_cnt, clear_all, set_epoch_len
import numpy as np
import cma

dim_list = [20, 200, 400, 600, 800, 1000]
func_list = [sphere_for_cmaes, ackley_for_cmaes, griewank_for_cmaes, rastrigin_for_cmaes, schwefel_for_cmaes]
func_name = ['sphere', 'ackley', 'griewank', 'rastrigin', 'schwefel']
search_list = [1, 1, 10, 5, 500]


def get_optimal_txt(func_no, dim_no):
    txt = "objective_function/optimal_position/" + func_name[func_no] + "/" + func_name[func_no] + '_' \
          + str(dim_list[dim_no]) + '.txt'
    return txt


def get_save_txt(func_no):
    txt = 'CMAES_exp/log/' + func_name[func_no] + "/" + func_name[func_no] + '_scale.txt'
    return txt


def exp(func_no, dim_no):
    set_optimal_position(get_optimal_txt(func_no, dim_no))
    set_epoch_len(dim_list[dim_no] * 100)
    init_pos = [np.random.uniform(-search_list[func_no], search_list[func_no]) for _ in range(dim_list[dim_no])]
    es = cma.CMAEvolutionStrategy(init_pos, search_list[func_no] / 3)  # doctest: +ELLIPSIS
    while get_epoch_cnt() < 1:
        solutions = es.ask()
        es.tell(solutions, [func_list[func_no](x) for x in solutions])
        es.logger.add()
    clear_all()
    sol = es.result_pretty().fbest
    return sol


if __name__ == '__main__':
    repeat = 5
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
    # repeat = 1
    # func_result = []
    # func_no_list = [3, 4]
    # for func_no in func_no_list:
    #     for i in range(repeat):
    #         dim_result = []
    #         for j in range(len(dim_list)):
    #             dim_result.append(exp(func_no, j))
    #         print(dim_result)
    #         func_result.append(dim_result)
    #         print(i)
    #     np.savetxt(get_save_txt(func_no), np.array(func_result))

