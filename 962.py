'''
Write a python function to find the sum of all even natural numbers within the range l and r.
'''

def sum_Even(l, r):
    sum = 0
    for i in range(l, r+1):
        if i % 2 == 0:
            sum += i
    return sum


assert sum_Even(2,5) == 6
assert sum_Even(3,8) == 18
assert sum_Even(4,6) == 10
