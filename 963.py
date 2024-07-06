'''
Write a function to calculate the discriminant value.
'''

def discriminant_value(a,b,c):
    d = b**2-4*a*c
    if d > 0:
        return ("Two solutions",d)
    elif d == 0:
        return ("one solution",d)
    else:
        return ("no real solution",d)
    

assert discriminant_value(4,8,2)==("Two solutions",32)
assert discriminant_value(5,7,9)==("no real solution",-131)
assert discriminant_value(0,0,9)==("one solution",0)
