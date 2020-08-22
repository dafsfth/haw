#  希尔排序： 也称递减增量排序算法， 是插入排序的一种更高效的改进版本
# 1.选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
# 每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。
# 仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
import math


Arr = [2, 1, 34, 23, 13, 9, 4, 8, 5, 13, 40, 21, 35]


def shell_sort1(arr):
    gap = 1
    while gap <= len(arr) / 3:
        gap = gap * 3 + 1  # 构造初始增量
    while gap > 0:
        for i in range(gap, len(arr)):   # 对相隔gap的两个数进行比较
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap            # 如果换的数小于之前的数， 进行交换
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
    return arr


arr = shell_sort1(Arr)
print(arr)

