'''
Write a python function to toggle only first and last bits of a given number.
'''

def toggle_F_and_L_bits(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n ^ (1 << (n.bit_length() - 1)) ^ 1


assert toggle_F_and_L_bits(10) == 3
assert toggle_F_and_L_bits(15) == 6
assert toggle_F_and_L_bits(20) == 5
