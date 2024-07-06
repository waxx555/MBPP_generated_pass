'''
Write a function to check if all the elements in tuple have same data type or not.
'''

def check_type(t):
    return len(set(map(type, t))) == 1


assert check_type((5, 6, 7, 3, 5, 6) ) == True
assert check_type((1, 2, "4") ) == False
assert check_type((3, 2, 1, 4, 5) ) == True
