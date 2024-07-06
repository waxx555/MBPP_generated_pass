'''
Write a function to check if each element of second tuple is smaller than its corresponding index in first tuple.
'''

def check_smaller(t1, t2):
    return all(t1[i] > t2[i] for i in range(len(t1)))


assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((4, 5, 6), (3, 4, 5)) == True
assert check_smaller((11, 12, 13), (10, 11, 12)) == True
