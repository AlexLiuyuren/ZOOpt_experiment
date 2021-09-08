import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os, argparse

def plot_low_dim(package_list, func_name, inter=5):
    """[summary]

    Parameters
    ----------
    package : str
        [description]
    task_name : [type]
        [description]
    func_name : [type]
        [description]
    """
    project_dir = os.path.dirname(os.path.dirname(__file__))
    dim = {'ackley': 20, 'sphere': 20, 'rastrigin': 20, 'griewank': 20, 'schwefel': 20}
    df_all = pd.DataFrame()
    for package in package_list:
        raw_data_dir = os.path.join(project_dir, package+'_exp', 'log/low_dim')
        raw_data_file = os.path.join(raw_data_dir, '{}_{}.txt'.format(func_name, dim[func_name]))
        data = np.loadtxt(raw_data_file)
        print(package, data.shape)
        for i in range(data.shape[0]): 
            start_point = 100
            dict_tmp = {
                'Function evaluations': np.arange(start_point, data.shape[1], inter),
                'Function value': data[i, start_point:data.shape[1]:inter],
                'Package': [package] * len(np.arange(start_point, data.shape[1], inter))
            }
            df_tmp = pd.DataFrame(dict_tmp)
            df_all = df_all.append(df_tmp)
    sns.set_theme(style="darkgrid")
    ax = sns.lineplot(x="Function evaluations", y="Function value", hue="Package", data=df_all)
    ax.set_title('On convergence rate: {}, dim={}'.format(func_name.capitalize(), dim[func_name]))
    save_dir = os.path.join(project_dir, 'img/low_dim')
    os.makedirs(save_dir, exist_ok=True)
    save_file = os.path.join(save_dir, func_name+'.pdf')
    plt.savefig(save_file)
    plt.cla()

def plot_scale_line(package_list, func_name):
    project_dir = os.path.dirname(os.path.dirname(__file__))
    result = pd.DataFrame(columns=['Dimension size', 'Function value', 'Package'])
    dim = [20, 200, 400, 600, 800, 1000]
    for package in package_list:
        raw_data_dir = os.path.join(project_dir, package+'_exp', 'log', 'scale')
        raw_data_file = os.path.join(raw_data_dir, '{}.txt'.format(func_name))
        data = np.loadtxt(raw_data_file)
        print('package: {}, {}: {}'.format(package, func_name, data.shape))
        data = np.mean(data, axis=0)
        print("Mean data shape: {}".format(data.shape))
        for i in range(data.shape[0]):
            df_tmp = pd.DataFrame([[dim[i], data[i],  package]], columns=['Dimension size', 'Function value', 'Package'])
            result = pd.concat([result, df_tmp], ignore_index=True, axis=0)
            # df_all = df_all.append(df_tmp)
            # df_tmp = pd.DataFrame([[budget[func_name]/10 * (1 + j), data[i, j], package] for j in range(data.shape[1]) if j % 2 == 1] , columns=['Budget', 'Function value', 'Package'])
            # df_all = df_all.append(df_tmp)
        
    print(result.shape)
    sns.set_theme(style="darkgrid")
    ax = sns.lineplot(x="Dimension size", y="Function value", hue="Package", style="Package", data=result, markers=True)
    save_dir = os.path.join(project_dir, 'img/scale')
    os.makedirs(save_dir, exist_ok=True)
    save_file = os.path.join(save_dir, func_name+'.pdf')
    ax.set_title("On scalability: {}".format(func_name.capitalize()))
    if func_name == "rastrigin":
        ax.tick_params(axis='y', labelsize=10)
    ax.figure.savefig(save_file)
    ax.cla()

def plot_noisy_line(package_list, func_name):
    project_dir = os.path.dirname(os.path.dirname(__file__))
    df_all = pd.DataFrame(columns=['Function evaluations', 'Function value', 'Package'])
    budget = {'ackley': 10000, 'sphere': 10000, 'rastrigin': 10000, 'griewank': 40000, 'schwefel': 10000}
    dim = {'ackley': 20, 'sphere': 20, 'rastrigin': 20, 'griewank': 100, 'schwefel': 20}
    sigma = {"sphere": 0.5, "ackley": 0.5, "rastrigin": 20, "griewank": 0.5, "schwefel": 300}
    for package in package_list:
        raw_data_dir = os.path.join(project_dir, package+'_exp', 'log', 'noisy')
        if package == "ZOOpt" or package == "pycma":
            raw_data_file = os.path.join(raw_data_dir, func_name + '_nh_{}.txt'.format(dim[func_name]))
            data = np.loadtxt(raw_data_file)
        elif package == "DEAP" or package == "pygad":
            raw_data_file = os.path.join(raw_data_dir, func_name + '_{}.txt'.format(dim[func_name]))
            data = np.loadtxt(raw_data_file)
        else:
            print("package not supported")
            assert(-1)
        print(data.shape)
        data = np.mean(data, axis=0)
        # print(data.shape)
        for i in range(data.shape[0]):
            df_tmp = pd.DataFrame([[budget[func_name]/10 * (i+1), data[i],  package]], columns=['Function evaluations', 'Function value', 'Package'])
            df_all = df_all.append(df_tmp)
            # df_tmp = pd.DataFrame([[budget[func_name]/10 * (1 + j), data[i, j], package] for j in range(data.shape[1]) if j % 2 == 1] , columns=['Budget', 'Function value', 'Package'])
            # df_all = df_all.append(df_tmp)
            # print(df_all[-10:])
    sns.set_theme(style="darkgrid")
    ax = sns.lineplot(x="Function evaluations", y="Function value", hue="Package", style="Package", data=df_all, markers=True)
    save_dir = os.path.join(project_dir, 'img/noisy')
    os.makedirs(save_dir, exist_ok=True)
    save_file = os.path.join(save_dir, func_name+'.pdf')
    ax.set_title("Optimizing noisy function: {}, dim={}, sigma={}".format(func_name.capitalize(), dim[func_name], sigma[func_name]))
    ax.figure.savefig(save_file)
    ax.cla()

