'''
Write a function to assign frequency to each tuple in the given tuple list.
'''

def assign_freq(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return str([i + (freq[i],) for i in freq])


assert assign_freq([(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)] ) == '[(6, 5, 8, 3), (2, 7, 2), (9, 1)]'
assert assign_freq([(4, 2, 4), (7, 1), (4, 8), (4, 2, 4), (9, 2), (7, 1)] ) == '[(4, 2, 4, 2), (7, 1, 2), (4, 8, 1), (9, 2, 1)]'
assert assign_freq([(11, 13, 10), (17, 21), (4, 2, 3), (17, 21), (9, 2), (4, 2, 3)] ) == '[(11, 13, 10, 1), (17, 21, 2), (4, 2, 3, 2), (9, 2, 1)]'
