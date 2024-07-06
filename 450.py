'''
Write a function to extract specified size of strings from a give list of string values.
'''

def extract_string(lst, n):
    return [i for i in lst if len(i)==n]


assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']
