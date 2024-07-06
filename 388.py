'''
Write a python function to find the highest power of 2 that is less than or equal to n.
'''

def highest_Power_of_2(n):
    return 2**(n.bit_length()-1)


assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(19) == 16
assert highest_Power_of_2(32) == 32
