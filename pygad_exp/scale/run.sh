#!/usr/bin/env bash

python pygad_exp/scale/run.py -o ackley &
python pygad_exp/scale/run.py -o sphere &
python pygad_exp/scale/run.py -o rastrigin &
python pygad_exp/scale/run.py -o schwefel &
python pygad_exp/scale/run.py -o griewank &
wait