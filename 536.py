'''
Write a function to select the nth items of a list.
'''

def nth_items(lst, n):
    return lst[::n]


assert nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9],2)==[1, 3, 5, 7, 9] 
assert nth_items([10,15,19,17,16,18],3)==[10,17] 
assert nth_items([14,16,19,15,17],4)==[14,17]
