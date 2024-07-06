'''
Write a function to sort a list of elements using radix sort.
'''

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


assert radix_sort([15, 79, 25, 68, 37]) == [15, 25, 37, 68, 79]
assert radix_sort([9, 11, 8, 7, 3, 2]) == [2, 3, 7, 8, 9, 11]
assert radix_sort([36, 12, 24, 26, 29]) == [12, 24, 26, 29, 36]
