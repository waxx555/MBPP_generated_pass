'''
Write a function to check whether the given number is armstrong or not.
'''

def armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return n == sum


assert armstrong_number(153)==True
assert armstrong_number(259)==False
assert armstrong_number(4458)==False
