'''
Write a python function to find the sublist having maximum length.
'''

def Find_Max(arr):
    return max(arr,key=len)



assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]
