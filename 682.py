'''
Write a function to multiply two lists using map and lambda function.
'''

def mul_list(l1,l2):
    return list(map(lambda x,y:x*y,l1,l2))


assert mul_list([1, 2, 3],[4,5,6])==[4,10,18]
assert mul_list([1,2],[3,4])==[3,8]
assert mul_list([90,120],[50,70])==[4500,8400]
