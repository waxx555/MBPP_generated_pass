'''
Write a python function to check whether the triangle is valid or not if sides are given.
'''

def check_Validity(a,b,c):
    return a+b>c and b+c>a and a+c>b


assert check_Validity(1,2,3) == False
assert check_Validity(2,3,5) == False
assert check_Validity(7,10,5) == True
