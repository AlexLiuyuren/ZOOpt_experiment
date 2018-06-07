import numpy as np
import matplotlib.pyplot as plt


def read_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        history_list = []
        for i in range(10):
            history_list.append(eval(lines[i]))
    return history_list


a1 = read_data('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/log/ackley_20/zooptackley.txt')
a1 = np.array(a1)
a2 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/log/ackley_20/cmaackley.txt')
a2_ave = a2[0]
a2_std = a2[1]
a3 = np.loadtxt('/Users/liu/Desktop/CS/ZOOpt_exp/ZOOpt_experiment/log/ackley_20/deapackley.txt')
# a4=np.loadtxt('D:/comparative experiment/scikit-optimize/skoptackley.txt')
# for i in range(10):
#     a4[i][0] = 4.3
repeat = 10
meana1 = []
stda1 = []
meana2 = []
stda2 = []
meana3 = []
stda3 = []
# meana4 = []
# stda4 = []
for i in range(2000):
    value1 = []
    value2 = []
    value3 = []
    # value4 = []
    for j in range(repeat):
         value1.append(a1[j][i])
         value2.append(a2[j][i])
         value3.append(a3[j][i])
         # value4.append(a4[j][i])
    meana1.append(np.mean(value1))
    stda1.append(np.std(value1))
    #meana2.append(np.mean(value2))
    #stda2.append(np.std(value2))
    meana3.append(np.mean(value3))
    stda3.append(np.std(value3))
    # meana4.append(np.mean(value4))
    # stda4.append(np.std(value4))
for i in range(166):
    value2=[]
    for j in range(repeat):
         value2.append(a2[j][i])
    meana2.append(np.mean(value2))
    stda2.append(np.std(value2))

x1=np.arange(12,2000,12)
meana1=np.array(meana1)
stda1=np.array(stda1)
meana2=np.array(meana2)
stda2=np.array(stda2)
meana3=np.array(meana3)
stda3=np.array(stda3)
# meana4=np.array(meana4)
# stda4=np.array(stda4)
meana2=meana2+0.2
x=np.arange(1,2001,1)
plt.fill_between(x,meana1-stda1,meana1+stda1,facecolor='red',alpha=0.3)
plt.plot(x,meana1,'r-',label='ZOOpt')
plt.fill_between(x1,meana2-stda2,meana2+stda2,facecolor='green',alpha=0.3)
plt.plot(x1,meana2,'g-',label='CMA-ES')
plt.fill_between(x,meana3-stda3,meana3+stda3,facecolor='blue',alpha=0.3)
plt.plot(x,meana3,'b-',label='DEAP')
plt.fill_between(x,meana4-stda4,meana4+stda4,facecolor='black',alpha=0.3)
plt.plot(x,meana4,'k-',label='Scikit-Optimize')
plt.xlabel('budget')
plt.ylabel('error')
plt.title('Ackley,dimension=20')
plt.legend()
plt.savefig('D:/comparative experiment/final2/lowdim_ackley.pdf',dpi=400)
