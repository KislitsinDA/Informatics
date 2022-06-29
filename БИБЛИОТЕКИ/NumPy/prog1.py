import numpy as np


def make_field(size):
    x = np.ones((size, size), dtype="int8")
    for i in range(len(x)):
        if i != 0 and i % 2 != 0:
            x[i][0] = 0

        for j in range(1, len(x[i])):
            if x[i][j - 1] == 0:
                x[i][j] = 1

            else:
                x[i][j] = 0
    return x


print(make_field(5))
