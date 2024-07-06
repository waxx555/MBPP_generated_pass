'''
Write a function to find the nth octagonal number.
'''

def is_octagonal(n):
    return n*(3*n-2)


assert is_octagonal(5) == 65
assert is_octagonal(10) == 280
assert is_octagonal(15) == 645
