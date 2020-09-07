from sympy import *
import scipy
import matplotlib.pyplot as plt
import numpy as np




# 微分方程

# dsolve(eq, f(x), hint)
# # 可以是任何受支持的常微分方程   # f(x)是一个变量的函数，该变量的导数   # hint是您要使用dsolve的求解方法

"""
一阶常微分方程
================================

对于常微分方程组
===============================
eq”是函数的列表
from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import x
f = Function('f')
dsolve(Derivative(f(x), x, x) + 9*f(x), f(x))
"""
# scipy.integrate.odeint


def dif1(x, f):
    return diff(f(x), x, 2) + f(x)      # f(x)''+f(x)=0 二阶常系数齐次微分方程


def test1():
    x = symbols('x')  # 变量
    f = Function('f')  # 函数
    result = dsolve(dif1(x, f), f(x))

    pprint(result)  # 漂亮的打印


def dif2(x, f):
    return diff(f(x), x) - x**2 - 1


def test2():
    f = Function('f')  # 函数
    u = symbols('u')   # 变量
    result = dsolve(dif2(u, f), f(u))
    pprint(result)


def dif3(x, f):
    return diff(f(x), x, 2) + 4 * diff(f(x), x) + 29 * f(x)

"""
    {f(x0): x1, f(x).diff(x).subs(x, x2):x3}`
"""


def test3():
    x = symbols('x')
    f = Function('f')
    result = dsolve(dif3(x, f), f(x), ics={f(0): 0, f(x).diff(x).subs(x, 0): 15})
    print(result)
    pprint(result)


def test4():
    x, C1, C2, e = symbols('x, C1, C2, e')
    f = (C1 * sin(5 * x) + C2 * cos(5 * x)) * e**(-2*x)
    result = diff(f, x)
    print(result)


# 求导
def test5():
    init_printing()
    u, v = symbols('u v')
    x, y, z = symbols('x y z')
    u = x * y
    v = x + y
    z = E ** u * sin(v)
    pprint(z.diff(x))
    pprint(z.diff(y))


def test6():
    u, v = symbols('u, v')
    x, y, z, t = symbols('x, y, z, t')
    u = E ** t
    v = cos(t)
    z = u * v + sin(t)
    pprint(z.diff(t))


# 隐函数求导
def test7():
    x, y, z = symbols('x y z')
    f = x ** 2 + y ** 2 -9
    result = idiff(f, x, y)   # x y 那个在前
    print(result)


# 求偏导
def test8():
    x, y, z = symbols('x y z')
    expr = x ** 2 + y ** 2 + z ** 2 - 4 * z
    result = idiff(expr, z, x, 2)
    print(result)


# 多元方程组求导
def test9():
    x, y = symbols('x y')
    u = Function('u')(x, y)
    v = Function('v')(x, y)
    f1 = x * u - y * v
    f2 = y * u + x * v - 1
    pprint(f1.diff(x))
    pprint(f2.diff(y))


def f4(x, f):
    return diff(f(x), x, 2) - 1000*(1-f(x)**2) * diff(f(x), x) - f(x)


def test11():
    x = symbols('x')
    f = Function('f')
    result = dsolve(f4(x, f), f(x), ics={f(0): 0, f(x).diff(x).subs(x, 0): 0})
    print(result)


"""
t = symbols('t')
x, y = symbols('x, y', cls=Function)
eq = (Eq(Derivative(x(t),t), 12*t*x(t) + 8*y(t)), Eq(Derivative(y(t),t), 21*x(t) + 7*t*y(t)))
dsolve(eq)



from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import x
f = Function('f')
dsolve(Derivative(f(x), x, x) + 9*f(x), f(x))
Eq(f(x), C1*sin(3*x) + C2*cos(3*x))
"""

# 微分方程组
def test10():
    t = symbols('t')
    x, y, z = symbols('x y z', cls=Function)
    eq = (Eq(Derivative(x(t), t), 2*x(t) - 3*y(t) + 3*z(t)),
          Eq(Derivative(y(t), t), 4*x(t) -5*y(t) + 3*z(t)),
          Eq(Derivative(z(t), t), 4*x(t) - 4*y(t) + 2*z(t)))
    result = dsolve(eq)
    pprint(result)


def test12():
    t = symbols('t')
    x, y = symbols('x y', cls=Function)
    eq = (Eq(Derivative(x(t), t), sqrt(5 * (1 - t) / (1 - x(t))**2 + (t - y(t))**2)),
          Eq(Derivative(y(t), t), sqrt(5 * (t - y(t)) / (1 - x(t))**2 + (t - y(t))**2)))

    result = dsolve(eq=eq)
    print(result)

d



if __name__ == '__main__':
    test12()
