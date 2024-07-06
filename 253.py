'''
Write a python function to count integers from a given list.
'''

def count_integer(lst):
    return len([i for i in lst if type(i) == int])


assert count_integer([1,2,'abc',1.2]) == 2
assert count_integer([1,2,3]) == 3
assert count_integer([1,1.2,4,5.1]) == 2
