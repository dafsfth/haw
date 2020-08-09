#            堆排序

#  1.构造初始堆, 将给定无序序列构造成一个大顶堆（一般升序采用大顶堆，降序采用小顶堆)。


def max_heap(A, i):
    r = 2 * (i + 1)
    l = 2 * (i+1) - 1
    if (l <= length) and (A[i] < A[l]):
        largest = l
    else:
        largest = i
    if (r <= length) and (A[largest] < A[r]):
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heap(A, largest)


def build_max_heap(A):
    # length = len(A) - 1
    for i in range(int(length/2), -1, -1):
        max_heap(A, i)


#  2.将堆顶元素与末尾元素进行交换，使末尾元素最大。然后继续调整堆，再将堆顶元素与末尾元素交换，得到第二大元素。如此反复进行交换、重建、交换
def heap_sort(A):
    global length
    length = len(A) - 1
    build_max_heap(A)
    for i in range(length, 0, -1):
        A[0], A[i] = A[i], A[0]
        length -= 1
        max_heap(A, 0)


A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
if __name__ == "__main__":
    heap_sort(A)
    print(A)