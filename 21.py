'''
Write a function to find m number of multiples of n.
'''

def multiples_of_num(m,n):
    return [n*i for i in range(1,m+1)]




assert multiples_of_num(4,3)== [3,6,9,12]
assert multiples_of_num(2,5)== [5,10]
assert multiples_of_num(9,2)== [2,4,6,8,10,12,14,16,18]
