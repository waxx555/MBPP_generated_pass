'''
Write a python function to find the first element occurring k times in a given array.
'''

def first_Element(arr,n,k):
    for i in arr:
        if arr.count(i) == k:
            return i
    return -1


assert first_Element([0,1,2,3,4,5],6,1) == 0
assert first_Element([1,2,1,3,4],5,2) == 1
assert first_Element([2,3,4,3,5,7,1,2,3,5],10,2) == 2
