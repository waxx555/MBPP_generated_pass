'''
Write a function to sum a specific column of a list in a given list of lists.
'''

def sum_column(lst, index):
    return sum([i[index] for i in lst])


assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],0)==12
assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],1)==15
assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],3)==9
