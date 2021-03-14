import numpy as np
from math import exp
import matplotlib as plt


def f1(x):
    return 100 * (x[1] - x[0]) ** 2 + (1 - x[0]) ** 2


def f1_grad(x):
    return np.array([202 * x[0] - 200 * x[1] - 2, 200 * x[1] - 200 * x[0]])


def f1_hess(x):
    return np.array([[202, -200], [-200, 200]])


def f2(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def f2_grad(x):
    return np.array([400 * x[0] ** 3 - 400 * x[0] * x[1] + 2 * x[0] - 2, 200 * x[1] - 200 * x[0] ** 2])


def f2_hess(x):
    return np.array([[-400 * x[1] + 1200 * x[0] ** 2 + 2, -400 * x[0]], [-400 * x[0], 200]])


def f3(x):
    return 2 * exp(-0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2) + \
           3 * exp(-1 * (1 / 3 * (x[0] - 2)) ** 2 - 0.25 * (x[1] - 3) ** 2)


def analyze(method, f, f_grad, f_hess, x0, x_min, x_max, x_step, y_min, y_max, y_step):
    x_s = np.arange(x_min, x_max, x_step)
    y_s = np.arange(y_min, y_max, y_step)
    z_s = np.array([[f(np.array([x, y])) for x in x_s] for y in y_s])

    plt.plot()

    plt.show()