'''
Write a function to count unique keys for each value present in the tuple.
'''

def get_unique(t):
    d = {}
    for i in t:
        if i[1] in d:
            d[i[1]] += 1
        else:
            d[i[1]] = 1
    return str(d)


assert get_unique([(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1), (9, 1), (8, 4), (10, 4)] ) == '{4: 4, 2: 3, 1: 2}'
assert get_unique([(4, 5), (2, 3), (3, 5), (9, 3), (8, 3), (9, 2), (10, 2), (9, 5), (11, 5)] ) == '{5: 4, 3: 3, 2: 2}'
assert get_unique([(6, 5), (3, 4), (2, 6), (11, 1), (8, 22), (8, 11), (4, 3), (14, 3), (11, 6)] ) == '{5: 1, 4: 1, 6: 2, 1: 1, 22: 1, 11: 1, 3: 2}'
