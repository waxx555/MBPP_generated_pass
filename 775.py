'''
Write a python function to check whether every odd index contains odd numbers of a given list.
'''

def odd_position(lst):
    return all([i%2!=0 for i in lst[1::2]])



assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([4,1,2]) == True
assert odd_position([1,2,3]) == False
