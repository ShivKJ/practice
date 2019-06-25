"""
given [a0,a1,a2,...,an]
create function f(x) = a0 + a1*x + a2*x**2 .. +an*x**n
"""


def get(coeff):
    def fun(x):
        y = 0

        for a in reversed(coeff):
            y = a + x * y

        return y

    return fun
