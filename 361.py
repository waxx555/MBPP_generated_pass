'''
Write a function to remove empty lists from a given list of lists.
'''

def remove_empty(arr):
    return [i for i in arr if i]


assert remove_empty([[], [], [], 'Red', 'Green', [1,2], 'Blue', [], []])==['Red', 'Green', [1, 2], 'Blue']
assert remove_empty([[], [], [],[],[], 'Green', [1,2], 'Blue', [], []])==[ 'Green', [1, 2], 'Blue']
assert remove_empty([[], [], [], 'Python',[],[], 'programming', 'language',[],[],[], [], []])==['Python', 'programming', 'language']
