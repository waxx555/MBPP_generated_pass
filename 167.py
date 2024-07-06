'''
Write a python function to find smallest power of 2 greater than or equal to n.
'''

def next_Power_Of_2(n):
    p = 1
    if n and not (n & (n - 1)):
        return n
    while p < n:
        p <<= 1
    return p


assert next_Power_Of_2(0) == 1
assert next_Power_Of_2(5) == 8
assert next_Power_Of_2(17) == 32
