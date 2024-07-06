'''
Write a function to remove an empty tuple from a list of tuples.
'''

def remove_empty(lst):
    return [i for i in lst if i]


assert remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])==[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  
assert remove_empty([(), (), ('',), ("python"), ("program")])==[('',), ("python"), ("program")]  
assert remove_empty([(), (), ('',), ("java")])==[('',),("java") ]  
