from cvxopt import solvers, matrix


# matrix里区分int和double，所以数字后面都需要加小数点
# cvxopt.matrix与numpy.matrix的排列顺序不同，其中cvxopt.matrix是列优先，numpy.matrix是行优先
"""
二次规划
cvxopt.slovers.qp   
================================

参数：
Output arguments:

"""


def test1():

    P = matrix([[1.0, 0.0], [0.0, 0.0]])
    q = matrix([3.0, 4.0])  # 1 x 2
    G = matrix([[-1.0, 0.0, -1.0, 2.0, 3.0], [0.0, -1.0, 3.0, 5.0, 4.0]])  # 2x5
    h = matrix([0.0, 0.0, -15.0, 100.0, 80.0])  # 1 x 5

    sol = solvers.qp(P, q, G, h)   # 调用优化函数solvers.qp求解
    print(sol['x'])


# min f(x1, x2) = -2x1 - 6x2 + x1^2 + 2x2^2 - 2x1x2
def test2():
    P = matrix([[1.0, -1.0], [-1.0, 2.0]])
    q = matrix([-2.0, -6.0])
    G = matrix([[1.0, -1.0], [1.0, 2.0]])
    h = matrix([2.0, 2.0])

    result = solvers.qp(P, q, G=G, h=h)
    print('x', result['x'])
    print('y', result['y'])
    print('s', result['s'])
    print('z', result['z'])

    # print('p', P)
    # print('q', q)
    # print('G', G)
    # print('h', h)



if __name__ == '__main__':
    test2()