'''
Write a python function to remove negative numbers from a list.
'''

def remove_negs(lst):
    return [i for i in lst if i>=0]


assert remove_negs([1,-2,3,-4]) == [1,3]
assert remove_negs([1,2,3,-4]) == [1,2,3]
assert remove_negs([4,5,-6,7,-8]) == [4,5,7]
