'''
Write a function to find the index of the last occurrence of a given number in a sorted array.
'''

def find_last_occurrence(arr, n):
    return len(arr) - arr[::-1].index(n) - 1


assert find_last_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
assert find_last_occurrence([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9) == 9
assert find_last_occurrence([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6) == 6
