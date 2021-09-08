#!/usr/bin/env bash

python ZOOpt_exp/noisy/run.py -o ackley --noise_handling &
python ZOOpt_exp/noisy/run.py -o ackley &
python ZOOpt_exp/noisy/run.py -o sphere --noise_handling &
python ZOOpt_exp/noisy/run.py -o sphere &
python ZOOpt_exp/noisy/run.py -o rastrigin --noise_handling &
python ZOOpt_exp/noisy/run.py -o rastrigin &
python ZOOpt_exp/noisy/run.py -o griewank --noise_handling &
python ZOOpt_exp/noisy/run.py -o griewank &
python ZOOpt_exp/noisy/run.py -o schwefel --noise_handling &
python ZOOpt_exp/noisy/run.py -o schwefel &
wait