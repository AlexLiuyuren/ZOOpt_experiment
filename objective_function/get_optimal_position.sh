#!/usr/bin/env bash

dim_list=(20 50 100 200 400 600 800 1000 10000)
for dim in ${dim_list[*]}
do
python objective_function/get_optimal_position.py -o ackley -d ${dim}
python objective_function/get_optimal_position.py -o sphere -d ${dim}
python objective_function/get_optimal_position.py -o rastrigin -d ${dim}
python objective_function/get_optimal_position.py -o griewank -d ${dim}
python objective_function/get_optimal_position.py -o schwefel -d ${dim}
done