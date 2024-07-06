'''
Write a function to find the greatest common divisor (gcd) of two integers by using recursion.
'''

def recur_gcd(a, b):
    if b == 0:
        return a
    else:
        return recur_gcd(b, a % b)
    

assert recur_gcd(12,14) == 2
assert recur_gcd(13,17) == 1
assert recur_gcd(9, 3) == 3
