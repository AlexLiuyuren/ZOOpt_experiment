#!/usr/bin/env bash
rm *.dat
rm CMAES_exp/log/*/*.txt
rm CMAES_exp/log/*/ave_std/*.txt
# rm CMAES_exp/log/sphere/*.txt
# rm CMAES_exp/log/rastrigin/*.txt
# rm CMAES_exp/log/griewank/*.txt
# rm CMAES_exp/log/schwefel/*.txt

rm DEAP_exp/log/*/*.txt
rm DEAP_exp/log/*/ave_std/*.txt
# rm DEAP_exp/log/sphere/*.txt
# rm DEAP_exp/log/rastrigin/*.txt
# rm DEAP_exp/log/griewank/*.txt
# rm DEAP_exp/log/schwefel/*.txt

rm hyperopt_exp/log/*/*.txt
rm hyperopt_exp/log/*/ave_std/*.txt

rm ZOOpt_exp/log/*/*.txt
rm ZOOpt_exp/log/*/ave_std/*.txt
