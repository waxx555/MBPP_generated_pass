'''
Write a python function to count positive numbers in a list.
'''

def pos_count(lst):
    return len(list(filter(lambda x: x>0,lst)))
               

assert pos_count([1,-2,3,-4]) == 2
assert pos_count([3,4,5,-1]) == 3
assert pos_count([1,2,3,4]) == 4
