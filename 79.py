'''
Write a python function to check whether the length of the word is odd or not.
'''

def word_len(word):
    return len(word)%2!=0


assert word_len("Hadoop") == False
assert word_len("great") == True
assert word_len("structure") == True
