'''
Write a python function to check whether the triangle is valid or not if 3 points are given.
'''

def check_Triangle(x1,y1,x2,y2,x3,y3):
    if x1 == x2 == x3 or y1 == y2 == y3:
        return 'No'
    return 'Yes'


assert check_Triangle(1,5,2,5,4,6) == 'Yes'
assert check_Triangle(1,1,1,4,1,5) == 'No'
assert check_Triangle(1,1,1,1,1,1) == 'No'
