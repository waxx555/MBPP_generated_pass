'''
Write a python function to find common divisor between two numbers in a given pair.
'''

def num_comm_div(x, y):
    n = 0
    for i in range(1, min(x, y)+1):
        if x % i == y % i == 0:
            n += 1
    return n


assert num_comm_div(2,4) == 2
assert num_comm_div(2,8) == 2
assert num_comm_div(12,24) == 6
