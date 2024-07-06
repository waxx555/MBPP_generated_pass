'''
Write a python function to find the length of the shortest word.
'''

def len_log(lst):
    return min([len(i) for i in lst])


assert len_log(["win","lose","great"]) == 3
assert len_log(["a","ab","abc"]) == 1
assert len_log(["12","12","1234"]) == 2
