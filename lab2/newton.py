import numpy as np
import functions


def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)


def newton(f, f_grad, f_hess, x0, eps=1e-6, max_iter=1e6):
    x = x0
    it = 0
    trace = [x]

    while True:
        grad = f_grad(x)
        hess = f_hess(x)

        if np.linalg.norm(grad) < eps or it >= max_iter:
            return x, trace

        step = grad.dot(np.linalg.inv(hess))
        print(it, x)
        x -= step
        trace.append(x)
        it += 1


def analyze(f, x_border, y_border, f_grad, f_hess, x0):
    return functions.analyze(f, x_border, y_border, lambda: newton(f, f_grad, f_hess, x0))

