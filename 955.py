'''
Write a function to find out, if the given number is abundant.
'''

def is_abundant(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum > n


assert is_abundant(12)==True
assert is_abundant(13)==False
assert is_abundant(9)==False
