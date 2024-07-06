'''
Write a python function to find the frequency of the largest value in a given array.
'''

def frequency_Of_Largest(n,arr):
    return arr.count(max(arr))


assert frequency_Of_Largest(5,[1,2,3,4,4]) == 2
assert frequency_Of_Largest(3,[5,6,5]) == 1
assert frequency_Of_Largest(4,[2,7,7,7]) == 3
