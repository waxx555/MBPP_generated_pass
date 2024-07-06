'''
Write a function to check if a string represents an integer or not.
'''

def check_integer(string):
    try:
        int(string)
        return True
    except:
        return False
    

assert check_integer("python")==False
assert check_integer("1")==True
assert check_integer("12345")==True
