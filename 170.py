'''
Write a function to find sum of the numbers in a list between the indices of a specified range.
'''

def sum_range_list(arr,start,end):
    return sum(arr[start:end+1])


assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],8,10)==29
assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],5,7)==16
assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],7,10)==38
