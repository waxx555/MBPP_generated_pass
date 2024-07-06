'''
Write a function to reverse words in a given string.
'''

def reverse_words(s):
    return " ".join(s.split()[::-1])


assert reverse_words("python program")==("program python")
assert reverse_words("java language")==("language java")
assert reverse_words("indian man")==("man indian")
