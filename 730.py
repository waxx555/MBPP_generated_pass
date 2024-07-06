'''
Write a function to remove consecutive duplicates of a given list.
'''

def consecutive_duplicates(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]


assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
assert consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[10, 15, 19, 18, 17, 26, 17, 18, 10]
assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==['a', 'b', 'c', 'd']
