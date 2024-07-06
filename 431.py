'''
Write a function that takes two lists and returns true if they have at least one common element.
'''

def common_element(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True
    return None


assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
assert common_element([1,2,3,4,5], [6,7,8,9])==None
assert common_element(['a','b','c'], ['d','b','e'])==True
