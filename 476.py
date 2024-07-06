'''
Write a python function to find the sum of the largest and smallest value in a given array.
'''

def big_sum(arr):
    return max(arr)+min(arr)


assert big_sum([1,2,3]) == 4
assert big_sum([-1,2,3,4]) == 3
assert big_sum([2,3,6]) == 8
