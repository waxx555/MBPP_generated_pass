'''
Write a function to find the equilibrium index of the given array.
'''

def equilibrium_index(arr):
    n = len(arr)
    left_sum = 0
    right_sum = sum(arr)
    for i in range(n):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1


assert equilibrium_index([1, 2, 3, 4, 1, 2, 3]) == 3
assert equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3
assert equilibrium_index([1, 2, 3]) == -1
