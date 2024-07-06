'''
Write a python function to check whether the two numbers differ at one bit position only or not.
'''

def differ_At_One_Bit_Pos(x, y):
    return bin(x ^ y).count('1') == 1



assert differ_At_One_Bit_Pos(13,9) == True
assert differ_At_One_Bit_Pos(15,8) == False
assert differ_At_One_Bit_Pos(2,4) == False
