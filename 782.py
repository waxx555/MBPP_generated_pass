'''
Write a python function to find the sum of all odd length subarrays.
'''

def Odd_Length_Sum(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += ((i+1) * (n-i) + 1) // 2 * arr[i]
    return sum


assert Odd_Length_Sum([1,2,4]) == 14
assert Odd_Length_Sum([1,2,1,2]) == 15
assert Odd_Length_Sum([1,7]) == 8
