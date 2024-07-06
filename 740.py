'''
Write a function to convert the given tuple to a key-value dictionary using adjacent elements.
'''

def tuple_to_dict(t):
    return {t[i]: t[i + 1] for i in range(0, len(t), 2)}


assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}
