import numpy as np
from simplex import *


def ih_govno_funkcia(a, ind, c):
    print()
    print(find_min(a[:, :-1], a[:, -1], c))


# systema = [
#     [1, 2, "<=", 7],
#     [2, 1, "<=", 8],
#     [0, 1, "<=", 3],
#     [1, 0, ">=", 0],
#     [0, 1, ">=", 0],
# ]
#
# c = [3, 2]

systema = [
    [3, 1, -1, 1, "==", 4],
    [5, 1, 1, -1, "==", 4],
    [1, 0, 0, 0, ">=", 0],
    [0, 1, 0, 0, ">=", 0],
    [0, 0, 1, 0, ">=", 0],
    [0, 0, 0, 1, ">=", 0],
]

c = [-6, -1, -4, 5]

# systema = [
#     [2, -1, 1, 0, "==", 1],
#     [-1, 2, 0, 1, "==", 1],
#     [1, 0, 0, 0, ">=", 0],
#     [0, 1, 0, 0, ">=", 0],
#     [0, 0, 1, 0, ">=", 0],
#     [0, 0, 0, 1, ">=", 0],
# ]
#
# c = [1, 1, -2, -3]

indexes = []
syslen = systema[0].__len__() - 2


def dole(i):
    systema[i][-2] = "=="
    global syslen
    indexes.append(syslen)
    systema[i][syslen] = 1
    syslen += 1


def doge(i):
    for j in range(len(systema[i]) - 2):
        systema[i][j] *= -1
    systema[i][-1] *= -1
    dole(i)


def preproc():
    global c
    c += [0] * len(systema)
    for i in range(len(systema)):
        systema[i] = systema[i][:-2] + [0] * len(systema) + systema[i][-2:]


def postproc():
    for i in range(len(systema)):
        systema[i] = systema[i][:-2] + systema[i][-1:]


def doit():
    preproc()
    for i in range(len(systema)):
        if (systema[i][-2] == "<="):
            dole(i)
        elif (systema[i][-2] == ">="):
            doge(i)
        elif (systema[i][-2] == "=="):
            pass
        else:
            print("operator govno")
            return
    print(np.array(systema))
    print(np.array(indexes))
    postproc()
    print(np.array(systema))
    print(np.array(c))

    ih_govno_funkcia(np.array(systema), indexes, c)


if __name__ == '__main__':
    doit()
