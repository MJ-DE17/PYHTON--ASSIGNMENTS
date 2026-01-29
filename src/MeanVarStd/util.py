import numpy as np

def mean_var_std(arr):
    mean = np.mean(arr, axis=1)
    var = np.var(arr, axis=0)
    std = np.std(arr)
    return mean, var, std
