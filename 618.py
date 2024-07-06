'''
Write a function to divide two lists using map and lambda function.
'''

def div_list(l1, l2):
    return list(map(lambda x, y: x/y, l1, l2))


assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
assert div_list([3,2],[1,4])==[3.0, 0.5]
assert div_list([90,120],[50,70])==[1.8, 1.7142857142857142]
