'''
Write a python function to find the most significant bit number which is also a set bit.
'''

def set_Bit_Number(n):
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n ^ (n >> 1)


assert set_Bit_Number(6) == 4
assert set_Bit_Number(10) == 8
assert set_Bit_Number(18) == 16
