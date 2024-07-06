'''
Write a python function to shift first element to the end of given list.
'''

def move_last(lst):
    return lst[1:] + [lst[0]]


assert move_last([1,2,3,4]) == [2,3,4,1]
assert move_last([2,3,4,1,5,0]) == [3,4,1,5,0,2]
assert move_last([5,4,3,2,1]) == [4,3,2,1,5]
