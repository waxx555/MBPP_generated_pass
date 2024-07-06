'''
Write a python function to shift last element to first position in the given list.
'''

def move_first(lst):
    return [lst[-1]] + lst[:-1]


assert move_first([1,2,3,4]) == [4,1,2,3]
assert move_first([0,1,2,3]) == [3,0,1,2]
assert move_first([9,8,7,1]) == [1,9,8,7]
