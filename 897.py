'''
Write a python function to check whether the word is present in a given sentence or not.
'''

def is_Word_Present(sentence, word):
    return word in sentence


assert is_Word_Present("machine learning","machine") == True
assert is_Word_Present("easy","fun") == False
assert is_Word_Present("python language","code") == False
