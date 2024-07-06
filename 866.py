'''
Write a function to check whether the given month name contains 31 days or not.
'''

def check_monthnumb(month):
    if month in ["January", "March", "May", "July", "August", "October", "December"]:
        return True
    return False


assert check_monthnumb("February")==False
assert check_monthnumb("January")==True
assert check_monthnumb("March")==True
