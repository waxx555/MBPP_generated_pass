'''
Write a function to find the occurence of characters 'std' in the given string 1. list item 1. list item 1. list item 2. list item 2. list item 2. list item
'''

def count_occurance(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == "std":
            count += 1
    return count


assert count_occurance("letstdlenstdporstd") == 3
assert count_occurance("truststdsolensporsd") == 1
assert count_occurance("makestdsostdworthit") == 2
