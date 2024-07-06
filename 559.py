'''
Write a function to find the largest sum of contiguous subarray in the given array.
'''

def max_sub_array_sum(arr, n):
    max_so_far = arr[0]
    curr_max = arr[0]
    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far


assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10
