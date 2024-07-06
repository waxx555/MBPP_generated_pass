'''
Write a function to remove duplicate words from a given string using collections module.
'''

from collections import Counter

def remove_duplicate(s):
    return ' '.join(Counter(s.split()).keys())


assert remove_duplicate("Python Exercises Practice Solution Exercises")==("Python Exercises Practice Solution")
assert remove_duplicate("Python Exercises Practice Solution Python")==("Python Exercises Practice Solution")
assert remove_duplicate("Python Exercises Practice Solution Practice")==("Python Exercises Practice Solution")
