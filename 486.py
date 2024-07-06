'''
Write a function to compute binomial probability for the given number.
'''

def binomial_probability(n, k, p):
    from math import factorial
    return factorial(n)/(factorial(k)*factorial(n-k)) * p**k * (1-p)**(n-k)


assert binomial_probability(10, 5, 1.0/3) == 0.13656454808718185
assert binomial_probability(11, 6, 2.0/4) == 0.2255859375
assert binomial_probability(12, 7, 3.0/5) == 0.227030335488
