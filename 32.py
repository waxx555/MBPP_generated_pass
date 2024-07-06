'''
Write a python function to find the largest prime factor of a given number.
'''

def max_Prime_Factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n



assert max_Prime_Factors(15) == 5
assert max_Prime_Factors(6) == 3
assert max_Prime_Factors(2) == 2
