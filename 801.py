'''
Write a python function to count the number of equal numbers from three given integers.
'''

def test_three_equal(x, y, z):
    if x == y == z:
        return 3
    elif x == y or y == z or z == x:
        return 2
    else:
        return 0
    

assert test_three_equal(1,1,1) == 3
assert test_three_equal(-1,-2,-3) == 0
assert test_three_equal(1,2,2) == 2
