'''
Write a python function to find the maximum sum of elements of list in a list of lists.
'''

def maximum_Sum(lst):
    return max([sum(i) for i in lst])



assert maximum_Sum([[1,2,3],[4,5,6],[10,11,12],[7,8,9]]) == 33
assert maximum_Sum([[0,1,1],[1,1,2],[3,2,1]]) == 6
assert maximum_Sum([[0,1,3],[1,2,1],[9,8,2],[0,1,0],[6,4,8]]) == 19
