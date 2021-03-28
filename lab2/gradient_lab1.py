import functions
import numpy as np
from gradient_descent import calculate_step


def gradient_lab1(f, f_grad, x0, eps=1e-6, max_iter=1e6):
    x = x0
    it = 0
    trace = [x]

    while True:
        grad = -f_grad(x)

        step = calculate_step(f, x, grad)
        next_x = x + step * grad

        if abs(f(next_x) - f(x)) < eps or np.linalg.norm(grad) < eps or it >= max_iter:
            return x, trace

        trace.append(x)
        x = next_x
        it += 1


def analyze(f, x_border, y_border, f_grad, x0):
    return functions.analyze(f, x_border, y_border, lambda: gradient_lab1(f, f_grad, x0))
