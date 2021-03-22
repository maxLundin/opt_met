import functions
import numpy as np


def dihotomi(f, left_border, right_border, eps=1e-6):
    iters = 0
    delta = eps / 4
    while right_border - left_border > eps:
        iters += 1
        mid = (left_border + right_border) / 2
        x1 = mid - delta
        x2 = mid + delta
        f1 = f(x1)
        f2 = f(x2)
        if f1 < f2:
            right_border = x2
        elif f1 > f2:
            left_border = x1
        else:
            return mid, iters
    return (left_border + right_border) / 2, iters


def search_range_with_min(f, x0, step=0.1, eps=1e-6, max_iter=1e4):
    if f(x0) < f(x0 + step):
        x0 += step
        step *= -1

    it = 0
    y0 = f(x0)
    x = x0 + step

    while f(x) <= y0 + eps and it < max_iter:
        step *= 2
        x += step
        it += 1

    if step > 0:
        return x0, x
    return x, x0


def calculate_step(f, x, grad):
    step_f = lambda step: f(x + step * grad)
    left, right = search_range_with_min(step_f, 0)
    arg, _ = dihotomi(step_f, left, right)
    return arg


def gradient_descent(f, f_grad, x0, eps=1e-6, max_iter=1e6):
    x = x0
    it = 0
    trace = [x]

    s = -f_grad(x)

    while True:
        lamb = calculate_step(f, x, s)
        next_x = x + lamb * s

        s = -f_grad(next_x) + s * (np.linalg.norm(f_grad(next_x)) / np.linalg.norm(f_grad(x))) ** 2

        if abs(f(next_x) - f(x)) < eps or np.linalg.norm(s) < eps or it >= max_iter:
            return x, trace

        trace.append(x)
        x = next_x
        it += 1


def analyze(f, x_border, y_border, f_grad, x0):
    return functions.analyze(f, x_border, y_border, lambda: gradient_descent(f, f_grad, x0))
