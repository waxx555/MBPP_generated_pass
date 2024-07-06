'''
Write a function to substaract two lists using map and lambda function.
'''

def sub_list(lst1,lst2):
    return list(map(lambda x,y: x-y,lst1,lst2))


assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
assert sub_list([1,2],[3,4])==[-2,-2]
assert sub_list([90,120],[50,70])==[40,50]
