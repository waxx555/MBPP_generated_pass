'''
Write a function to multiply the adjacent elements of the given tuple.
'''

def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))


assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
assert multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
