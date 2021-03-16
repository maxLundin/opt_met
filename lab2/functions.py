import numpy as np
from math import exp
import plotly.graph_objects as go
import datetime


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


def f3_grad(x):
    return np.array([-2 / 3 * (x[0] - 2) * exp(-1 / 9 * (x[0] - 2) ** 2 - 0.25 * (x[1] - 3) ** 2) - (x[0] - 1) * exp(
        -0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2),
                     -1.5 * (x[1] - 3) * exp(-1 / 9 * (x[0] - 2) ** 2 - 0.25 * (x[1] - 3) ** 2) - 4 * (x[1] - 1) * exp(
                         -0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2)])


def f3_hess(x):
    return np.array([[4 / 27 * (x[0] - 2) ** 2 * exp(-1 / 9 * (x[0] - 2) ** 2 - 0.25 * (x[1] - 3) ** 2) - 2 / 3 * exp(
        -1 / 9 * (x[0] - 2) ** 2 - 0.25 * (x[1] - 3) ** 2) - exp(-0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2) + 0.5 * (
                              x[0] - 1) ** 2 * exp(-0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2),
                      1 / 3 * (x[0] - 2) * (x[1] - 3) * exp(-1 / 9 * (x[0] - 2) ** 2 - 0.25 * (x[1] - 3) ** 2) + 2 * (
                              x[0] - 1) * (x[1] - 1) * exp(-0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2)],
                     [1 / 3 * (x[0] - 2) * (x[1] - 3) * exp(-1 / 9 * (x[0] - 2) ** 2 - 0.25 * (x[1] - 3) ** 2) + 2 * (
                             x[0] - 1) * (x[1] - 1) * exp(-0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2),
                      0.75 * (x[1] - 3) ** 2 * exp(-1 / 9 * (x[0] - 2) ** 2 - 0.25 * (x[1] - 3) ** 2) - 1.5 * exp(
                          -1 / 9 * (x[0] - 2) ** 2 - 0.25 * (x[1] - 3) ** 2) - 4 * exp(
                          -0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2) + 8 * (x[1] - 1) ** 2 * exp(
                          -0.25 * (x[0] - 1) ** 2 - (x[1] - 1) ** 2)]])


def analyze(f, x_border, y_border, method):
    x = np.linspace(x_border[0], x_border[1], 50)
    y = np.linspace(y_border[0], y_border[1], 50)
    z = np.vectorize(lambda x, y: f(np.array([x, y])))(*np.meshgrid(x, y))

    fig = go.Figure()
    fig.add_trace(
        go.Contour(
            x=x, y=y,
            z=z,
            contours_coloring='lines',
            line_width=2
        ))

    start_time = datetime.datetime.now()
    res, trace = method()
    end_time = datetime.datetime.now()
    print(res, 'Microseconds ' + str((end_time - start_time).microseconds))

    xy = trace
    print(f'step count = {len(xy)}')
    fig.add_trace(
        go.Scatter(
            x=[p[0] for p in xy],
            y=[p[1] for p in xy],
        )
    )

    fig.show()
