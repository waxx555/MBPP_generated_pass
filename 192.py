'''
Write a python function to check whether a string has atleast one letter and one number.
'''

def check_String(s):
    return any(i.isalpha() for i in s) and any(i.isdigit() for i in s)


assert check_String('thishasboth29') == True
assert check_String('python') == False
assert check_String ('string') == False
