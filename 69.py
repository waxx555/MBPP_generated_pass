'''
Write a function to check whether a list contains the given sublist or not.
'''

def is_sublist(lst,sublst):
    n = len(sublst)
    for i in range(len(lst)-n+1):
        if lst[i:i+n]==sublst:
            return True
    return False


assert is_sublist([2,4,3,5,7],[3,7])==False
assert is_sublist([2,4,3,5,7],[4,3])==True
assert is_sublist([2,4,3,5,7],[1,6])==False
