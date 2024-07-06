'''
Write a python function to count lower case letters in a given string.
'''

def lower_ctr(s):
    count = 0
    for i in s:
        if i.islower():
            count += 1
    return count


assert lower_ctr('abc') == 3
assert lower_ctr('string') == 6
assert lower_ctr('Python') == 5
