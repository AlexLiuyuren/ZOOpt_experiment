#!/usr/bin/env bash

python ZOOpt_exp/scale/run.py -o ackley &
python ZOOpt_exp/scale/run.py -o sphere &
python ZOOpt_exp/scale/run.py -o rastrigin &
python ZOOpt_exp/scale/run.py -o schwefel &
python ZOOpt_exp/scale/run.py -o griewank &
wait