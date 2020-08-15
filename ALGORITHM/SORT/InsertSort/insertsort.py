def insert_sort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]  # 后移
            j -= 1
        A[j+1] = x  # 补


Al = [10, 3, 2, 14, 23, 34, 9, 5, 7, 9, 3, 10]
insert_sort(Al)
print(Al)


def sort(A):
    max_list = []
    for i in range(len(A)):
        x = A.pop(A.index(max(A)))
        max_list.append(x)
    return max_list


# a = sort(Al)
# print(a)