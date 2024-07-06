'''
Write a function to find the maximum value in a given heterogeneous list.
'''

def max_val(lst):
    return max([i for i in lst if type(i)==int])


assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
assert max_val(['Python', 15, 20, 25])==25
assert max_val(['Python', 30, 20, 40, 50, 'version'])==50
