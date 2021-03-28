import numpy as np
from copy import deepcopy


def find_min(matrix, pos_ind, f):
    f = np.array(f.copy() + [0]).astype(dtype=float)
    matrix = np.array(matrix.copy()).astype(dtype=float)

    # print(matrix)

    max_el_col = np.argmax(f[:-1])
    basis = [-1 for _ in range(len(matrix))]

    while f[max_el_col] > 0:

        min_row_b = -1
        min_b = np.inf

        for i in range(len(matrix)):
            if matrix[i, max_el_col] > 0:
                b_res = matrix[i, -1] / matrix[i, max_el_col]

                if b_res < min_b:
                    min_row_b = i
                    min_b = b_res

        if min_row_b == -1:
            print("gg")
            return

        resolve_el = matrix[min_row_b, max_el_col]
        basis[min_row_b] = max_el_col

        for i in range(len(matrix)):
            if i == min_row_b:
                continue
            else:
                if matrix[i, max_el_col] != 0:
                    k = matrix[i, max_el_col] / resolve_el
                    matrix[i] = matrix[i] - matrix[min_row_b] * k

        k = f[max_el_col] / resolve_el
        f = f - matrix[min_row_b, :] * k
        matrix[min_row_b] = matrix[min_row_b] / resolve_el

        max_el_col = np.argmax(f[:-1])

    res = [0 for _ in range(len(basis))]
    for i in range(len(basis)):
        if basis[i] != -1:
            res[basis[i]] = matrix[i, -1] / matrix[i, basis[i]]

    # print(res)
    # print(f)
    # print(basis)
    # print(matrix)
    return res
