#!/usr/bin/env bash

dim_list=(20 50 200 400 600 800 1000 10000)
for dim in ${dim_list[*]}
do
python objective_function/get_optimal_position.py sphere ${dim}
python objective_function/get_optimal_position.py ackley ${dim}
done