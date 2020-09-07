from pylab import *
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures



rcParams['font.sans-serif'] = ['SimHei']  # 乱码
rcParams['axes.unicode_minus'] = False

"""
离散分布
======================================
    rv_continuous
   rv_discrete
   rv_histogram
   
连续分布
=======================================
多元分布  Multivariate distributions
=======================================
Discrete distributions   离散分布
======================================
汇总统计 Summary statistics
=========================================
Frequency statistics   频率统计
=========================================
相关函数  Correlation functions
========================================
Statistical tests  统计检验
==========================================
Transformations 转换
============================================
统计距离  Statistical distances
=========================================
随机变量生成  Random variate generation
=============================================
循环统计函数Circular statistical functions
============================================
列联表函数 Contingency table functions
===========================================
绘图测试
==========================================
单变量和多元核密度估计
============================================
掩蔽统计函数  Masked statistics functions
"""
# 伯努利分布 0-1分布
def test1():
    x = np.arange(0, 2, 1)  # 定义随机变量
    p1 = 0.5                # 求分布概率  PMF
    pList1 = stats.bernoulli.pmf(x, p1)

    plt.plot(x, pList1, 'ro', ls='None')  # 画图
    plt.vlines(x, 0, pList1)    # x轴， ymin  ymax
    plt.xlabel('随机变量')
    plt.ylabel('概率')

    plt.show()


# 二项分布
def test2():
    n = 5
    p = 0.5
    x = arange(0, n+1, 1)
    p_list = stats.binom.pmf(x, n, p)

    plot(x, p_list, 'ro', ls='None')
    vlines(x, 0, p_list)
    xlabel('随机变量'), ylabel('概率')

    show()


# 集合分布
def test3():
    k = 5   # 第k次成功
    p = 0.6
    x = arange(0, k+1, 1)
    p_list = stats.geom.pmf(x, p)

    plot(x, p_list, 'ro', ls='None')
    vlines(x, 0, p_list, colors=['r', 'b', 'k', 'y', 'w'])
    xlabel('随机变量'), ylabel('概率')

    show()


# 泊松分布
def test4():
    mean1 = 2  # 给定时间范围内某件事发生的平均次数
    k = 4      # 事件的发生次数
    x = arange(0, k+1, 1)

    p_list = stats.poisson.pmf(x, mean1)

    plot(x, p_list, 'ro', ls='None')
    vlines(x, 0, p_list)

    xlabel('随机变量'), ylabel('概率')
    title('泊松分布')

    show()


# 正太分布
def test5():
    u = 0   # 均值
    v = 1
    x = linspace(-5, 5, 100)
    y = stats.norm.pdf(x, u, v)

    plot(x, y, lw=2)
    xlabel('随机变量：x'), ylabel('概率')
    grid()

    title('正太分布')

    show()


# 一元线性回归
"""
linregress
计算两组测量值的线性最小二乘回归

return 
Slope                          回归线的斜率。      a
intercept                       回归线的截距。     b
rvalue                          相关系数。        r^2
pvalue                          
stderr                          估计梯度的标准误差

"""
def test6():
    x = np.array([143, 145, 146, 147, 149, 150, 153, 154, 155, 156, 157, 158,  159, 160, 162, 164])
    y = np.array([88, 85, 88, 91, 92, 93, 93, 95, 96, 98, 97, 96, 98,  99, 100, 102])

    result = stats.linregress(x, y)
    print(result)


def test7():
    x = np.array([143, 145, 146, 147, 149, 150, 153, 154, 155, 156, 157, 158, 159, 160, 162, 164])
    y = np.array([88, 85, 88, 91, 92, 93, 93, 95, 96, 98, 97, 96, 98, 99, 100, 102])
    x = sm.add_constant(x)   # 向数组中添加一列。

    model = sm.OLS(y, x).fit()
    print(model.summary())

    pred = model.predict()    # 预测模型


def test8():
    x = np.array([143, 145, 146, 147, 149, 150, 153, 154, 155, 156, 157, 158, 159, 160, 162, 164])
    y = np.array([88, 85, 88, 91, 92, 93, 93, 95, 96, 98, 97, 96, 98, 99, 100, 102])

    # x, y 加一维数据
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]

    model = linear_model.LinearRegression()
    model.fit(x, y)
    print('斜率是： ', model.coef_)
    print('截距是： ', model.intercept_)


