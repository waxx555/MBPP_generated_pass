'''
Write a function to check if the given array represents min heap or not.
'''

def check_min_heap(arr, i):
    if i >= len(arr):
        return True
    if 2*i+1 < len(arr) and arr[i] > arr[2*i+1]:
        return False
    if 2*i+2 < len(arr) and arr[i] > arr[2*i+2]:
        return False
    return check_min_heap(arr, 2*i+1) and check_min_heap(arr, 2*i+2)


assert check_min_heap([1, 2, 3, 4, 5, 6], 0) == True
assert check_min_heap([2, 3, 4, 5, 10, 15], 0) == True
assert check_min_heap([2, 10, 4, 5, 3, 15], 0) == False
