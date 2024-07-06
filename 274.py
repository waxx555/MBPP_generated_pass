'''
Write a python function to find sum of even index binomial coefficients.
'''
def binomialCoeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum += binomialCoeff(n, i)
    return sum


assert even_binomial_Coeff_Sum(4) == 8
assert even_binomial_Coeff_Sum(6) == 32
assert even_binomial_Coeff_Sum(2) == 2
