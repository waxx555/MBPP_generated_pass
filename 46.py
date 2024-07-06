'''
Write a python function to determine whether all the numbers are different from each other are not.
'''

def test_distinct(data):
    return len(data) == len(set(data))



assert test_distinct([1,5,7,9]) == True
assert test_distinct([2,4,5,5,7,9]) == False
assert test_distinct([1,2,3]) == True
