'''
Write a function to multiply all the numbers in a list and divide with the length of the list.
'''
def reduce(func,seq):
    result=seq[0]
    for i in seq[1:]:
        result=func(result,i)
    return result
def multiply_num(lst):
    return round((reduce(lambda x,y: x*y,lst)/len(lst)),1)


assert multiply_num((8, 2, 3, -1, 7))==-67.2
assert multiply_num((-10,-20,-30))==-2000.0
assert multiply_num((19,15,18))==1710.0
