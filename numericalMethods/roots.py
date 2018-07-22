from typing import Callable

Function = Callable[[float], float]


def bisection_method(f: Function, a: float, b: float,
                     tol=1e-8, max_itr=100) -> float:
    if abs(f(a)) < tol:
        return a

    if abs(f(b)) < tol:
        return b

    assert f(a) * f(b) < 0

    itr = 0

    while abs(a - b) > tol and itr < max_itr:
        x = (a + b) / 2
        f_x = f(x)

        if abs(f_x) < tol:
            return x

        if f(a) * f_x < 0:
            b = x
        else:
            a = x

        itr += 1

    return (a + b) / 2


def scant(f: Function, a: float, b: float, tol=1e-8, max_itr=100) -> float:
    if abs(f(a)) < tol:
        return a

    if abs(f(b)) < tol:
        return b

    k_1, k = a, b
    fk_1, fk = f(k_1), f(k)

    itr = 0

    while itr < max_itr:
        k_plus_1 = k - (k - k_1) * fk / (fk - fk_1)
        k_1, k = k, k_plus_1
        fk_1, fk = fk, f(k_plus_1)

        if abs(fk) < tol:
            return k

        itr += 1

    return k


def regula_falsi(f: Function, a: float, b: float, tol=1e-8, max_itr=100):
    if abs(f(a)) < tol:
        return a

    if abs(f(b)) < tol:
        return b

    assert f(a) * f(b) < 0

    if f(b) < 0:
        return regula_falsi(f, b, a, tol, max_itr)

    itr = 0

    while itr < max_itr:
        x = b - (b - a) * f(b) / (f(b) - f(a))
        fx = f(x)

        if abs(fx) < tol:
            return x

        if fx > 0:
            b = x
        else:
            a = x
        itr += 1

    return b


def newton_raphson(f: Function, derivative_f: Function, a: float,
                   tol=1e-8, max_itr=100):
    if abs(f(a)) < tol:
        return a

    itr = 0

    while itr < max_itr:
        derivative_at_a = derivative_f(a)

        assert abs(derivative_at_a) > tol, 'derivative can not be zero.'

        b = a - f(a) / derivative_at_a

        if abs(f(b)) < tol:
            return b

        a = b

        itr += 1

    return a


def chebyshev_method(f: Function, deri_f: Function, deri_deri_f: Function, a: float,
                     tol=1e-8, max_itr=100):
    if abs(f(a)) < tol:
        return a

    itr = 0

    while itr < max_itr:
        deri_f_a = deri_f(a)
        assert abs(deri_f_a) > 0, 'derivative can not be zero'

        deri_deri_f_a = deri_deri_f(a)
        assert abs(deri_deri_f_a) > 0, 'double derivative can not be zero'

        f_a = f(a)
        b = a - f_a / deri_f_a - (f_a ** 2) * deri_deri_f_a / (deri_f_a ** 3) / 2

        if abs(f(b)) < tol:
            return b

        a = b

        itr += 1

    return a

# if __name__ == '__main__':
#     from math import cos, exp, sin
#
#     f = lambda x: x ** 3 - 5 * x + 1
#
#     a, b = 0, 1
#     print(bisection_method(f, 0, 1))
#     print(scant(f, a, b))
#     print(regula_falsi(f, a, b))
#
#     deri_f = lambda x: 3 * x ** 2 - 5
#
#     print(newton_raphson(f, deri_f, 0.5))
#
#     f = lambda x: cos(x) - x * exp(x)
#     deri_f = lambda x: -sin(x) - exp(x) - x * exp(x)
#
#     print(newton_raphson(f, deri_f, 1, max_itr=2))
#     deri_deri_f = lambda x: -cos(x) - 2 * exp(x) - x * exp(x)
#
#     print(chebyshev_method(f, deri_f, deri_deri_f, 1, max_itr=2))
