#!/usr/bin/env bash

python pycma_exp/low_dim/run.py -o ackley &
python pycma_exp/low_dim/run.py -o sphere &
python pycma_exp/low_dim/run.py -o rastrigin &
python pycma_exp/low_dim/run.py -o schwefel &
python pycma_exp/low_dim/run.py -o griewank &
wait