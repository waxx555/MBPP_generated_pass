'''
Write a python function to find the first repeated character in a given string.
'''

def first_repeated_char(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return s[i]
    return "None"



assert first_repeated_char("abcabc") == "a"
assert first_repeated_char("abc") == "None"
assert first_repeated_char("123123") == "1"
