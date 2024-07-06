'''
Write a function to find number of odd elements in the given list using lambda function.
'''

count_odd = lambda lst: len([i for i in lst if i%2!=0])


assert count_odd([1, 2, 3, 5, 7, 8, 10])==4
assert count_odd([10,15,14,13,-18,12,-20])==2
assert count_odd([1, 2, 4, 8, 9])==2
