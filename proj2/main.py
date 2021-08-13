import math
import matplotlib.pyplot as matplotlib
import numpy as np

arr = np.load("btc_price.npy")
n = len(arr)
for lambda1 in [0, 10, 500, 10000]:
    i_matrix = np.full((n, n), 0, dtype='f')
    d_matrix = np.full((n - 1, n), 0, dtype='f')
    for i in range(n):
        i_matrix[i][i] = 1
    for i in range(n - 1):
        d_matrix[i][i] = math.sqrt(lambda1)
        d_matrix[i][i + 1] = -d_matrix[i][i]
    joined = np.vstack((i_matrix, d_matrix))
    transposed = np.transpose(joined)
    product = np.dot(transposed, joined)
    result = np.linalg.solve(product, arr)# (product^T) * product * x = arr
    matplotlib.plot(result)
    matplotlib.show()