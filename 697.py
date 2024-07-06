'''
Write a function to find number of even elements in the given list using lambda function.
'''

count_even = lambda l: len(list(filter(lambda x: x % 2 == 0, l)))

assert count_even([1, 2, 3, 5, 7, 8, 9, 10])==3
assert count_even([10,15,14,13,-18,12,-20])==5
assert count_even([1, 2, 4, 8, 9])==3
