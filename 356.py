'''
Write a function to find the third angle of a triangle using two angles.
'''

def find_angle(angle1, angle2):
    return 180-angle1-angle2


assert find_angle(47,89)==44
assert find_angle(45,95)==40
assert find_angle(50,40)==90
