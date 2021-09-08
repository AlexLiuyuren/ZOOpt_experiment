#!/usr/bin/env bash

python hyperopt_exp/low_dim/run.py -o ackley &
python hyperopt_exp/low_dim/run.py -o sphere &
python hyperopt_exp/low_dim/run.py -o rastrigin &
python hyperopt_exp/low_dim/run.py -o schwefel &
python hyperopt_exp/low_dim/run.py -o griewank &
wait