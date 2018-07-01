from numpy import array, diag
from numpy.linalg import inv

LAMBDA = (1 + 5 ** 0.5) / 2

NORMALIZATION1 = (LAMBDA ** 2 + 1) ** 0.5
NORMALIZATION2 = ((1 / LAMBDA) ** 2 + 1) ** 0.5

P = array([[LAMBDA / NORMALIZATION1, -1 / LAMBDA / NORMALIZATION2],
           [1 / NORMALIZATION1, 1 / NORMALIZATION2]])

P_INV = inv(P)

X = array([1, 0])


def fib(n: int):
    if n <= 1:
        return n

    D = diag([LAMBDA ** (n - 1), (-1 / LAMBDA) ** (n - 1)])

    return int((P @ D @ P_INV @ X)[0])
