'''
Write a python function to count the number of lists in a given number of lists.
'''

def count_list(lst):
    return len(lst)


assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
assert count_list([[1,2],[2,3],[4,5]]) == 3
assert count_list([[1,0],[2,0]]) == 2
