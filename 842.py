'''
Write a function to find the number which occurs for odd number of times in the given array.
'''

def get_odd_occurence(arr, n):
    res = 0
    for i in range(n):
        res = res ^ arr[i]
    return res


assert get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5
assert get_odd_occurence([1, 2, 3, 2, 3, 1, 3], 7) == 3
assert get_odd_occurence([5, 7, 2, 7, 5, 2, 5], 7) == 5
