'''
Write a function to calculate the permutation coefficient of given p(n, k).
'''

def permutation_coefficient(n, k):
    fact = 1
    for i in range(n, n - k, -1):
        fact *= i
    return fact


assert permutation_coefficient(10, 2) == 90
assert permutation_coefficient(10, 3) == 720
assert permutation_coefficient(10, 1) == 10
