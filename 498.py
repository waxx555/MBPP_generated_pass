'''
Write a python function to find gcd of two positive integers.
'''

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)


assert gcd(12, 17) == 1
assert gcd(4,6) == 2
assert gcd(2,9) == 1
