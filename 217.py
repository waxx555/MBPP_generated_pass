'''
Write a python function to find the first repeated character in a given string.
'''

def first_Repeated_Char(s):
    char_set = set()
    for i in s:
        if i in char_set:
            return i
        char_set.add(i)
    return '\0'


assert first_Repeated_Char("Google") == "o"
assert first_Repeated_Char("data") == "a"
assert first_Repeated_Char("python") == '\0'
