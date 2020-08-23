# 计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
# 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
"""
找出待排序的数组中最大和最小的元素；
统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。
"""


def counting_sort(arr, max_value):
    bucket_len = max_value + 1
    bucket = [0] * bucket_len
    sort_index = 0
    for i in range(len(arr)):   # 计数
        # if not bucket[arr[i]]:
        #     bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucket_len):  # 排序
        while bucket[j] > 0:
            arr[sort_index] = j
            sort_index += 1
            bucket[j] -= 1

    return arr


A = [2, 1, 34, 23, 13, 9, 4, 8, 5, 13, 40, 21, 35]
arr = counting_sort(A, max(A))
print(arr)