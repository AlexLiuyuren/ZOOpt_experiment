#!/usr/bin/env bash

python DEAP_exp/noisy/run.py -o ackley &
python DEAP_exp/noisy/run.py -o sphere &
python DEAP_exp/noisy/run.py -o rastrigin &
python DEAP_exp/noisy/run.py -o schwefel &
python DEAP_exp/noisy/run.py -o griewank &
wait