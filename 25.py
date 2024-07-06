'''
Write a python function to find the product of non-repeated elements in a given array.
'''

def find_Product(arr,n):
    product = 1
    for i in range(n):
        if arr.count(arr[i])==1:
            product *= arr[i]
    return product




assert find_Product([1,1,2,3],4) == 6
assert find_Product([1,2,3,1,1],5) == 6
assert find_Product([1,1,4,5,6],5) == 120
