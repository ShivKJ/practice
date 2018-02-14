import numpy as np
from numpy import ndarray, array


def largest_eigen(A: ndarray, v: ndarray, tol=1e-8, iter=100):
    '''
    This method finds largest eigen value and corresponding eigen vector
    for a given matrix A with initial start vector v. This method
    is also known as power method.

    v_0 = v

    y_k+1 = Av_k
    v_k+1 = y_k+1 / max(abs(y_k+1))

    lambda = lim ((y_k+1)r_th) / (v_k)r_th, r = 0,1,2, ... len(v)
             k->inf

    :param A:
    :param v:
    :param tol:
    :param iter:
    :return:
    '''
    A = array(A)
    v = array(v) / v.max()
    idx, r = 0, 1

    y = A @ v

    lam = y[r] / v[r]
    v = y / np.abs(y).max()

    while idx < iter:
        y = A @ v
        _lam = y[r] / v[r]

        if abs(lam - _lam) < tol:
            return _lam, v

        lam = _lam
        v = y / np.abs(y).max()
        idx += 1

    return lam, v


if __name__ == '__main__':
    A = array([[-15, 4, 3], [10, -12, 6], [20, -4, 2]])
    v = array([1, 1, 1])
    print(largest_eigen(A, v))
