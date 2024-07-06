'''
Write a python function to check whether the product of numbers is even or not.
'''

def is_Product_Even(arr,n):
    for i in range(n):
        if arr[i] % 2 == 0:
            return True
    return False


assert is_Product_Even([1,2,3],3) == True
assert is_Product_Even([1,2,1,4],4) == True
assert is_Product_Even([1,1],2) == False
