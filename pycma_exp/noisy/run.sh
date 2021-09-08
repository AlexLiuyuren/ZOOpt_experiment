#!/usr/bin/env bash

python pycma_exp/noisy/run.py -o ackley &
python pycma_exp/noisy/run.py -o ackley --noise_handling &
python pycma_exp/noisy/run.py -o sphere &
python pycma_exp/noisy/run.py -o sphere --noise_handling &
python pycma_exp/noisy/run.py -o rastrigin &
python pycma_exp/noisy/run.py -o rastrigin --noise_handling &
python pycma_exp/noisy/run.py -o schwefel &
python pycma_exp/noisy/run.py -o schwefel --noise_handling &
python pycma_exp/noisy/run.py -o griewank &
python pycma_exp/noisy/run.py -o griewank --noise_handling &
wait
