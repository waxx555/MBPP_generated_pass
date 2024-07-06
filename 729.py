'''
Write a function to add two lists using map and lambda function.
'''

def add_list(l1, l2):
    return list(map(lambda x, y: x + y, l1, l2))


assert add_list([1, 2, 3],[4,5,6])==[5, 7, 9]
assert add_list([1,2],[3,4])==[4,6]
assert add_list([10,20],[50,70])==[60,90]
