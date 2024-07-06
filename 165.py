'''
Write a python function to count characters at same position in a given string (lower and uppercase characters) as in english alphabet.
'''

def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if s[i].lower() == chr(97+i):
            count += 1
    return count


assert count_char_position("xbcefg") == 2
assert count_char_position("ABcED") == 3
assert count_char_position("AbgdeF") == 5
