'''
Write a function to find the index of the first occurrence of a given number in a sorted array.
'''

def find_first_occurrence(arr, n):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == n and (mid == 0 or arr[mid-1] != n):
            return mid
        elif arr[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1


assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4
