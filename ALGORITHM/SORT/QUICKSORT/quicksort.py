import random

A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]


def partition(list1, p, r):
    x = list1[r]
    # x = random.choice(list1)
    i = p - 1
    for j in range(p, r):
        if list1[j] <= x:
            i += 1
            list1[i], list1[j] = list1[j], list1[i]
    list1[i+1], list1[r] = x, list1[i+1]
    return i+1


def quick_sort(list1, p, r):
    if p < r:
        q = partition(list1, p, r)
        quick_sort(list1, p, q)
        quick_sort(list1, q+1, r)


# 快速排序的随机版本
def rand_partition(list1, p, r):
    i = random.randint(p, r)
    # print(i)
    list1[i], list1[r] = list1[r], list1[i]
    return partition(list1, p, r)


def rand_quick_sort(list1, p, r):
    if p < r:
        q = rand_partition(list1, p, r)
        rand_quick_sort(list1, p, q)
        rand_quick_sort(list1, q+1, r)


# quick_sort(A, 0, len(A))
rand_quick_sort(A, 0, len(A)-1)
print(A)

