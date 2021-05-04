# In The Name Of GOD

import numpy as np


def get_l_u_form(first, second):  # e = l, f = u
    for k in range(len(first)):
        second[k][k] = 1.0
        for h in range(k + 1, len(first)):
            s = float((first[h][k]) / first[k][k])
            second[h][k] = s
            first[h] -= s * first[k]


def get_lyb(li, bi):
    y = np.c_[li, bi]
    for k in range(len(y)):
        for i in range(k + 1, len(y)):
            s = float(y[i][k] / y[k][k])
            y[i] -= s * y[k]
    return y[:, -1]


def get_uxy(ui, yi):
    y = np.c_[ui, yi]
    for k in range(len(y)):
        y[k] /= y[k][k]
        for i in range(k):
            s = float(y[i][k] / y[k][k])
            y[i] -= s * y[k]
    return y[:, -1]


def solve_augmented(matrix2, vector):
    y = np.c_[matrix2, vector]
    for k in range(len(y)):
        y[k] /= y[k][k]
        for i in range(len(y)):
            if i != k:
                s = float(y[i][k] / y[k][k])
                y[i] -= s * y[k]
    return y[:, -1]


inp = input().strip().split(' ')
n = int(inp[0])
m = int(inp[1])

matrix = np.full(n * n, 0, dtype='f').reshape(n, n)
l = np.full(n * n, 0, dtype='f').reshape(n, n)

for i in range(n):
    a = input().strip().split(' ')
    for j in range(n):
        a[j] = float(a[j])
    matrix[i] = a

output = ''
get_l_u_form(matrix, l)

while m > 0:
    b = input().strip().split(' ')
    for j in range(n):
        b[j] = int(b[j])
    ret = get_lyb(np.copy(l), b)
    ret2 = get_uxy(np.copy(matrix), ret)

    output += str(np.round(ret2, 4))
    m = m - 1
print(output.replace('[', '').replace(']', '\n'))
