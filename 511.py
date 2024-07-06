'''
Write a python function to find minimum sum of factors of a given number.
'''

def find_Min_Sum(n):
    sum = 0
    i = 2
    while(i*i <= n):
        while(n%i == 0):
            sum += i
            n //= i
        i += 1
    sum += n
    return sum


assert find_Min_Sum(12) == 7
assert find_Min_Sum(105) == 15
assert find_Min_Sum(2) == 2
