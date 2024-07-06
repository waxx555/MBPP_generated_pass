'''
Write a function to check if the given tuple contains all valid values or not.
'''

def check_valid(t):
    return all(t)


assert check_valid((True, True, True, True) ) == True
assert check_valid((True, False, True, True) ) == False
assert check_valid((True, True, True, True) ) == True
