#!/usr/bin/env bash

python DEAP_exp/low_dim/run.py -o ackley &
python DEAP_exp/low_dim/run.py -o sphere &
python DEAP_exp/low_dim/run.py -o rastrigin &
python DEAP_exp/low_dim/run.py -o schwefel &
python DEAP_exp/low_dim/run.py -o griewank &
wait