'''
Write a function to check whether it follows the sequence given in the patterns array.
'''

def is_samepatterns(lst, patterns):
    return len(set(lst))==len(set(patterns))==len(set(zip(lst,patterns)))


assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True 
assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False 
assert is_samepatterns(["red","green","greenn"], ["a","b"])==False 
