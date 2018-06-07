import numpy as np
import sys


def get_ave_std(filename, line):
    with open(filename) as f:
        result = []
        lines = f.readlines()
        for i in range(line):
            l = eval(lines[i])
            result.append(eval(lines[i])[:200000])
        result = np.array(result)
        new_matrix = result.T
        ave = []
        std = []
        print(new_matrix.shape)
        for i in range(len(new_matrix)):
            ave.append(np.mean(new_matrix[i]))
            std.append(np.std(new_matrix[i]))
        return np.array(ave), np.array(std)


if __name__ == '__main__':
    argv = sys.argv
    filename = argv[1]
    line = eval(argv[2])
    ave, std = get_ave_std(filename, line)
    log = np.array([list(ave), list(std)])
    print(log.shape)
    np.savetxt(filename[:-4] + "_ave_std.txt", log)


