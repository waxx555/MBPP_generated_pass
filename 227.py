'''
Write a function to find minimum of three numbers.
'''

def min_of_three(a,b,c):
    return min(a,b,c)


assert min_of_three(10,20,0)==0
assert min_of_three(19,15,18)==15
assert min_of_three(-10,-20,-30)==-30
