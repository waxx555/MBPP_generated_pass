'''
Write a python function to count the occurrence of a given character in a string.
'''

def count(s,c):
    return s.count(c)


assert count("abcc","c") == 2
assert count("ababca","a") == 3
assert count("mnmm0pm","m") == 4
