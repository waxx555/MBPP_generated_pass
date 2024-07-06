'''
Write a function to find if the given number is abundant or not.
'''

def check_abundant(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum > n


assert check_abundant(12) == True
assert check_abundant(15) == False
assert check_abundant(18) == True
