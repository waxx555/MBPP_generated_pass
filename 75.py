'''
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
'''

def find_tuples(tuples, k):
    return str([i for i in tuples if all(j%k==0 for j in i)])


assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == '[(6, 24, 12)]'
assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == '[(5, 25, 30)]'
assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == '[(8, 16, 4)]'
