# 从队列里找出最大（最小）的数排在首尾，然后依次排列


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


A = [2, 1, 34, 23, 13, 9, 4, 8, 5, 13, 40, 21, 35]
arr = selection_sort(A)
print(arr)