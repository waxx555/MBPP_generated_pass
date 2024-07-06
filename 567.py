'''
Write a function to check whether a specified list is sorted or not.
'''

def issort_list(lst):
    return lst == sorted(lst)


assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False
