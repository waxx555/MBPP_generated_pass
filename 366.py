'''
Write a python function to find the largest product of the pair of adjacent elements from a given list of integers.
'''

def adjacent_num_product(arr):
    return max([arr[i]*arr[i+1] for i in range(len(arr)-1)])


assert adjacent_num_product([1,2,3,4,5,6]) == 30
assert adjacent_num_product([1,2,3,4,5]) == 20
assert adjacent_num_product([2,3]) == 6
