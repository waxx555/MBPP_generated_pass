'''
Write a function to add all the numbers in a list and divide it with the length of the list.
'''

def sum_num(lst):
    return sum(lst)/len(lst)


assert sum_num((8, 2, 3, 0, 7))==4.0
assert sum_num((-10,-20,-30))==-20.0
assert sum_num((19,15,18))==17.333333333333332
