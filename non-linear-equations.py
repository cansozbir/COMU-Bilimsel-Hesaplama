from math import exp
from gauss_jordan_elimination import linear_system_solver

def f(x, y):
    return 4 - x**2 - y**2

def dfdx(x, y):
    return -2*x

def dfdy(x, y):
    return -2*y

def g(x, y):
    return 1 - exp(x)- y

def dgdx(x, y):
    return -exp(x)

def dgdy(x, y):
    return -1


xi = float(input('X0 : '))  # x0
yi = float(input('Y0 : '))  # y0

def solver(xi, yi, sens):
    while True:
        m = linear_system_solver([[dfdx(xi, yi), dfdy(xi, yi), -f(xi, yi)],
                                  [dgdx(xi, yi), dgdy(xi, yi), -g(xi, yi)]])
        xi = xi + m[0][-1]
        yi = yi + m[1][-1]
        if m[0][-1] > sens or m[1][-1] > sens:
            break
    return xi, yi


print(solver(xi, yi, 0.001))
