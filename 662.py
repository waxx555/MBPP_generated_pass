'''
Write a function to sort a list in a dictionary.
'''

def sorted_dict(d):
    for i in d:
        d[i].sort()
    return d


assert sorted_dict({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]})=={'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
assert sorted_dict({'n1': [25,37,41], 'n2': [41,54,63], 'n3': [29,38,93]})=={'n1': [25, 37, 41], 'n2': [41, 54, 63], 'n3': [29, 38, 93]}
assert sorted_dict({'n1': [58,44,56], 'n2': [91,34,58], 'n3': [100,200,300]})=={'n1': [44, 56, 58], 'n2': [34, 58, 91], 'n3': [100, 200, 300]}
