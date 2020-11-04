import matplotlib.animation as an
from pylab import *

"""
FuncAnimation
通过反复调用函数*func*生成动画。

参数：
fig
func  每帧调用的函数
"""
# start = [1, 0.18, 0.63, 0.29, 0.03, 0.24, 0.86, 0.07, 0.58, 0]
#
# metric = [[0.03, 0.86, 0.65, 0.34, 0.34, 0.02, 0.22, 0.74, 0.66, 0.65],
#             [0.43, 0.18, 0.63, 0.29, 0.03, 0.24, 0.86, 0.07, 0.58, 0.55],
#             [0.66, 0.75, 0.01, 0.94, 0.72, 0.77, 0.20, 0.66, 0.81, 0.52]]
#
# fig = figure()
# windows = fig.add_subplot(111)
# line, = windows.plot(start)
#
#
# def update(data):
#     line.set_ydata(data)
#     return line,
#
#
# ani = an.FuncAnimation(fig, update, metric, interval=2 * 1000)  # 每次从metric中取一行数据作为参数送入update中
# show()
#
#


# ==================================================================================
# fig = figure()
# ax = fig.add_subplot(111)
# line, = ax.plot(np.random.rand(10))
#
#
# # 变换函数
# def update(data):
#     line.set_ydata(data)
#     return line,
#
#
# # 生成数据
# def gen_data():
#     while True:
#         yield np.random.rand(10)
#
#
# ani = an.FuncAnimation(fig, update, gen_data, interval=2*1000)
# show()
# ===================================================================================


# =====================================================================================================
# fig = figure()
# ax = fig.add_subplot(111)
# line, = ax.plot([], [], lw=2)
#
#
# # plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,
#
#
# # i is framenumber
# def animate(i):
#     x = linspace(0, 2, 1000)
#     y = sin(2 * pi * (x - 0.01 * i))
#     line.set_data(x, y)
#     return line,
#
#
# ani = an.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
# # blit = true 表示重新画改变的部分
# show()
#

# =====================================================================================================


# ==============================================================================================
# 每次产生一个新的坐标
# def data_gen():
#     t = data_gen.t
#     cnt = 0
#     while cnt < 1000:
#         cnt += 1
#         t += 0.05
#         yield t, sin(2 * pi * t) * exp(-t / 10)
#
#
# data_gen.t = 0
#
# fig, ax = subplots()
# line, = ax.plot([], [], lw=2)
#
# ax.set_ylim(-1.1, 1.1)
# ax.set_xlim(0, 5)
# ax.grid()
#
# x_data , y_data = [], []
#
#
# def run(data):
#     t, y =data
#     x_data.append(t)
#     y_data.append(y)
#
#     xmin, xmax = ax.get_xlim()
#
#     # 扩展x轴
#     if t > xmax:
#         ax.set_xlim(xmin, 2*xmax)
#         ax.figure.canvas.draw()
#
#     line.set_data(x_data, y_data)
#
#     return line,
#
#
# # 表示图形只更新需要绘制的元素
# ani = an.FuncAnimation(fig, run, data_gen, blit=True, interval=10, repeat=False)
#
# show()

# ==============================================================================================

# =======================================================================
def update_line(num, data, line):
    line.set_data(data[..., num])
    return line,


fig = figure()
data = np.random.rand(2, 15)
l, = plot([], [], 'r-')
xlim(0, 1), ylim(0, 1)

line_ani = an.FuncAnimation(fig, update_line, 15, frames=(data, 1), interval=50, )

show()

# ========================================================================


