'''
Write a python function to find lcm of two positive integers.
'''

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm


assert lcm(4,6) == 12
assert lcm(15,17) == 255
assert lcm(2,6) == 6
