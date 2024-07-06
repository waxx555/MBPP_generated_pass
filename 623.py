'''
Write a function to find the n-th power of individual elements in a list using lambda function.
'''

def nth_nums(lst,n):
    return [i**n for i in lst]


assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
assert nth_nums([10,20,30],3)==([1000, 8000, 27000])
assert nth_nums([12,15],5)==([248832, 759375])
