# 从无序序列头部开始，进行两两比较，根据大小交换位置，直到最后将最大（小）的数据元素交换到了无序队列的队尾


def bubble_sort(arr):
    m = len(arr)
    for i in range(m):
        for j in range(m - 1 - i):  # 每循环一次， 内循环次数减1（将最大的数移到末尾）
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


A = [2, 1, 34, 23, 13, 9, 4, 8, 5, 13, 40, 21, 35]
arr = bubble_sort(A)
print(arr)
