'''
Write a python function to check whether the given number can be represented as difference of two squares or not.
'''

def dif_Square(n):
    for i in range(n):
        for j in range(n):
            if i**2-j**2==n:
                return True
    return False


assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True
