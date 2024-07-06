'''
Write a function to flatten the tuple list to a string.
'''

def flatten_tuple(t):
    return ' '.join([x for i in t for x in i])


assert flatten_tuple([('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]) == '1 4 6 5 8 2 9 1 10'
assert flatten_tuple([('2', '3', '4'), ('6', '9'), ('3', '2'), ('2', '11')]) == '2 3 4 6 9 3 2 2 11'
assert flatten_tuple([('14', '21', '9'), ('24', '19'), ('12', '29'), ('23', '17')]) == '14 21 9 24 19 12 29 23 17'
