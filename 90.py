'''
Write a python function to find the length of the longest word.
'''

def len_log(words):
    return len(max(words, key=len))


assert len_log(["python","PHP","bigdata"]) == 7
assert len_log(["a","ab","abc"]) == 3
assert len_log(["small","big","tall"]) == 5
