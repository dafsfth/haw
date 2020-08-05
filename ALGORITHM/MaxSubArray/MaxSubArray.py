# ------------------------------最大子数组的3中解法--------------------------------------
import numpy as np


a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


# 1.暴力算法O(n**2)


def test1():
    sum1 = -np.inf
    for i in range(len(a)):
        cur_sum = 0
        for j in a[i: ]:
            cur_sum += j
            if cur_sum > sum1:
                sum1 = cur_sum
    return sum1


# 2. 分治算法O(nlgn)

def cross(mid):
    left_sum = -np.inf
    cur_sum = 0
    for i in a[mid::-1]:
        cur_sum += i
        if cur_sum > left_sum:
            left_sum = cur_sum

    right_sum = -np.inf
    cur_sum = 0
    for j in a[mid+1:]:
        cur_sum += j
        if cur_sum > right_sum:
            right_sum = cur_sum

    return left_sum + right_sum


def left_right(low, high):
    if low == high:
        return a[low]

    mid = int((low + high) / 2)

    big_left = left_right(low, mid)
    big_right = left_right(mid + 1, high)
    big_cross = cross(mid)

    biggest = max(big_left, big_right, big_cross)
    return biggest


def test2():
    big = left_right(0, 15)
    print(big)
# test2()
# 线性时间算法  O(n)：


def test3():
    cur_sum = 0
    max_sum = 0
    for i in a:
        cur_sum += i
        if cur_sum > max_sum:
            max_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return max_sum

# sum = test3()
# print(sum)

