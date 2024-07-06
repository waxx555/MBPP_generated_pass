'''
Write a function to add two integers. however, if the sum is between the given range it will return 20.
'''

def sum_nums(a,b,x,y):
    return 20 if x <= a+b <= y else a+b


assert sum_nums(2,10,11,20)==20
assert sum_nums(15,17,1,10)==32
assert sum_nums(10,15,5,30)==20
