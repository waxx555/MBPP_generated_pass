'''
Write a python function to count unset bits of a given number.
'''

def count_unset_bits(n):
    count = 0
    while n:
        count += 1 if n & 1 == 0 else 0
        n >>= 1
    return count


assert count_unset_bits(2) == 1
assert count_unset_bits(4) == 2
assert count_unset_bits(6) == 1
