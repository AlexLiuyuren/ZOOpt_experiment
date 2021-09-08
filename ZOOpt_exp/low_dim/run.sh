#!/usr/bin/env bash

python ZOOpt_exp/low_dim/run.py -o ackley &
python ZOOpt_exp/low_dim/run.py -o sphere &
python ZOOpt_exp/low_dim/run.py -o rastrigin &
python ZOOpt_exp/low_dim/run.py -o schwefel &
python ZOOpt_exp/low_dim/run.py -o griewank &
wait