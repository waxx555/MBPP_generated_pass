'''
Write a python function to find the sum of even factors of a number.
'''

def sumofFactors(n):
    sum = 0
    for i in range(2, n+1, 2):
        if n % i == 0:
            sum += i
    return sum


assert sumofFactors(18) == 26
assert sumofFactors(30) == 48
assert sumofFactors(6) == 8
