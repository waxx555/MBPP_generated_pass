'''
Write a function to find all the values in a list that are greater than a specified number.
'''

def greater_specificnum(arr,n):
    return all(i>n for i in arr)


assert greater_specificnum([220, 330, 500],200)==True
assert greater_specificnum([12, 17, 21],20)==False
assert greater_specificnum([1,2,3,4],10)==False
