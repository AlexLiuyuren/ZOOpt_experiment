#!/usr/bin/env bash

python CMAES_exp/schwefel/schwefel_20.py &
python CMAES_exp/schwefel/schwefel_high_dim.py &
python CMAES_exp/schwefel/schwefel_noisy.py &
python CMAES_exp/schwefel/schwefel_noisy_without_nh.py &
