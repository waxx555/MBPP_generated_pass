'''
Write a python function to find the sum of fourth power of n natural numbers.
'''

def fourth_Power_Sum(n):
    return n*(n+1)*(2*n+1)*(3*n*n+3*n-1)//30


assert fourth_Power_Sum(2) == 17
assert fourth_Power_Sum(4) == 354
assert fourth_Power_Sum(6) == 2275
