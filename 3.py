'''
Write a python function to identify non-prime numbers.
'''

def is_not_prime(n):
    if n < 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return True
    return False



assert is_not_prime(2) == False
assert is_not_prime(10) == True
assert is_not_prime(35) == True
