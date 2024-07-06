'''
Write a python function to find the hamming distance between given two integers.
'''

def hamming_Distance(x,y):
    return bin(x^y).count('1')


assert hamming_Distance(4,8) == 2
assert hamming_Distance(2,4) == 2
assert hamming_Distance(1,2) == 2
