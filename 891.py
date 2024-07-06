'''
Write a python function to check whether the given two numbers have same number of digits or not.
'''

def same_Length(a,b):
    return len(str(a)) == len(str(b))


assert same_Length(12,1) == False
assert same_Length(2,2) == True
assert same_Length(10,20) == True
