# ZOOpt_experiment
This repository contains the experiments in 
> **Yu-Ren Liu, Yi-Qi Hu, Hong Qian, Yang Yu, Chao Qian. ZOOpt: Toolbox for Derivative-Free Optimization**. [CORR abs/1801.00329](https://arxiv.org/abs/1801.00329)

ZOOpt is compared with pycma, pygad, DEAP and hyperopt on optimizing four benchmark synthetic functions.We investigate the convergence rate, scalability and the robustness against noise of the tested toolboxes.  

In each toolbox root directory, e.g. ``ZOOpt_exp``, four sub-directories are included, respectively are ``log``, ``low_dim``, ``noisy`` and ``scale``.  ``log`` directory stores all the data that were produced during the optimization.``low_dim`` directory contains the script to perform optimization on low-dimensional functions, of which the dimension size is 20.  ``noisy`` directories contains the experiments on optimizing noisy functions. ``scale`` directory contains the experiments on investigating the scalability of the toolboxes, where the dimension size is set to be 20, 200, 400, 600, 800, 1000 respectively and the final solution values are recorded. 

If you don't want to re-run the experiments, you can directly use the data in ``log`` folder and visualize the results by running ``plot/plot.py``. The result images will be saved in ``img`` directory. To reproduce all the experiments, you can run the scripts that we provided in each subdirectories ``toolboxname_exp/task_name/run.sh``. 

For example, to reproduce the experiments of ZOOpt on optimizing noisy functions. You can type the following command in your terminal.

```
$ bash ZOOpt_exp/noisy/run.sh
```

## Usage
Plot the optimization process using the data we provided:
```
$ conda create -n ZOOpt_exp python==3.6
$ source activate ZOOpt_exp
$ pip install -r requirements.txt
$ python plot/plot.py --task low_dim
$ python plot/plot.py --task scale
$ python plot/plot.py --task noisy
```

To reproduce the experiments on optimizing low-dimensional functions (investigate the convergence rate):

```
$ bash ZOOpt_exp/low_dim/run.sh
$ bash pycma_exp/low_dim/run.sh
$ bash pygad_exp/low_dim/run.sh
$ bash hyperopt_exp/low_dim/run.sh
$ bash DEAP_exp/low_dim/run.sh
$ python plot/plot.py --task low_dim
```

Note that each line will cost a lot of time, the plot function works normally only when the data are complete, i.e. all tasks are finished. 

To reproduce the experiments on investigating the scalability of the toolbox:
```
$ bash ZOOpt_exp/scale/run.sh
$ bash pycma_exp/scale/run.sh
$ bash pygad_exp/scale/run.sh
$ bash DEAP_exp/scale/run.sh
$ python plot/plot.py --task scale
```

To reproduce the experiments on optimizing noisy functions:
```
$ bash ZOOpt_exp/noisy/run.sh
$ bash pycma_exp/noisy/run.sh
$ bash pygad_exp/noisy/run.sh
$ bash DEAP_exp/noisy/run.sh
$ python plot/plot.py --task noisy
```
