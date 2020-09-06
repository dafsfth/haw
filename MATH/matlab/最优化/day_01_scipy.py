"""
optimize = SciPy“优化”提供最小化（或最大化）的函数目标函数，可能受约束。它包括
非线性问题的求解器（支持局部和全局优化算法），线性规划，约束非线性最小二乘法、寻根和曲线拟合。

> minimize_scalar: 一元函数极小化的接口  brent  bounded  golden


> 局部（多元）优化:
>> minimize :    多元函数极小化的接口  neldermead  powell cg  bfgs  newtoncg  lbfgsb  tnc  cobyla  slsqp trustconstr  dogleg trustncg trustkrylov  trustexact

> 全局优化
>> basinhopping   Basinhopping随机优化器
>> brute  强力搜索优化器
>> differential_evolution  基于微分进化的随机极小化
>> shgo  单纯形同调全局优化
>> dual_annealing  双退火随机优化器


> 最小二乘法与曲线拟合

>> 非线性最小二乘法:
>>> # least_squares   求解一个变量有界的非线性最小二乘问题

>> 线性最小二乘法:
>>> # nnls  具有非负约束的线性最小二乘问题
>>> # lsq_linear  有界约束的线性最小二乘问题。


Curve Fitting:
寻根
====================================

标量型函数
-------------------------------------
root_scalar  标量函数非线性解算器的统一接口。
brentq       二次插值Brent方法
brenth         用双曲外推法修正Harris修正的Brent方法
ridder          里德方法。
bisect        对分法
newton        牛顿法（也叫割线法和哈雷法）。
toms748             Alefeld，Potra&Shi算法748
RootResults    某些根查找程序返回的根查找结果。

fixed_point    单变量定点解算器

多维的
--------------------------------------
root : 多元函数非线性求解器的统一接口。
    optimize.root-hybr
   optimize.root-lm
   optimize.root-broyden1
   optimize.root-broyden2
   optimize.root-anderson
   optimize.root-linearmixing
   optimize.root-diagbroyden
   optimize.root-excitingmixing
   optimize.root-krylov
   optimize.root-dfsane

线性规划
===================================================
linprog  线性规划问题极小化的统一接口
    optimize.linprog-simplex
   optimize.linprog-interior-point
   optimize.linprog-revised_simplex

分配问题
---------------------------------------------------
linear_sum_assignment   解决线性和分配问题


有限差分近似
----------------------------------------------------
approx_fprime - 近似标量函数的梯度。
check_grad - 使用有限差分检查提供的导数。

行搜索
------------------------------------------------------
bracket - 给两个起点加上一个最小值。
line_search -  返回满足强Wolfe条件的步骤。


黑森近似
------------------------------------------------------
LbfgsInvHessProduct - BFGS线性近似逆算子。
HessianUpdateStrategy - 实现Hessian更新策略的接口

基准问题
-----------------------------------------------------
rosen - 罗森布鲁克函数.
   rosen_der - 罗森布鲁克函数的导数。
   rosen_hess - Rosenbrock函数的Hessian矩阵。
   rosen_hess_prod - Rosenbrock-Hessian和向量的乘积。

遗留函数
================
Optimization

通用多变量方法：
------------------------------------------------------
fmin - Nelder-Mead单纯形算法。
   fmin_powell - 鲍威尔（改进的）水平集方法。
   fmin_cg - 非线性（Polak-Ribiere）共轭梯度算法。
   fmin_bfgs - 拟牛顿法（Broydon-Fletcher-Goldfarb-Shanno）。
   fmin_ncg - 线搜索牛顿共轭梯度。

约束多元方法
-------------------------------------------------------------
fmin_l_bfgs_b - Zhu，Byrd和Nocedal的约束优化器。
   fmin_tnc - 截断牛顿码。
   fmin_cobyla - 线性逼近约束优化。
   fmin_slsqp - 使用序列最小二乘规划最小化。


单变量（标量）极小化方法
---------------------------------------------------------------
fminbound - 标量函数的有界极小化。
   brent - 基于Brent方法的一维函数极小化。
   golden - 一维函数极小化的黄金分割法。


Least-Squares
----------------------------------------------------------------
leastsq - 在N个未知数中最小化M方程的平方和。


Root Finding
=========================
一般非线性解算器
----------------------------------------------------------------
fsolve - 非线性多变量方程求解器。
   broyden1 - Broyden's first method.
   broyden2 - Broyden's second method.


大规模非线性求解器:
-----------------------------------------
newton_krylov
   anderson


简单迭代求解器：
-----------------------------------------------
excitingmixing
   linearmixing
   diagbroyden
"""


from scipy import optimize
import numpy as np
from pylab import *


# 单变量
methods = ['brent', 'bounded', 'golden']
# 有界选择bounded , 无界选其他两个


# 求解x = 2 * e ^ (-x) *sin(x)  在0-8上的最大值与最小值
def test1():
    f = lambda x: 2 * np.exp(-x) * np.sin(x)
    result = optimize.minimize_scalar(f, bounds=(0, 5), method='bounded')
    print(result)

    x = linspace(-1, 9, 1000)
    plot(x, f(x), '-r', result.x, result.fun, 'g*')
    # axvline(result['fun'], c='g')
    show()


def test2():
    f = lambda x: x ** 2 - 1

    result = optimize.minimize_scalar(f)
    x = linspace(-2, 2, 1000)
    plot(x, f(x), result.x, result.fun, 'r*')
    show()


