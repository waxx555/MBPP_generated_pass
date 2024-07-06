'''
Write a function to multiply two integers without using the * operator in python.
'''

def multiply_int(a, b):
    result = 0
    for i in range(b):
        result += a
    return result


assert multiply_int(10,20)==200
assert multiply_int(5,10)==50
assert multiply_int(4,8)==32
