import numpy as np
from util import mean_var_std

n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])

mean, var, std = mean_var_std(arr)

print(mean)
print(var)
print(std)
