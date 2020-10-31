#include <stdio.h>

void swap(int *a, int *b)
{
    int temp;
    temp = *a, *a = *b, *b = temp;
}

void selection_sort(int arr[], int len)
{
    int i, j;
    for (i = 0; i < len - 1; i++)
    {
        int min = i;
        for (j = i + 1; j < len; j++)
        {
            if (arr[min] > arr[j])
            {
                min = j;
            }
        }
        swap(&arr[min], &arr[i]);
    }
}

int main()
{
    int arr[10] = {3, 2, 14, 23, 10, 12, 32, 8, 43, 34};
    selection_sort(arr, 10);
    for (int i = 0; i < 10; i++)
    {
        printf("%d  ", arr[i]);
    }
}