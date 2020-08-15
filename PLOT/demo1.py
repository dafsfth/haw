from pylab import *
# import numpy as np
# import matplotlib.pyplot as plt


def test1():

    figure(figsize=(8, 6))
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)

    subplot(122)
    # xlim(-4.0, 4.0)
    xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])
    plt.plot(x, s, color='green', linewidth='1.0', linestyle='-')

    subplot(121)
    plt.plot(x, c)

    plt.show()


# 将坐标轴移向中心
def test2():
    """
    将坐标轴改为中心
    :return:
    """
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))   # (0, 0)

    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = cos(x), sin(x)

    plot(x, c, color='red', linewidth='2.0', linestyle='-', label='cosine')
    plot(x, s, color='green', linewidth='2.0', linestyle='-', label='sine')

    legend(loc='upper left')

    xlim(min(x) * 1.1, max(c) * 1.1)
    xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-np.pi$', r'$-np.pi/2$', r'$0$', r'$np.pi/2$', r'$np.pi$'])

    yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])

    show()


# 标记
def test3():
    ax = gca()

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    x = linspace(-pi, pi, 256, endpoint=True)
    s, c = sin(x), cos(x)

    plot(x, c, color='red', linewidth='2.0', linestyle='-', label='cosine')
    plot(x, s, color='blue', linewidth='2.0', linestyle='-', label='sine')

    legend(loc='upper left')

    xticks([-pi, -pi/2, 0, pi/2, pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    yticks([-1, 1], [r'$-1$', r'$1$'])

    t = 2 * pi / 3
    plot([t, t], [0, cos(t)], color='red', linewidth='1.0', linestyle='--')
    scatter(t, cos(t), 50, color='green')
    annotate(r'$\cos(\frac{2\pi}{3})=-\frac{{1}}{2}$',
             xy=(t, cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plot([t, t], [0, sin(t)], color='green', linewidth='1.0', linestyle='--')
    scatter(t, sin(t), 50, color='blue')
    annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, sin(t)),
             # xycoords='data',
             xytext=(10, 30),
             textcoords='offset points',  # 控制文本位置
             fontsize=16,
             arrowprops=dict(arrowstyle="->"
                             # connectionstyle="arc3, rad=.2"
                             ))
    # 将被遮挡的刻度显示出来
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.85))

    show()


# 子图
def test4():
    import matplotlib.gridspec as g
    G = g.GridSpec(3, 3)

    subplot(G[0, :])
    xticks([]), yticks([])
    text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=.5)

    subplot(G[1, : -1])
    xticks([]), yticks([])
    text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24, alpha=.5)

    subplot(G[1:, -1])
    xticks([]), yticks([])
    text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24, alpha=.5)

    subplot(G[2, 0])
    xticks([]), yticks([])
    text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=.5)

    subplot(G[2, 1])
    xticks([]), yticks([])
    text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=.5)

    show()


# 填充
def test5():
    x = np.linspace(-pi, pi, 256, endpoint=True)
    y = sin(2 * x)

    plot(x, y+1, color='blue', alpha=1.0)
    fill_between(x, 1, y+1, color='blue', alpha=.25)

    plot(x, y-1, color='red', alpha=1.0)
    fill_between(x, -1, y-1, (y-1) > -1, color='blue', alpha=.25)
    fill_between(x, -1, y-1, (y-1) < -1, color='red', alpha=.25)
    #            x   y1   y2    where

    xlim(-pi, pi), xticks([])
    ylim(-2.5, 2.5), yticks([])

    show()


# 散点图
def test6():
    n = 1024
    x = np.random.normal(0, 10, n)
    y = np.random.normal(0, 10, n)
    T = arctan(y, x)

    subplot(121)
    scatter(x, y, s=75, c=T, alpha=.5)
    xticks([]), yticks([])

    subplot(122)
    scatter(x, y)
    xticks([]), yticks([])

    show()


# 条形图
def test7():
    n = 12
    x = arange(n)

    # y1 = np.random.uniform(0.5, 1.0, n)
    y1 = multiply(1 - x / float(n), np.random.uniform(0.5, 1.0, n))
    # y2 = np.random.uniform(0.5, 1.0, n)
    y2 = multiply(1 - x / float(n), np.random.uniform(0.5, 1.0, n))

    bar(x, +y1, facecolor='blue', edgecolor='white')
    bar(x, -y2, facecolor='red', edgecolor='white')

    # for x1, y in zip(x, y1):
    #     #     text(x1+0.4, y+0.05, '%.2f' %y, ha='center', va='bottom')
    #     #
    #     # for x1, y in zip(x, y2):
    #     #     text(x+0.4, -y-0.05, '%.2f' %y, ha='center', va='top')

    for i in range(n):
        text(x[i] + 0.04, y1[i] + 0.05, '%.2f' % y1[i], ha='center', va='bottom')
        text(x[i] + 0.04, -y2[i] - 0.05, '%.2f' % y2[i], ha='center', va='top')

    xticks([]), yticks([])
    ylim(-1.25, 1.5)

    show()


