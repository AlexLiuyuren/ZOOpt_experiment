#!/usr/bin/env bash

dim_list=(20 50 100 200 400 600 800 1000 10000)
for dim in ${dim_list[*]}
do
python objective_function/get_optimal_position.py rastrigin ${dim} 5
python objective_function/get_optimal_position.py griewank ${dim} 10
python objective_function/get_optimal_position.py schwefel ${dim} 500
done