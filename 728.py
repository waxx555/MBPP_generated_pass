'''
Write a function to sum elements in two lists.
'''

def sum_list(l1, l2):
    return [x+y for x,y in zip(l1,l2)]


assert sum_list([10,20,30],[15,25,35])==[25,45,65]
assert sum_list([1,2,3],[5,6,7])==[6,8,10]
assert sum_list([15,20,30],[15,45,75])==[30,65,105]