def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)


# 等高线
def test8():
    n = 256
    x = linspace(-3, 3, n)
    y = linspace(-3, 3, n)

    X, Y = meshgrid(x, y)

    contourf(X, Y, f(X, Y), 8, alpha=.8, camp=cm.ma)
    C = contour(X, Y, f(X, Y), 8, color='black', linewidth=.5)
    clabel(C, inline=1, fontsize=10)

    xticks([]), yticks([])

    show()


def test9():
    x = linspace(-10, 10, 100)
    y = linspace(-10, 10, 100)

    X, Y = meshgrid(x, y)  # 将x, y变为网格数据
    Z = X**3 - X**2 + Y**3 - Y**2

    subplot(131)
    contourf(X, Y, Z, 6, cmap='hot')  # f填充颜色, 6层颜色，cmap：颜色格式，  hot表示热温图
    contour(X, Y, Z)  # 画等高线

    subplot(132)
    C = contour(X, Y, Z, [20, 60])
    clabel(C, fontsize=10, colors=('b', 'r'), fmt='%.2f')  # 标注

    subplot(133)
    cf = contourf(X, Y, Z, cmap='hot')
    c = contour(X, Y, Z, 8, colors='k')
    clabel(c, fontsize=10, colors='blue')
    xticks([]), yticks([])
    colorbar(cf)  # 颜色条

    show()


# 灰度图
def test10():
    n = 100
    x = linspace(-3, 3, n)
    y = linspace(-3, 3, n)
    X, Y = meshgrid(x, y)
    Z = f(X, Y)

    imshow(Z, interpolation='bicubic', cmap='bone', origin='lower')  # interpolation : 插入文字,  bicubic: 双立方插值
    colorbar(shrink=.92)

    xticks([]), yticks([])

    show()


# 饼状图
def test11():
    n = 20
    Z = ones(n)
    Z[-1] *= 2

    pie(Z, explode=Z*.05, colors=['%f' % (i / float(n)) for i in range(n)],
        wedgeprops={"linewidth": 1, "edgecolor": "black"})

    xticks([]), yticks([])

    show()


"""
pie(x,              # x (每一块)的比例，如果sum(x) > 1会使用sum(x)归一化
    explode=None,   # explode (每一块)离开中心距离
    labels=None,    # labels  (每一块)饼图外侧显示的说明文字
    colors=('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'),
    autopct=None,   # autopct 控制饼图内百分比设置,可以使用format字符串或者format function
                            '%1.1f'指小数点前后位数(没有用空格补齐)
    pctdistance=0.6,    # pctdistance 类似于labeldistance,指定autopct的位置刻度
    shadow=False,   # shadow  是否阴影
    labeldistance=1.1,  # labeldistance label绘制位置,相对于半径的比例, 如<1则绘制在饼图内侧
    startangle=None, # startangle  起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起
    radius=None,    # radius  控制饼图半径
    counterclock=True, wedgeprops=None, textprops=None,
    center = (0, 0), frame = False )
"""


def test12():
    labels = ['China', 'Swiss', 'USA', 'UK', 'Laos', 'Spain']
    X = [222, 42, 455, 664, 454, 334]
    pie(X, labels=labels, autopct='%1.2f%%')
    title('pie chart')

    show()


def test13():
    expl = [0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0]
    colors = ["blue", "red", "coral", "green", "yellow", "orange"]
    quants = [15094025, 11299967, 4457784, 4440376, 3099080, 2383402, 2293954, 2260803, 2217900, 1846950.0]
    labels = ['USA', 'China', 'India', 'Japan', 'Germany', 'Russia', 'Brazil', 'UK', 'France', 'Italy']
    title('Top 10 GDP Countries', bbox={'facecolor': '0.8', 'pad': 5})
    pie(quants, explode=expl, labels=labels, colors=colors, autopct='%1.2f%%', pctdistance=0.8, shadow=True)

    show()


# 量场图
def test14():
    n = 8
    x = y = [i for i in range(n)]
    X, Y = meshgrid(x, y)
    T = arctan2(Y - n / 2.0, X - n / 2.0)
    R = 10 + sqrt((Y-n/2.0)**2+(X-n/2.0)**2)
    U, V = R * cos(T), R * sin(T)

    quiver(X, Y, U, V, R, alpha=.5)
    quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)

    xticks([]), yticks([])

    show()


# polar
def test16():

    axes(polar=True)

    n = 20
    theta = arange(0, 2*pi, 2*pi / n)
    radi = 10 * np.random.rand(n)
    width = pi / 4 * np.random.rand(n)
    bars = bar(theta, radi, width=width, bottom=0)

    show()


# 3d
def test15():
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = Axes3D(fig)
    
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='hot')
    ax.set_zlim(-2, 2)

    show()


test15()




