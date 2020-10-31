#include <stdio.h>

void insert_sort(int arr[], int len)
{
    int i, j, tmp;
    for (i = 1; i < len; i++)
    {
        tmp = arr[i];
        for (j = i; j > 0 && arr[j - 1] > tmp; j--)
        {
            arr[j] = arr[j - 1];
        }
        arr[j] = tmp;
    }
}

void main()
{
    int a[10] = {3, 2, 14, 23, 10, 12, 32, 8, 43, 34};
    int len = (int)sizeof(a) / sizeof(*a);
    insert_sort(a, len);
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", a[i]);
    }
}