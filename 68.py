'''
Write a python function to check whether the given array is monotonic or not.
'''

def is_Monotonic(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))


assert is_Monotonic([6, 5, 4, 4]) == True
assert is_Monotonic([1, 2, 2, 3]) == True
assert is_Monotonic([1, 3, 2]) == False
