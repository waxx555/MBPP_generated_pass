'''
Write a python function to check whether two given lines are parallel or not.
'''

def parallel_lines(l1,l2):
    return l1[0]/l1[1] == l2[0]/l2[1]


assert parallel_lines([2,3,4], [2,3,8]) == True
assert parallel_lines([2,3,4], [4,-3,8]) == False
assert parallel_lines([3,3],[5,5]) == True
