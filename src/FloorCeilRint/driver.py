import numpy as np
from util import floor_ceil_rint

np.set_printoptions(sign=' ')

arr = np.array(list(map(float, input().split())))

f, c, r = floor_ceil_rint(arr)

print(f)
print(c)
print(r)
