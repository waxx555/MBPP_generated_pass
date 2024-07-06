'''
Write a function to shortlist words that are longer than n from a given list of words.
'''

def long_words(n, s):
    return [word for word in s.split() if len(word) > n]


assert long_words(3,"python is a programming language")==['python','programming','language']
assert long_words(2,"writing a program")==['writing','program']
assert long_words(5,"sorting list")==['sorting']
