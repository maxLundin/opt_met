import numpy as np

def ih_govno_funkcia(a, ind, c):
    pass

systema = [
    [1, 2, 3, "<=", 3],
    [1, 2, 3, "<=", 3],
    [1, 2, 3, ">=", 3]
]

c = [1, 2, 3, 44]

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

    ih_govno_funkcia(systema, indexes, c)


if __name__ == '__main__':
    doit()
