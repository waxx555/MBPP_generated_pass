'''
Write a function to check whether the given month number contains 31 days or not.
'''

def check_monthnumb_number(n):
    if n in [1,3,5,7,8,10,12]:
        return True
    return False


assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==False
assert check_monthnumb_number(6)==False
