import numpy as np
import matplotlib.pyplot as plt


def read_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        history_list = []
        for i in range(10):
            history_list.append(eval(lines[i]))
    return history_list


cut = 100
a1 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/ZOOpt_exp/log/ackley_20_ave_std.txt')
a1_ave = a1[0][cut:]
a1_std = a1[1][cut:]
# print(len(a1_ave))
a2 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/CMAES_exp/log/ackley_20_ave_std.txt')
a2_ave = a2[0][cut:]
a2_std = a2[1][cut:]
# print(len(a2_ave))
a3 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/DEAP_exp/log/ackley_20_ave_std.txt')
a3_ave = a3[0][cut:]
a3_std = a3[1][cut:]
a4 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/hyperopt_exp/log/ackley_20_ave_std.txt')
a4_ave = a4[0][cut:]
a4_std = a4[1][cut:]
# a4=np.loadtxt('D:/comparative experiment/scikit-optimize/skoptackley.txt')
# for i in range(10):
#     a4[i][0] = 4.3
repeat = 10
meana1 = []
stda1 = []
meana2 = []
stda2 = []
# a3_ave = []
# a3_std = []
# meana4 = []
# stda4 = []
# for i in range(2000):
#     value3 = []
#     # value4 = []
#     for j in range(repeat):
#          value3.append(a3[j][i])
#          # value4.append(a4[j][i])
#     a3_ave.append(np.mean(value3))
#     a3_std.append(np.std(value3))
#     # meana4.append(np.mean(value4))
#     # stda4.append(np.std(value4))
# print(len(a3_ave))
x=np.arange(1 + cut, 2001, 1)
# a3_ave = np.array(a3_ave)
# a3_std = np.array(a3_std)
# meana4=np.array(meana4)
# stda4=np.array(stda4)
# meana2=meana2+0.2
plt.fill_between(x, a1_ave-a1_std, a1_ave+a1_std, facecolor='red', alpha=0.3)
plt.plot(x, a1_ave,'r-', label='ZOOpt')
plt.fill_between(x, a2_ave-a2_std, a2_ave+a2_std, facecolor='green', alpha=0.3)
plt.plot(x, a2_ave,'g-', label='CMA-ES')
plt.fill_between(x, a3_ave-a3_std, a3_ave+a3_std, facecolor='blue', alpha=0.3)
plt.plot(x, a3_ave, 'b-', label='DEAP')
plt.fill_between(x, a4_ave-a4_std, a4_ave+a4_std, facecolor='orange', alpha=0.3)
plt.plot(x, a4_ave, '-', color='orange', label='Hyperopt')
# plt.fill_between(x, a4_ave-stda4,meana4+stda4,facecolor='black',alpha=0.3)
# plt.plot(x,meana4,'k-',label='Scikit-Optimize')
plt.xlabel('budget')
plt.ylabel('error')
plt.title('Ackley,dimension=20')
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.legend()
plt.savefig('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/plot/img/ackley_20.pdf', dpi=400)
