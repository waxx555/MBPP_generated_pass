'''
Write a python function to find the sum of the three lowest positive numbers from a given list of numbers.
'''

def sum_three_smallest_nums(lst):
    return sum(sorted([x for x in lst if x > 0])[:3])


assert sum_three_smallest_nums([10,20,30,40,50,60,7]) == 37
assert sum_three_smallest_nums([1,2,3,4,5]) == 6
assert sum_three_smallest_nums([0,1,2,3,4,5]) == 6
