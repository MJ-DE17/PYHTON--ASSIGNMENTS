import numpy as np
from util import determinant

n = int(input())
matrix = np.array([list(map(float, input().split())) for _ in range(n)])

print(determinant(matrix))