def plot_noisy_bar(package_list, func_name):
    project_dir = os.path.dirname(os.path.dirname(__file__))
    df_all = pd.DataFrame(columns=['Budget', 'Function value', 'Package'])
    budget = {'ackley': 10000, 'sphere': 10000, 'rastrigin': 10000, 'griewank': 40000, 'schwefel': 10000}
    dim = {'ackley': 20, 'sphere': 20, 'rastrigin': 20, 'griewank': 100, 'schwefel': 20}
    for package in package_list:
        raw_data_dir = os.path.join(project_dir, package+'_exp', 'log', 'noisy')
        if package == "ZOOpt":
            raw_data_file = os.path.join(raw_data_dir, func_name + '_nh_{}.txt'.format(dim[func_name]))
            data = np.loadtxt(raw_data_file)
        elif package == "pycma":
            raw_data_file = os.path.join(raw_data_dir, func_name + '_nh_{}.txt'.format(dim[func_name]))
            data = np.loadtxt(raw_data_file)
        elif package == "DEAP":
            raw_data_file = os.path.join(raw_data_dir, func_name + '_{}.txt'.format(dim[func_name]))
            data = np.loadtxt(raw_data_file)
        else:
            print("package not supported")
            assert(-1)
        print(package, data.shape)
        for i in range(data.shape[0]):
            df_tmp_1 = pd.DataFrame([[budget[func_name]/10 * 5, data[i, 4],  package]], columns=['Budget', 'Function value', 'Package'])
            df_tmp_2 = pd.DataFrame([[budget[func_name]/10 * 10, data[i, 9],  package]], columns=['Budget', 'Function value', 'Package'])
            df_all = df_all.append(df_tmp_1)
            df_all = df_all.append(df_tmp_2)
            # df_tmp = pd.DataFrame([[budget[func_name]/10 * (1 + j), data[i, j], package] for j in range(data.shape[1]) if j % 2 == 1] , columns=['Budget', 'Function value', 'Package'])
            # df_all = df_all.append(df_tmp)
            print(df_all[-10:])
    sns.set_theme(style="whitegrid")
    g = sns.catplot(data=df_all, kind="bar", x="Budget", y="Function value", hue="Package", ci=95, palette="dark", alpha=.6, height=6)
    save_dir = os.path.join(project_dir, 'img/noisy')
    os.makedirs(save_dir, exist_ok=True)
    save_file = os.path.join(save_dir, func_name+'.pdf')
    g.savefig(save_file)

def barplot_low_dim(package_list, objective_func_list):
    project_dir = os.path.dirname(os.path.dirname(__file__))
    for func in objective_func_list:
        df_all = pd.DataFrame(columns=['Function value', 'Package'])
        for package in package_list:
            raw_data_dir = os.path.join(project_dir, package+'_exp', 'log/low_dim')
            file_name = os.path.join(raw_data_dir, func + '_20.txt')
            data = np.loadtxt(file_name)
            data = data[:, -1]
            print(data.shape)
            df_tmp = pd.DataFrame([[data[i], package] for i in range(len(data))], columns=['Function value', 'Package'])
            df_all = df_all.append(df_tmp) 
            print(df_all[-10:]) 
            sns.set(rc={"figure.figsize":(6, 8)})
            ax = sns.barplot(x="Package", y="Function value", data=df_all, ci=95)
            ax.set_yscale("log")
            save_dir = os.path.join(project_dir, 'img', 'low_dim', 'bar')
            os.makedirs(save_dir, exist_ok=True)
            save_file = os.path.join(save_dir, '{}.pdf'.format(func))
            plt.savefig(save_file)
            plt.cla()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--task', help='can be "low_dim", "noisy" or "scale"')
    args = parser.parse_args()
    func_list = ['ackley', 'sphere', 'rastrigin', 'schwefel', 'griewank']
    # func_list = ['ackley']
    if args.task == 'low_dim':
        for func in func_list:
            plot_low_dim(['ZOOpt', 'pycma', 'DEAP', 'pygad', 'hyperopt'], func, inter=2)
    if args.task == "noisy":
        for func in func_list:
            plot_noisy_line(['ZOOpt', 'pycma', 'DEAP', 'pygad'], func)
    if args.task == "scale":
        package_list = ['ZOOpt', 'pycma', 'DEAP', 'pygad']
        func_list = ['ackley', 'rastrigin', 'sphere', 'schwefel']
        for func in func_list:
            plot_scale_line(package_list, func)