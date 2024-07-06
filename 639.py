'''
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
'''

def sample_nam(lst):
    return sum(len(i) for i in lst if i[0].isupper())


assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
assert sample_nam(["abcd", "Python", "abba", "aba"])==6
