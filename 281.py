'''
Write a python function to check if the elements of a given list are unique or not.
'''

def all_unique(lst):
    return len(lst) == len(set(lst))


assert all_unique([1,2,3]) == True
assert all_unique([1,2,1,2]) == False
assert all_unique([1,2,3,4,5]) == True
