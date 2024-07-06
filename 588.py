'''
Write a python function to find the difference between largest and smallest value in a given array.
'''

def big_diff(arr):
    return max(arr) - min(arr)


assert big_diff([1,2,3,4]) == 3
assert big_diff([4,5,12]) == 8
assert big_diff([9,2,3]) == 7
