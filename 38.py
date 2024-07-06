'''
Write a function to find the division of first even and odd number of a given list.
'''

def div_even_odd(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            for j in range(len(arr)):
                if arr[j]%2!=0:
                    return arr[i]//arr[j]
    return -1



assert div_even_odd([1,3,5,7,4,1,6,8])==4
assert div_even_odd([1,2,3,4,5,6,7,8,9,10])==2
assert div_even_odd([1,5,7,9,10])==10
