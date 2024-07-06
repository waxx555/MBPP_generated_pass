'''
Write a function to sort the given array by using shell sort.
'''

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]
