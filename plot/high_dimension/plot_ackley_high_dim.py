import numpy as np
import matplotlib.pyplot as plt


cut = 0
a1 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/ZOOpt_exp/log/ackley_20_ave_std.txt')
a1_ave = a1[0][cut:]
a1_std = a1[1][cut:]
# print(len(a1_ave))
a2 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/CMAES_exp/log/ackley_20_ave_std.txt')
a2_ave = a2[0][cut:]
a2_std = a2[1][cut:]
# print(len(a2_ave))
a3 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/DEAP_exp/log/ackley_high_dim_ave_std.txt')
a3_ave = a3[0][cut:]
a3_std = a3[1][cut:]