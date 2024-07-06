'''
Write a function to calculate the sum of the negative numbers of a given list of numbers using lambda function.
'''

sum_negativenum = lambda l: sum([i for i in l if i < 0])


assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
assert sum_negativenum([10,15,-14,13,-18,12,-20])==-52
assert sum_negativenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==-894
