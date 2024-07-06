'''
Write a function to print check if the triangle is equilateral or not.
'''

def check_equilateral(a,b,c):
    if a==b==c:
        return True
    else:
        return False
    

assert check_equilateral(6,8,12)==False 
assert check_equilateral(6,6,12)==False
assert check_equilateral(6,6,6)==True
