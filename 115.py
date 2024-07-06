'''
Write a function to check whether all dictionaries in a list are empty or not.
'''

def empty_dit(lst):
    for i in lst:
        if i:
            return False
    return True


assert empty_dit([{},{},{}])==True
assert empty_dit([{1,2},{},{}])==False
assert empty_dit({})==True
