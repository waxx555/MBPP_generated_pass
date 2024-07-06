'''
Write a python function to count set bits of a given number.
'''

def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


assert count_Set_Bits(2) == 1
assert count_Set_Bits(4) == 1
assert count_Set_Bits(6) == 2
