'''
Write a function to check whether the given month name contains 28 days or not.
'''

def check_monthnum(month):
    return month in ['February']


assert check_monthnum("February")==True
assert check_monthnum("January")==False
assert check_monthnum("March")==False
