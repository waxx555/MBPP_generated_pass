'''
Write a function to count character frequency of a given string.
'''

def char_frequency(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    return freq


assert char_frequency('python')=={'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
assert char_frequency('program')=={'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 1}
assert char_frequency('language')=={'l': 1, 'a': 2, 'n': 1, 'g': 2, 'u': 1, 'e': 1}
