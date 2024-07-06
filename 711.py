'''
Write a python function to check whether the product of digits of a number at even and odd places is equal or not.
'''

def product_Equal(n):
    n = str(n)
    even = 1
    odd = 1
    for i in range(len(n)):
        if i % 2 == 0:
            even *= int(n[i])
        else:
            odd *= int(n[i])
    return even == odd


assert product_Equal(2841) == True
assert product_Equal(1234) == False
assert product_Equal(1212) == False
