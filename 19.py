'''
Write a function to find whether a given array of integers contains any duplicate element.
'''

def test_duplicate(arr):
    return len(arr)!=len(set(arr))




assert test_duplicate(([1,2,3,4,5]))==False
assert test_duplicate(([1,2,3,4, 4]))==True
assert test_duplicate([1,1,2,2,3,3,4,4,5])==True
