#!/usr/bin/env bash

python pygad_exp/noisy/run.py -o ackley &
python pygad_exp/noisy/run.py -o sphere &
python pygad_exp/noisy/run.py -o rastrigin &
python pygad_exp/noisy/run.py -o griewank &
python pygad_exp/noisy/run.py -o schwefel &
wait