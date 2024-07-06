'''
Write a function to convert a list of multiple integers into a single integer.
'''

def multiple_to_single(lst):
    return int(''.join(map(str,lst)))



assert multiple_to_single([11, 33, 50])==113350
assert multiple_to_single([-1,2,3,4,5,6])==-123456
assert multiple_to_single([10,15,20,25])==10152025
