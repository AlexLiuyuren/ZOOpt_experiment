from zoopt import Dimension, ValueType, Dimension2, Objective, Parameter, Opt, ExpOpt
import numpy as np
def ackley(solution):
    x = solution.get_x()
    bias = 0.2
    value = -20 * np.exp(-0.2 * np.sqrt(sum([(i - bias) * (i - bias) for i in x]) / len(x))) - \
            np.exp(sum([np.cos(2.0*np.pi*(i-bias)) for i in x]) / len(x)) + 20.0 + np.e
    return value

optimal_position = [0.24546860247859748, 0.058532922527610554, 0.19369056457228906, 0.2621536455161537, -0.6098746807670492, -0.33192803959771533, 0.618569031303408, 0.8481808210608066, -0.11857659821287769, 0.3567815443335951, 0.08684676373036582, -0.12932792907821855, 0.5407818541021501, 0.49957605662621596, -0.15377988096034123, -0.8488752305637497, -0.6858534539123635, 0.8029668647971604, -0.7499791560298656, 0.8443788915877086]

def ackley(sol):
    """
        ackley function
    """
    x = sol.get_x()
    x_len = len(x)
    seq = 0
    cos = 0

    for i in range(x_len):
        seq += (x[i] - optimal_position[i]) * (x[i] - optimal_position[i])
        cos += np.cos(2.0 * np.pi * (x[i] - optimal_position[i]))
    ave_seq = seq / x_len
    ave_cos = cos / x_len
    value = -20 * np.exp(-0.2 * np.sqrt(ave_seq)) - np.exp(ave_cos) + 20.0 + np.e
    return value

dim_size = 20  # dimension size
dim = Dimension(dim_size, [[-1, 1]]*dim_size, [True]*dim_size)  
# dim = Dimension2([(ValueType.CONTINUOUS, [-1, 1], 1e-6)]*dim_size)
obj = Objective(ackley, dim)
# perform optimization
solution = Opt.min(obj, Parameter(budget=100*dim_size, intermediate_result=True))
# print the solution
print(solution.get_x(), solution.get_value())
# parallel optimization for time-consuming tasks
# solution = Opt.min(obj, Parameter(budget=100*dim_size, parallel=True, server_num=3))