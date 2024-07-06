'''
Write a function to find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times.
'''
def max_sub_array_sum(arr, n):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_sub_array_sum_repeated(arr, n, k):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if k == 1:
        return max_sub_array_sum(arr, n)
    arr_sum = sum(arr)
    if arr_sum < 0:
        return max_sub_array_sum(arr, n)
    arr = arr + arr
    return max_sub_array_sum(arr, 2*n)


assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1
