'''
Write a python function to calculate the sum of the numbers in a list between the indices of a specified range.
'''

def sum_Range_list(lst, start, end):
    return sum(lst[start:end+1])


assert sum_Range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12],8,10) == 29
assert sum_Range_list([1,2,3,4,5],1,2) == 5
assert sum_Range_list([1,0,1,2,5,6],4,5) == 11
