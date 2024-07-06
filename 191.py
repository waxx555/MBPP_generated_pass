'''
Write a function to check whether the given month name contains 30 days or not.
'''

def check_monthnumber(month):
    if month in ["April","June","September","November"]:
        return True
    else:
        return False
    

assert check_monthnumber("February")==False
assert check_monthnumber("June")==True
assert check_monthnumber("April")==True
