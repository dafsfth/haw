#include <stdio.h>

void bubble_sort(int *p, int len)
{
    int i, j, c;
    for (i = 0; i < len - 1; i++)
    {
        for (j = i + 1; j < len; j++)
        {
            if (p[i] > p[j])
            {
                c = p[i], p[i] = p[j], p[j] = c;
            }
        }
    }
}

void main()
{
    int arr[10] = {3, 2, 14, 23, 10, 12, 32, 8, 43, 34};
    bubble_sort(arr, 10);
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }
}