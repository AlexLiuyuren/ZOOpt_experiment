import numpy as np
import matplotlib.pyplot as plt


def plot_low_dim(cut, func_name, dim_name):
    txt_name = func_name + '_' + dim_name + '.txt'
    dim = int(eval(dim_name))
    budget = dim * 100
    zoopt = np.loadtxt('ZOOpt_exp/log/' + func_name + '/ave_std/' + txt_name)
    zoopt_ave = zoopt[0][cut:budget]
    zoopt_std = zoopt[1][cut:budget]
    cmaes = np.loadtxt('CMAES_exp/log/' + func_name + '/ave_std/' + txt_name)
    cmaes_ave = cmaes[0][cut:budget]
    cmaes_std = cmaes[1][cut:budget]
    deap = np.loadtxt('DEAP_exp/log/' + func_name + '/ave_std/' + txt_name)
    deap_ave = deap[0][cut:budget]
    deap_std = deap[1][cut:budget]
    hyperopt = np.loadtxt('hyperopt_exp/log/' + func_name + '/ave_std/' + txt_name)
    hyperopt_ave = hyperopt[0][cut:budget]
    hyperopt_std = hyperopt[1][cut:budget]
    x = np.arange(1 + cut, 1 + budget, 1)
    print(len(x))
    print(len(zoopt_ave))
    plt.fill_between(x, zoopt_ave - zoopt_std, zoopt_ave + zoopt_std, facecolor='red', alpha=0.3)
    plt.plot(x, zoopt_ave, 'r-', label='ZOOpt')
    plt.fill_between(x, cmaes_ave - cmaes_std, cmaes_ave + cmaes_std, facecolor='green', alpha=0.3)
    plt.plot(x, cmaes_ave, 'g-', label='CMA-ES')
    plt.fill_between(x, deap_ave - deap_std, deap_ave + deap_std, facecolor='blue', alpha=0.3)
    plt.plot(x, deap_ave, 'b-', label='DEAP')
    plt.fill_between(x, hyperopt_ave - hyperopt_std, hyperopt_ave + hyperopt_std, facecolor='orange', alpha=0.3)
    plt.plot(x, hyperopt_ave, '-', color='orange', label='Hyperopt')
    plt.xlabel('budget')
    plt.ylabel('error')
    upper_fn = func_name[0].upper() + func_name[1:]
    plt.title(upper_fn + ', dimension=' + dim_name)
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.legend()
    save_txt1 = func_name + '_' + dim_name + '.pdf'
    save_txt2 = func_name + '_' + dim_name + '.png'
    plt.savefig('plot/img/' + func_name + '/' + save_txt1, dpi=400)
    plt.savefig('plot/img/' + func_name + '/' + save_txt2, dpi=400)
    plt.close()


def plot_noisy(cut, func_name, budget, sigma):
    txt_name = func_name + '_' + 'noisy.txt'
    txt_without_nh_name = func_name + '_' + 'noisy_without_nh.txt'
    zoopt = np.loadtxt('ZOOpt_exp/log/' + func_name + '/ave_std/' + txt_name)
    zoopt_ave = zoopt[0][cut:budget]
    zoopt_std = zoopt[1][cut:budget]
    zoopt_without_nh = np.loadtxt('ZOOpt_exp/log/' + func_name + '/ave_std/' + txt_without_nh_name)
    zoopt_without_nh_ave = zoopt_without_nh[0][cut:budget]
    zoopt_without_nh_std = zoopt_without_nh[1][cut:budget]

    cmaes = np.loadtxt('CMAES_exp/log/' + func_name + '/ave_std/' + txt_name)
    cmaes_ave = cmaes[0][cut:budget]
    cmaes_std = cmaes[1][cut:budget]
    cmaes_without_nh = np.loadtxt('CMAES_exp/log/' + func_name + '/ave_std/' + txt_without_nh_name)
    cmaes_without_nh_ave = cmaes_without_nh[0][cut:budget]
    cmaes_without_nh_std = cmaes_without_nh[1][cut:budget]

    deap = np.loadtxt('DEAP_exp/log/' + func_name + '/ave_std/' + txt_name)
    deap_ave = deap[0][cut:budget]
    deap_std = deap[1][cut:budget]

    x = np.arange(1 + cut, 1 + budget, 1)
    # print(len(x))
    # print(len(zoopt_ave))
    plt.fill_between(x, zoopt_ave - zoopt_std, zoopt_ave + zoopt_std, facecolor='c', alpha=0.3)
    plt.plot(x, zoopt_ave, 'c-', label='ZOOpt-nh')
    plt.fill_between(x, zoopt_without_nh_ave - zoopt_without_nh_std, zoopt_without_nh_ave + zoopt_without_nh_std,
                     facecolor='red', alpha=0.3)
    plt.plot(x, zoopt_without_nh_ave, 'r-', label='ZOOpt')

    plt.fill_between(x, cmaes_ave - cmaes_std, cmaes_ave + cmaes_std, facecolor='tan', alpha=0.3)
    plt.plot(x, cmaes_ave, '-', color='tan', label='CMA-ES-nh')

    plt.fill_between(x, cmaes_without_nh_ave - cmaes_without_nh_std, cmaes_without_nh_ave + cmaes_without_nh_std,
                     facecolor='green', alpha=0.3)
    plt.plot(x, cmaes_without_nh_ave, 'g-', label='CMA-ES')

    plt.fill_between(x, deap_ave - deap_std, deap_ave + deap_std, facecolor='blue', alpha=0.3)
    plt.plot(x, deap_ave, 'b-', label='DEAP')
    plt.xlabel('budget')
    plt.ylabel('error')
    upper_fn = func_name[0].upper() + func_name[1:]
    plt.title(upper_fn + ', dim=100, sigma=' + str(sigma))
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.legend()
    save_txt1 = func_name + '_noisy.pdf'
    save_txt2 = func_name + '_noisy.png'
    plt.savefig('plot/img/' + func_name + '/' + save_txt1, dpi=400)
    plt.savefig('plot/img/' + func_name + '/' + save_txt2, dpi=400)
    plt.close()


