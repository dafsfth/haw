from scipy.cluster.vq import kmeans, vq, whiten
from scipy.fftpack import fft, ifft
from pylab import *
import math, sympy
from scipy import optimize
from scipy import interpolate


rcParams['font.sans-serif'] = ['SimHei']  # 乱码
rcParams['axes.unicode_minus'] = False


def test1_cluster():
    data = vstack((random.rand(100, 3) + array([.5, .5, .5]), random.rand(100, 3)))

    # 数据白化: 去除样本数据的冗余信息。
    data = whiten(data)

    # 分成3个聚类
    center, _ = kmeans(data, 3)

    # clx标出了对应索引样本的聚类，dist表示对应索引样本与聚类中心的距离。
    clx, dist = vq(data, center)  # 将样本数据中的每个样本点分配给一个中心点，形成3个聚类

    print(clx)


def test2_fftpack():
    """
    傅里叶变换
    :return:
    """
    x = array([1.0, 2.0, 1.0, -1.0, 1.5])

    # 对数组进行傅里叶变换
    y = fft(x)
    print(y)

    # 快速傅里叶逆变换
    y1 = ifft(x)
    print(y1)


def f2(x, a, b):
    return a * (x ** 2) + b


#  积分
def test3_integrate():
    import scipy.integrate
    f = lambda x: exp(-x**2)
    i = scipy.integrate.quad(f, 0, 5)   # 第一个值是积分的值，第二个值是对积分值的绝对误差估计。
    print(i)
    i2 = scipy.integrate.quad(f2, 0, 1, args=(3, 1))
    print(i2)

    # 重积分
    from math import sqrt
    f3 = lambda x, y: 19*x*y
    g = lambda x: 0
    h = lambda y: sqrt(1 - 4*y**2)
    i3 = scipy.integrate.dblquad(f3, 0, 0.5, g, h)
    print(i3)


def test4_interpld():
    from scipy import interpolate
    x = linspace(0, 4, 12)
    y = cos(x**2 / 3 + 4)
    plot(x, y, '-r*')
    f1 = interpolate.interp1d(x, y, kind='linear')
    f2 = interpolate.interp1d(x, y, kind='cubic')

    x_new = linspace(0, 4, 40)
    plot(x, y, 'o', x_new, f1(x_new), '-', x_new, f2(x_new), '--')
    legend(['data', 'linear', 'cubic','nearest'], loc='best')
    show()


# 线性代数
def test5_linalg():
    from scipy import linalg
    a = array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
    b = array([10, 8, 3])

    x = linalg.solve(a, b)
    print(x)


# 最优化
def test6_optimize():

    from sympy import diff, symbols
    f = lambda x: x**2 + x*2 + 9
    x1 = linspace(-10, 10, 100)
    plot(x1, f(x1))
    xopt = optimize.fmin_bfgs(f, 0)  # 第二个参数是梯度下降的起点

    xmin = xopt[0]
    ymin = f(xmin)
    scatter(xmin, ymin, s=20, c='r')
    show()


def test7():
    f = lambda x: x**2 + 20 * sin(x)
    x1 = linspace(-10, 10, 100)
    xopt = optimize.fmin_bfgs(f, 7)
    xmin = xopt[0]
    ymin = f(xmin)

    # basinhopping  全局最小
    ret = optimize.basinhopping(f, 0)
    # print(ret)

    # fminbound 局部最优
    s3 = optimize.fminbound(f, -10, -5)
    print(s3)

    # x1min = ret[0]
    # y1min = f(x1min)

    subplot(121)
    plot(x1, f(x1), xmin, ymin, 'r*')

    subplot(122)
    # plot(x1, f(x1), x1min, y1min, 'ro')
    # show()


# 函数求解
def test8_fsolve():
    f = lambda x: x**2 + 20 * sin(x)
    ret = optimize.fsolve(f, 1)

    # x2 = sympy.symbols('x')
    # y = sympy.diff(f, x2)
    # result1 = optimize.fsolve(y, 0)
    # print(result1)
    x1 = linspace(-10, 10, 100)
    plot(x1, f(x1), '-ro')
    show()
    print(ret)


def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [
        4 * x1 + 9,
        3 * x0**2 - sin(x1 * x2),
        x1 * x2 - 2.5
    ]


# 解方程组
def test9_fsolve():
    result = optimize.fsolve(f, [1, 1, 1])
    print(result)


def g(x, a, b):
    return a * cos(x) + b


# 拟合
def test10_curve_fit():
    x_data = linspace(-5, 5, 100)
    y_data = g(x_data, 50, 2) + 5 * np.random.randn(x_data.size)

    a, b = optimize.curve_fit(g, x_data, y_data)
    # b 对角线元素值表示每个参数的方差

    plot(x_data, y_data, 'r*', x_data, g(x_data, a[0], a[1]), '-b')
    show()
    print('系数：', a)
    print(b)


X = np.array([160, 165, 158, 172, 159, 176, 160, 162, 171])
Y = np.array([58, 63, 57, 65, 62, 66, 58, 59, 62])


# 最小二乘法
def test11_leastsq():
    # optimize.leastsq(func, x0, args=())
    # func 计算误差的函数   x0 是计算的初始参数值   args 是指定func的其他参数
    result1 = optimize.leastsq(residuals, [1, 0])
    k, b = result1[0]
    y = k * X + b
    print('k=', k, 'b=', b)
    plot(X, Y, 'r*', X, y, '-b')
    show()


# 偏差函数, 计算以p为参数的直线和原始数据之间的误差
def residuals(p):
    k, b = p
    return Y - (k * X + b)


# 插值
def test12():
    x = np.linspace(0, 2*pi+pi/4, 10)
    y = sin(x)

    x_new = linspace(0, 2*pi+pi/4, 100)
    f_linear = interpolate.interp1d(x, y)

    tck = interpolate.splrep(x, y)
    y_bsplrep = interpolate.splev(x_new, tck)

    plot(x, y, 'ro', label='原始数据')
    plot(x_new, f_linear(x_new), 'r', label='线性插值')
    plot(x_new, y_bsplrep, 'g', label='B-spline插值')

    legend(loc='best')

    show()


def test13():
    x = linspace(0, 10, 11)
    y = sin(x)

    ax = plot()
    plot(x, y, 'ro')

    # 建立插值数据点
    x_new = linspace(0, 10, 101)
    for kind in ['nearest', 'zero','linear','quadratic']:
        f = interpolate.interp1d(x, y, kind=kind)
        y_new = f(x_new)

        plot(x_new, y_new, label=str(kind))

    legend(loc='best')

    show()


if __name__ == '__main__':
    test13()