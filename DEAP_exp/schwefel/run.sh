#!/usr/bin/env bash

python DEAP_exp/schwefel/schwefel_20.py &
python DEAP_exp/schwefel/schwefel_high_dim.py &
python DEAP_exp/schwefel/schwefel_noisy.py &
