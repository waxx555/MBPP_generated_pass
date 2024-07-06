'''
Write a function to find the peak element in the given array.
'''

def find_peak(arr, n):
    if n == 1:
        return 0
    if arr[0] >= arr[1]:
        return 0
    if arr[n-1] >= arr[n-2]:
        return n-1
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i
    return -1


assert find_peak([1, 3, 20, 4, 1, 0], 6) == 2
assert find_peak([2, 3, 4, 5, 6], 5) == 4
assert find_peak([8, 9, 11, 12, 14, 15], 6) == 5 
