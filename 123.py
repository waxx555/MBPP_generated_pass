'''
Write a function to sum all amicable numbers from 1 to a specified number.
'''

def amicable_numbers_sum(n):
    def sum_of_divisors(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum

    amicable_sum = 0
    for i in range(1, n+1):
        if i == sum_of_divisors(sum_of_divisors(i)) and i != sum_of_divisors(i):
            amicable_sum += i
    return amicable_sum


assert amicable_numbers_sum(999)==504
assert amicable_numbers_sum(9999)==31626
assert amicable_numbers_sum(99)==0
