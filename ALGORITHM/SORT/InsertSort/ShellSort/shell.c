#include <stdio.h>

void shell_sort(int arr[], int len)
{
    int grap, i, j, tmp;
    for (grap >> 1; grap > 0; grap = grap >> 1)
    {
        for (i = grap; i < len; i++)
        {
            tmp = arr[i];
            for (j = i - grap; j >= 0 && arr[j] > tmp; j -= grap)
            {
                arr[j + grap] = arr[j];
            }
            arr[j + grap] = tmp;
        }
    }
}

void main()
{
    int arr[10] = {3, 2, 14, 23, 10, 12, 32, 8, 43, 34};
    shell_sort(arr, 10);
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }
}