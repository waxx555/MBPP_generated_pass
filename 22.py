'''
Write a function to find the first duplicate element in a given array of integers.
'''

def find_first_duplicate(arr):
    for i in range(len(arr)):
        if arr[i] in arr[i+1:]:
            return arr[i]
    return -1



assert find_first_duplicate(([1, 2, 3, 4, 4, 5]))==4
assert find_first_duplicate([1, 2, 3, 4])==-1
assert find_first_duplicate([1, 1, 2, 3, 3, 2, 2])==1
