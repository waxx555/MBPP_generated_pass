'''
Write a function to multiply consecutive numbers of a given list.
'''

def mul_consecutive_nums(lst):
    return [lst[i]*lst[i+1] for i in range(len(lst)-1)]


assert mul_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7])==[1, 3, 12, 16, 20, 30, 42]
assert mul_consecutive_nums([4, 5, 8, 9, 6, 10])==[20, 40, 72, 54, 60]
assert mul_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[2, 6, 12, 20, 30, 42, 56, 72, 90]
