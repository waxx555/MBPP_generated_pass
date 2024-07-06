'''
Write a python function to find the minimum length of sublist.
'''

def Find_Min_Length(lst):
    return min(map(len,lst))


assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