def plot_scale(func_name):
    dim = [20, 200, 400, 600, 800, 1000]
    txt_name = func_name + '_scale.txt'
    zoopt = np.loadtxt('ZOOpt_exp/log/' + func_name + '/ave_std/' + txt_name)
    zoopt_ave = zoopt[0]
    zoopt_std = zoopt[1]
    cmaes = np.loadtxt('CMAES_exp/log/' + func_name + '/ave_std/' + txt_name)
    cmaes_ave = cmaes[0]
    cmaes_std = cmaes[1]
    deap = np.loadtxt('DEAP_exp/log/' + func_name + '/ave_std/' + txt_name)
    deap_ave = deap[0]
    deap_std = deap[1]

    plt.errorbar(dim, zoopt_ave, yerr=zoopt_std, label='ZOOpt', color='red', fmt='-')
    plt.errorbar(dim, cmaes_ave, yerr=cmaes_std, label='CMA-ES', color='green', fmt='-')
    plt.errorbar(dim, deap_ave, yerr=deap_std, label='DEAP', color='blue', fmt='-')
    plt.xlabel('dimension_size')
    plt.ylabel('error')
    upper_fn = func_name[0].upper() + func_name[1:]
    plt.title(upper_fn)
    plt.legend()
    save_txt1 = func_name + '_scale.pdf'
    save_txt2 = func_name + '_scale.png'
    plt.savefig('plot/img/' + func_name + '/' + save_txt1, dpi=400)
    plt.savefig('plot/img/' + func_name + '/' + save_txt2, dpi=400)
    plt.close()


def plot_high_dim(cut, func_name):
    txt_name = func_name + '_10000.txt'
    zoopt_sre_name = func_name + '_10000_sre.txt'
    zoopt = np.loadtxt('ZOOpt_exp/log/' + func_name + '/ave_std/' + txt_name)
    zoopt_ave = zoopt[0][cut:]
    zoopt_std = zoopt[1][cut:]
    zoopt_sre = np.loadtxt('ZOOpt_exp/log/' + func_name + '/ave_std/' + zoopt_sre_name)
    zoopt_sre_ave = zoopt_sre[0][cut:]
    zoopt_sre_std = zoopt_sre[1][cut:]
    cmaes = np.loadtxt('CMAES_exp/log/' + func_name + '/ave_std/' + txt_name)
    cmaes_ave = cmaes[0][cut:]
    cmaes_std = cmaes[1][cut:]
    deap = np.loadtxt('DEAP_exp/log/' + func_name + '/ave_std/' + txt_name)
    deap_ave = deap[0][cut:]
    deap_std = deap[1][cut:]
    x = np.arange(1 + cut, 10001, 1)
    plt.fill_between(x, zoopt_ave - zoopt_std, zoopt_ave + zoopt_std, facecolor='red', alpha=0.3)
    plt.plot(x, zoopt_ave, 'r-', label='ZOOpt')
    plt.fill_between(x, zoopt_sre_ave - zoopt_sre_std, zoopt_sre_ave + zoopt_sre_std, facecolor='rosybrown', alpha=0.3)
    plt.plot(x, zoopt_sre_ave, '-', color='rosybrown', label='ZOOpt-sre')
    plt.fill_between(x, cmaes_ave - cmaes_std, cmaes_ave + cmaes_std, facecolor='green', alpha=0.3)
    plt.plot(x, cmaes_ave, 'g-', label='CMA-ES')
    plt.fill_between(x, deap_ave - deap_std, deap_ave + deap_std, facecolor='blue', alpha=0.1)
    plt.plot(x, deap_ave, 'b-', label='DEAP')
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.xlabel('budget')
    plt.ylabel('error')
    upper_fn = func_name[0].upper() + func_name[1:]
    plt.title(upper_fn)
    plt.legend()
    save_txt1 = func_name + '_10000.pdf'
    save_txt2 = func_name + '_10000.png'
    plt.savefig('plot/img/' + func_name + '/' + save_txt1, dpi=400)
    plt.savefig('plot/img/' + func_name + '/' + save_txt2, dpi=400)
    plt.close()


if __name__ == '__main__':
    plot_low_dim(100, 'ackley', '20')
    plot_low_dim(100, 'sphere', '20')
    plot_low_dim(100, 'griewank', '20')
    plot_low_dim(100, 'rastrigin', '20')
    plot_low_dim(100, 'schwefel', '20')

    plot_noisy(25000, 'ackley', 200000, 0.1)
    plot_noisy(25000, 'sphere', 200000, 1)
    plot_noisy(25000, 'griewank', 200000, 1)
    plot_noisy(25000, 'rastrigin', 200000, 1)
    plot_noisy(25000, 'schwefel', 200000, 1)

    plot_scale('ackley')
    plot_scale('sphere')
    plot_scale('griewank')
    plot_scale('rastrigin')
    plot_scale('schwefel')

    # plot_high_dim(0, 'ackley')
    # plot_high_dim(0, 'sphere')
    # plot_high_dim(0, 'griewank')
    # plot_high_dim(0, 'rastrigin')
    # plot_high_dim(0, 'schwefel')
