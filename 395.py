'''
Write a python function to find the first non-repeated character in a given string.
'''

def first_non_repeating_character(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None


assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abc") == "a"
assert first_non_repeating_character("ababc") == "c"
