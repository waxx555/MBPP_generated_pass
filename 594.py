'''
Write a function to find the difference of first even and odd number of a given list.
'''

def diff_even_odd(arr):
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even = i
            break
    for i in arr:
        if i % 2 != 0:
            odd = i
            break
    return even - odd


assert diff_even_odd([1,3,5,7,4,1,6,8])==3
assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
assert diff_even_odd([1,5,7,9,10])==9
