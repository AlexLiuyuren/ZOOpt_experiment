#!/usr/bin/env bash

python DEAP_exp/griewank/griewank_20.py &
python DEAP_exp/griewank/griewank_high_dim.py &
python DEAP_exp/griewank/griewank_noisy.py &