# 多元线性回归
def test9():
    data = pandas.read_excel('data2.xlsx')
    y = data.iloc[:, 1]
    x = data.iloc[:, 2: 6]

    y = y[:, np.newaxis]

    model = linear_model.LinearRegression()
    model.fit(x, y)
    print(model.coef_)
    print(model.intercept_)


"""
PolynomialFeatures
生成多项式和交互特征
======================================================================================
生成一个包含所有多项式组合的新特征矩阵度数小于或等于指定度数的特征。
例如，如果输入样本是二维的[a，b]，二次多项式特征为[1，a，b，a^2，ab，b^2]。

Parameters
-------------------------------------------
degree          多项式特征的次数。默认值为2
>>> from sklearn.preprocessing import PolynomialFeatures
    >>> X = np.arange(6).reshape(3, 2)
    >>> X
    array([[0, 1],
           [2, 3],
           [4, 5]])
    >>> poly = PolynomialFeatures(2)
    >>> poly.fit_transform(X)
    array([[ 1.,  0.,  1.,  0.,  0.,  1.],
           [ 1.,  2.,  3.,  4.,  6.,  9.],
           [ 1.,  4.,  5., 16., 20., 25.]])
    >>> poly = PolynomialFeatures(interaction_only=True)
    >>> poly.fit_transform(X)
    array([[ 1.,  0.,  1.,  0.],
           [ 1.,  2.,  3.,  6.],
           [ 1.,  4.,  5., 20.]])
"""


# 多项式回归
def test10():
    x = mat(linspace(1/30, 14/30, 14)).reshape(14, 1)
    y = mat([11.86, 15.67, 20.60, 26.69, 33.71, 41.93, 51.13, 61.49, 72.90, 85.44, 99.08, 113.77, 129.54, 146.48]).reshape(14, 1)

    model1 = PolynomialFeatures(degree=2)
    x_trans = model1.fit_transform(x)

    mode2 = linear_model.LinearRegression()
    mode2.fit(x_trans, y)

    plot(x, y, 'ro')
    xx = linspace(0, 0.5, 100).reshape(100, 1)
    xx_trans = model1.fit_transform(xx)

    plot(xx, mode2.predict(xx_trans), '-b')

    title('多项式回归')
    xlabel('x'), ylabel('y')
    show()

    print(mode2.coef_)
    print(mode2.intercept_)


def test11():
    x_train = [[6], [8], [10], [14], [18]]
    y_train = [[7], [9], [13], [17.5], [18]]
    x_text = [[7], [9], [11], [15]]
    y_text = [[8], [12], [15], [18]]

    # 多项式回归， 首相生成多项式特征
    quadratic_featurizer = PolynomialFeatures(degree=2)
    x_train_quadratic = quadratic_featurizer.fit_transform(x_train)

    regressor_quadratic = linear_model.LinearRegression()
    regressor_quadratic.fit(x_train_quadratic, y_train)

    xx = np.linspace(0, 26, 100)

    xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))

    plt.plot(xx, regressor_quadratic.predict(xx_quadratic), 'r-', label='quadratic equation')
    plt.legend(loc='upper left')
    plt.show()


# 化为多元线性回归
def test12():
    x = linspace(1 / 30, 14 / 30, 14)
    xx = transpose([[1] * 14, x, x**2])  # 手动将x转化为 1
    y = mat([11.86, 15.67, 20.60, 26.69, 33.71, 41.93, 51.13, 61.49, 72.90, 85.44, 99.08, 113.77, 129.54, 146.48]).reshape(14, 1)

    model = linear_model.LinearRegression()
    model.fit(xx, y)

    print(model.coef_)
    print(model.intercept_)

    plot(x, y, 'ro')
    plot(x, model.predict(xx), '-g')

    show()


# 多元二项式回归(化为多元线性回归)
def test13():

    x = mat([[1000, 600, 1200, 500, 300, 400, 1300, 1100, 1300, 300],
        [5, 7, 6, 6, 8, 7, 5, 4, 3, 9]]).reshape(10, 2)

    x1 = array([1000, 600, 1200, 500, 300, 400, 1300, 1100, 1300, 300])
    x2 = array([5, 7, 6, 6, 8, 7, 5, 4, 3, 9])
    y = mat([100, 75, 80, 70, 50, 65, 90, 100, 110, 60]).reshape(10, 1)

    f = lambda t: t**2
    xx = transpose([[1]*10, x1, x2, f(x1), f(x2)])

    model = linear_model.LinearRegression()
    model.fit(xx, y)

    print(model.coef_)
    print(model.intercept_)




if __name__ == '__main__':

    test13()