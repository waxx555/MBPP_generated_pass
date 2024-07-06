'''
Write a function to check if each element of the second tuple is greater than its corresponding index in the first tuple.
'''

def check_greater(t1, t2):
    return all(t2[i] > t1[i] for i in range(len(t1)))
               

assert check_greater((10, 4, 5), (13, 5, 18)) == True
assert check_greater((1, 2, 3), (2, 1, 4)) == False
assert check_greater((4, 5, 6), (5, 6, 7)) == True
