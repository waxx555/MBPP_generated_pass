'''
Write a function to find whether an array is subset of another array.
'''

def is_subset(arr1, n, arr2, m):
    freq = {}
    for i in arr1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in arr2:
        if i not in freq:
            return False
        if freq[i] == 0:
            return False
        freq[i] -= 1
    return True


assert is_subset([11, 1, 13, 21, 3, 7], 6, [11, 3, 7, 1], 4) == True
assert is_subset([1, 2, 3, 4, 5, 6], 6, [1, 2, 4], 3) == True
assert is_subset([10, 5, 2, 23, 19], 5, [19, 5, 3], 3) == False
