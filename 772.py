'''
Write a function to remove all the words with k length in the given string.
'''

def remove_length(s, k):
    return ' '.join([i for i in s.split() if len(i) != k])


assert remove_length('The person is most value tet', 3) == 'person is most value'
assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'
