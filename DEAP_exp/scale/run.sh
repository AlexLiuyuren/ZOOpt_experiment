#!/usr/bin/env bash

python DEAP_exp/scale/run.py -o ackley &
python DEAP_exp/scale/run.py -o sphere &
python DEAP_exp/scale/run.py -o rastrigin &
python DEAP_exp/scale/run.py -o schwefel &
python DEAP_exp/scale/run.py -o griewank &
wait