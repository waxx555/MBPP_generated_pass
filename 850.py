'''
Write a function to check if a triangle of positive area is possible with the given angles.
'''

def is_triangleexists(a,b,c):
    return a+b+c==180 and a>0 and b>0 and c>0


assert is_triangleexists(50,60,70)==True
assert is_triangleexists(90,45,45)==True
assert is_triangleexists(150,30,70)==False
