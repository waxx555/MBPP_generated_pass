'''
Write a python function to count number of non-empty substrings of a given string.
'''

def number_of_substrings(s):
    return int(len(s)*(len(s)+1)/2)


assert number_of_substrings("abc") == 6
assert number_of_substrings("abcd") == 10
assert number_of_substrings("abcde") == 15
