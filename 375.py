'''
Write a function to round the given number to the nearest multiple of a specific number.
'''

def round_num(n,m):
    return n//m*m


assert round_num(4722,10)==4720
assert round_num(1111,5)==1110
assert round_num(219,2)==218
