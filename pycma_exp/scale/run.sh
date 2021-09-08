#!/usr/bin/env bash

python pycma_exp/scale/run.py -o ackley &
python pycma_exp/scale/run.py -o sphere &
python pycma_exp/scale/run.py -o rastrigin &
python pycma_exp/scale/run.py -o schwefel &
python pycma_exp/scale/run.py -o griewank &
wait