def test3():
    fun = lambda x: (x[0] - 0.667) / (x[0] + x[1] + x[2] - 2)

    cons = ({'type': 'eq', 'fun': lambda x: x[0] * x[1] * x[2] - 1},  # xyz=1
            {'type': 'ineq', 'fun': lambda x: x[0] - e},  # x>=e，即 x > 0
            {'type': 'ineq', 'fun': lambda x: x[1] - e},
            {'type': 'ineq', 'fun': lambda x: x[2] - e}
            )

    x0 = np.array((1.0, 1.0, 1.0))  # 设置初始值
    res = optimize.minimize(fun, x0, method='SLSQP', constraints=cons)

    print(res)


def f(x):
    return (x - 2) * x * (x + 2) ** 2


def test4():
    res1 = optimize.minimize_scalar(f)
    res2 = optimize.minimize_scalar(f, bounds=(-3, -1), method='bounded')

    x = linspace(-10, 10, 1000)
    plot(x, f(x), res1.x, res1.fun, 'r*', res2.x, res2.fun, 'go')
    axhline(y=res1.fun)
    show()


# 多变量
"""
methods = [neldermead  powell cg  bfgs  newtoncg  lbfgsb  tnc  cobyla  slsqp trustconstr  dogleg trustncg trustkrylov  trustexact]
"""

"""
# 共轭梯度cg   fun: 4.5395122487997524e-14   x: array([ 0.50000009, -1.00000017])   cannot handle constraints nor bounds.
拟牛顿法bfgs:  fun: 9.34993218057605e-13     x: array([ 0.50000023, -1.00000071])  bfgs方法不能处理约束或边界。
cobyla  fun: 9.890387018443644e-08    x: array([ 0.50001972, -1.00019178])  cobyla cannot handle bounds.
tnc    fun: 2.3650455456105924e-11     x: array([ 0.49999852, -0.99999629])
slsqp   fun3.481012019557851e-10          x: array([ 0.49999184, -0.9999856 ])

"""

def test5():
    f = lambda x: (4 * x[0]**2 + 2 * x[1] ** 2 + 4*x[0]*x[1] + 2*x[1] + 1) * exp(x[0])
    result = optimize.minimize(f, x0=[-1, 1], method='slsqp', bounds=([0.4, 0.6], [-2, 0]))
    print(result)


def test6():
    x = [
        4.5395122487997524e-14,
        9.34993218057605e-13,
        2.3650455456105924e-11,
        9.890387018443644e-08,
        3.481012019557851e-10,
        1.3029e-10
    ]
    y = sort(x)
    print(y)


def test7():
    f = lambda x: 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2
    x, y = meshgrid(linspace(-2, 2, 40), linspace(-1, 3, 40))

    # # 画图
    # fig = figure()
    # ax = Axes3D(fig)
    #
    # # subplot(121)
    # ax.plot_surface(x, y, f([x, y]), rstride=1, cstride=1, cmap='rainbow')
    # # contourf(x, y, f([x, y]), zdir='z', offset=-2, cmap='hot')
    #
    # figure(2)
    #
    # contourf(x, y, f([x, y]), 8, alpha=.8)
    # c = contour(x, y, f([x, y]))
    # clabel(c, inline=1, fontsize=10, colors='k')
    #
    # show()
    result = optimize.minimize(f, x0=(-1.2, 2), method='slsqp')
    print(result)


# 全局最优化
def test8():
    f = lambda x: (4 * x[0] ** 2 + 2 * x[1] ** 2 + 4 * x[0] * x[1] + 2 * x[1] + 1) * exp(x[0])

    # 用跳盆算法求函数的全局最小值
    result1 = optimize.basinhopping(f, x0=[-1, 1])

    # 在给定范围内用蛮力最小化函数。
    # result2 = optimize.brute(f, ranges=(-2, 2))
    # print(result2)

    # 求多元函数的全局最小值。
    result3 = optimize.differential_evolution(f, bounds=([-1, 1], [-2, 0]))
    # print(result3)

    # 使用SHG(简单同调全局优化”)优化法求函数的全局最小值
    result4 = optimize.shgo(f, bounds=([-1, 1], [-2, 0]))
    print(result4)

    # 用对偶退火法求函数的全局最小值
    result5 = optimize.dual_annealing(f, bounds=([-1, 1], [-2, 0]))
    print(result5)


# 寻根
def test9():
    f = lambda x: x**2 + 2*x + 1
    # resul1t = optimize.root_scalar(f)

    result2 = optimize.brent(f)
    print(result2)

    result3 = optimize.fsolve(f, x0=0)
    print(result3)


# 线性规划
"""
        A_ub @ x <= b_ub
        A_eq @ x == b_eq
        lb <= x <= ub
"""
# min 13x1 + 9x2 + 10x3 + 11x4 + 12x5 + 8x6


def test10():
    c = np.array([13, 9, 10, 11, 12, 8])    # 目标函数的系数
    A_ub = np.array([[0.4, 1.1, 1, 0, 0, 0], [0, 0, 0, 0.5, 1.2, 1.3]])  # 不等式约束矩阵
    b_ub = np.array([800, 900])
    A_eq = np.array([[1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]])  # 等式约束矩阵
    b_eq = np.array([400, 600, 500])
    result = optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq)  # 默认情况下，边界是`（0，无）
    f = lambda x, y: x * y
    sum = 0
    for x, y in zip(result['x'], c):
        sum += f(x, y)
    print(sum)


# 指配问题
def test11():
    eff_mat = np.array([
        [12, 7, 9, 7, 9],
        [8, 9, 6, 6, 6],
        [7, 17, 12, 14, 12],
        [15, 14, 6, 6, 10],
        [4, 10, 7, 10, 6]
    ])
    row_index, col_index = optimize.linear_sum_assignment(eff_mat)
    print(row_index, col_index)
    print(eff_mat[row_index, col_index])



if __name__ == '__main__':
    test7()