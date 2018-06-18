#!/usr/bin/env bash
python CMAES_exp/griewank/griewank_high_dim.py &
python CMAES_exp/rastrigin/rastrigin_high_dim.py &
python CMAES_exp/schwefel/schwefel_high_dim.py &
python ZOOpt_exp/schwefel/schwefel_high_dim.py &
python ZOOpt_exp/schwefel/schwefel_high_dim_sre.py &
python DEAP_exp/schwefel/schwefel_high_dim.py &