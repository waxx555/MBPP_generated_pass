'''
Write a function to calculate the sum of the positive numbers of a given list of numbers using lambda function.
'''

def sum_positivenum(lst):
    return sum(list(filter(lambda x:x>0,lst)))

assert sum_positivenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==48
assert sum_positivenum([10,15,-14,13,-18,12,-20])==50
assert sum_positivenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==522
