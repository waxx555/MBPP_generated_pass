'''
Write a python function to check whether the given number can be represented by sum of two squares or not.
'''

def sum_Square(n):
    for i in range(n):
        for j in range(n):
            if i * i + j * j == n:
                return True
    return False


assert sum_Square(25) == True
assert sum_Square(24) == False
assert sum_Square(17) == True
