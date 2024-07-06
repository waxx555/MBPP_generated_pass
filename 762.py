'''
Write a function to check whether the given month number contains 30 days or not.
'''

def check_monthnumber_number(n):
    if n in [4,6,9,11]:
        return True
    return False


assert check_monthnumber_number(6)==True
assert check_monthnumber_number(2)==False
assert check_monthnumber_number(12)==False
