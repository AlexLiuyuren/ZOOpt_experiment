import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    with open('ZOOpt_exp/log/sphere_noisy.txt') as f:
        lines = f.readlines()
        best_history = eval(lines[0])
        plt.plot(best_history)
        plt.savefig('plot/img/sphere_noisy.png')

