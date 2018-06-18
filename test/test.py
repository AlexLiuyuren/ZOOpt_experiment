import numpy as np

a = np.array([[1, 2], [3, 4]])
save_name = 'test/test.txt'
np.savetxt(save_name, a)