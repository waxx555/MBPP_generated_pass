'''
Write a python function to find the sum of non-repeated elements in a given array.
'''

def find_Sum(arr, n):
    return sum(set(arr))


assert find_Sum([1,2,3,1,1,4,5,6],8) == 21
assert find_Sum([1,10,9,4,2,10,10,45,4],9) == 71
assert find_Sum([12,10,9,45,2,10,10,45,10],9) == 78
