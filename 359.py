'''
Write a python function to check whether one root of the quadratic equation is twice of the other or not.
'''

def Check_Solution(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        return "No"
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    if x1 == 2*x2 or x2 == 2*x1:
        return "Yes"
    else:
        return "No"
    

assert Check_Solution(1,3,2) == "Yes"
assert Check_Solution(1,2,3) == "No"
assert Check_Solution(1,-5,6) == "No"
