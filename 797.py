'''
Write a python function to find the sum of all odd natural numbers within the range l and r.
'''

def sum_in_Range(l, r):
    return sum(i for i in range(l,r+1) if i%2!=0)


assert sum_in_Range(2,5) == 8
assert sum_in_Range(5,7) == 12
assert sum_in_Range(7,13) == 40
