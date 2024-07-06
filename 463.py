'''
Write a function to find the maximum product subarray of the given array.
'''

def max_subarray_product(arr):
    max_ending_here = min_ending_here = max_so_far = arr[0]
    for i in range(1, len(arr)):
        temp = max_ending_here
        max_ending_here = max(arr[i], arr[i] * max_ending_here, arr[i] * min_ending_here)
        min_ending_here = min(arr[i], arr[i] * temp, arr[i] * min_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
assert max_subarray_product([6, -3, -10, 0, 2]) == 180 
assert max_subarray_product([-2, -40, 0, -2, -3]) == 80
