'''
Write a python function to check whether the length of the word is even or not.
'''

def word_len(s):
    return len(s) % 2 == 0


assert word_len("program") == False
assert word_len("solution") == True
assert word_len("data") == True
