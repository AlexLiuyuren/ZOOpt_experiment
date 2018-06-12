#!/usr/bin/env bash

python CMAES_exp/griewank/griewank_20.py &
python CMAES_exp/griewank/griewank_high_dim.py &
python CMAES_exp/griewank/griewank_noisy.py &
python CMAES_exp/griewank/griewank_noisy_without_nh.py &
