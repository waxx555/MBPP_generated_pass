'''
Write a python function to count negative numbers in a list.
'''

def neg_count(lst):
    return len([i for i in lst if i < 0])


assert neg_count([-1,-2,3,-4,-5]) == 4
assert neg_count([1,2,3]) == 0
assert neg_count([1,2,-3,-10,20]) == 2
