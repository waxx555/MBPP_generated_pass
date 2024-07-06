'''
Write a python function to left rotate the bits of a given number.
'''

def left_Rotate(n, d):
    return (n << d) | (n >> (32 - d))


assert left_Rotate(16,2) == 64
assert left_Rotate(10,2) == 40
assert left_Rotate(99,3) == 792
